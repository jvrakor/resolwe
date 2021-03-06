""".. Ignore pydocstyle D400.

=============
Elastic Utils
=============

Collection of convenient functions and shortcuts that simplifies using
the app.

.. autofunction:: resolwe.elastic.utils.const

"""
from __future__ import absolute_import, division, print_function, unicode_literals

from elasticsearch_dsl.connections import connections

from django.conf import settings
from django.test import SimpleTestCase, override_settings

__all__ = ('const', 'prepare_connection')


def const(con):
    """Define a constant mapping for elastic search index.

    This helper may be used to define index mappings, where the indexed
    value is always set to a specific constant. Example:

    .. code-block:: python

        mapping = {'field': const('I am a constant')}

    """
    return lambda obj: con


def prepare_connection():
    """Set dafault connection for ElasticSearch.

    .. warning::

        In case of using multiprocessing/multithreading, connection will
        be probably initialized in the main process/thread and the same
        connection (socket) will be used in all processes/threads. This
        will cause some unexpected timeouts of pushes to Elasticsearch.
        So make sure that this function is called again in each
        process/thread to make sure that unique connection will be used.
    """
    elasticsearch_host = getattr(settings, 'ELASTICSEARCH_HOST', 'localhost')  # pylint: disable=invalid-name
    elasticsearch_port = getattr(settings, 'ELASTICSEARCH_PORT', 9200)  # pylint: disable=invalid-name
    connections.create_connection(hosts=['{}:{}'.format(elasticsearch_host, elasticsearch_port)])
