Status API
==========

A status has a name, a value 'up' indicating if the corrosponding serivce will
give a good response, and a reason that gives additional, human readable,
information on why the service is not up.

The name should be unique, it will be the key used to aggregate statistics.

{
	"name": "Statusey Thing",
	"date": 1371302613.0897678,
	"duration": 3424.004,
	"up": true,
	"reason": "This really only has meaning of 'up' is false."
}

Statuses can take the form of trees. Each node in the tree has a status and
then each branch points to a status that gives more detailed information.

In the case of downstream services names must be unique to its parent status.

{
	"name": "Statusey Cluster",
	"up": false,
	"reason": "One or more Statusey Things in this cluster are down.",
	"downstream": [
		{
			"name": "Statusey Thing 1",
			"up": true
		}, {
			"name": "Statusey Thing 2",
			"up": false,
			"reason": "Something happened, and it was bad."
		}
	]
}

You can also point to another status api compliant server.

{
	"name": "Statusey Proxy",
	"up": false,
	"reason": "One or more Statusey Things in this cluster are down.",
	"downstream": [
		"http://status1.example.com/status",
		"http://status2.example.com/status"
	]
}
