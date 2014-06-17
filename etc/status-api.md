Status API
==========

A status has a name, a value 'up' indicating if the corrosponding serivce will
give a good response, and a reason that gives additional, human readable,
information on why the service is not up.

The name should be unique, it will be the key used to aggregate statistics.

```javascript
{
	"name": "Statusey Thing",
	"date": 1371302613.0897678,
	"duration": 3424.004,
	"up": true,
	"reason": "This really only has meaning if 'up' is false."
}
```

Sometimes your application is not completely down. In that case you can specify
"up" as a number between 0 and 1 indicating what percentage of your applicaton
is up.

```javascript
{
	"name": "Modular Statusey Thing",
	"date": 1371302613.0897678,
	"duration": 3424.004,
	"up": 0.6,
	"reason": "Some modules are down and some are up."
}
```

For more fine grained information, statuses can take the form of trees. Each
node in the tree has branches that point to a status that gives more
information.

In the case of downstream services names must be unique to its parent status.
The status of the cluster is then computed as a percentage of the downstream
nodes.

```javascript
{
	"name": "Statusey Cluster",
	"date": 1371302613.0897678,
	"duration": 3424.004,
	"reason": "One or more Statusey Things in this cluster are down.",
	"downstream": [
		{
			"name": "Statusey Thing 1",
			"date": 1371302613.0897678,
			"duration": 1501.002,
			"up": true
		}, {
			"name": "Statusey Thing 2",
			"up": false,
			"date": 1371304114.0917678,
			"duration": 1923.002,
			"reason": "Something happened, and it was bad."
		}
	]
}
```

You can also point to another status api compliant server.

```javascript
{
	"name": "Statusey Proxy",
	"date": 1371302613.0897678,
	"duration": 3424.004,
	"downstream": [
		"http://status1.example.com/status",
		"http://status2.example.com/status"
	]
}
```

The other two required parameters are date and duration. The date is the number
of seconds from the unix epoch, and indicaties when the status check began.

The duration is the number of seconds it took to determine the status. Starting
at the date indicated by "date".
