# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

import six

from .conf_factory import ConfFactory

logger = logging.getLogger(__name__)

from pelican import signals


def generate_all(generator):
    """
    The method that will be called by the Pelican plugin mechanism.

    :param generator: the Pelican generator
    """
    logger.info('panorama generation started')

    # Initializing the conf factory
    conf_factory = ConfFactory()
    conf_factory.configure()

    # Initializing the data factory
    data_factory = conf_factory.data_factory
    data_factory.parse_data(generator.articles)
    # Initializing the chart factory
    chart_factory = conf_factory.chart_factory
    # Initializing the results
    charts = {}
    # Iterating over the confs to produce data and render the charts
    for conf_id, conf in six.iteritems(conf_factory.confs):
        data = data_factory.produce(producer=conf['producer'])
        chart = chart_factory.render(data=data, renderer=conf['renderer'])
        charts[chart.name] = chart
    # Setting results in the context
    # Charts will be accessible in the Pelican context under this name
    generator.context['panorama_charts'] = charts

    logger.info('panorama generation ended')
    # link for conf file http://stackoverflow.com/questions/5055042/whats-the-best-practice-using-a-settings-file-in-python


def register():
    """ Called by the Pelican engine to register the plugin.
    It uses a Blinker (https://pypi.python.org/pypi/blinker) and is registered on the event "article_generator_finalized".
    Raised when the generator has ended the generation of its context.
    """
    signals.article_generator_finalized.connect(generate_all)