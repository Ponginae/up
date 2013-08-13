Up - A next generation status monitor
=====================================

Some times you just need to know, is it up? The goal of this project is to create a easy to use, but highly customizable status monitor.

Setup
-----

First start by installing the environment.

::
    $ mkdir example-status

    $ cd example-status

    $ virtualenv . -p python3 --no-site-packages

    $ bin/pip install up

Now you need to create the `upfile.py`. It goes in the same folder as everything else. From here you can setup what you want to monitor.

::

    from up import status, source

    class ExampleStatus(status.StatusMonitor):

        source = source.HTTPStatusSource('Example Status', 'https://example.com/')
        sink = sink.StdOutStatusSink()

You can now run it like this.

::

    $ bin/up
    Example Status: UP

Developers Setup
----------------

::

    $ virtualenv . -p python3 --no-site-packages

    $ bin/python setup.py develop
