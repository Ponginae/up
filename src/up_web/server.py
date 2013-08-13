from flask import Flask, request, render_template
from pymongo import MongoClient, ASCENDING
import json
import datetime
from bson.objectid import ObjectId
from werkzeug import Response

app = Flask(__name__)

DB_NAME = 'up'
DB_DOMAIN = 'localhost'
DB_PORT = 27017
COLLECTION_NAME = 'statuses'

client = MongoClient(DB_DOMAIN, DB_PORT)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


class MongoJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def jsonify(obj):
    """ jsonify with support for MongoDB ObjectId
    """
    return Response(json.dumps(obj, cls=MongoJsonEncoder), mimetype='application/json')


@app.route("/aggregate/by_name/")
def by_name():
    data = []

    if 'name' in request.args:
        cursor = collection.find({
            'path': request.args['name']
        })
        cursor.sort('date', ASCENDING)
        data = list(cursor)

    return jsonify(data)


@app.route("/annotations/")
def annotations():
    cursor = db.annotations.find()
    cursor.sort('date', ASCENDING)
    data = list(cursor)

    return jsonify(data)


@app.route('/')
def home():
    paths = collection.distinct('path')
    paths.sort()

    return render_template('home.html', paths=paths)

if __name__ == "__main__":
    app.debug = True
    app.run()
