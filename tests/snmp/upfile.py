from up import status, source, sink


class ExampleStatus(status.StatusMonitor):

    source = source.StatusTreeSource('SNMP Tests', [
        source.SNMPStatusSource('Test With name', 'demo.snmplabs.com'),
        source.SNMPStatusSource(domain='demo.snmplabs.com')
    ])
    sink = sink.StdOutStatusSink()
