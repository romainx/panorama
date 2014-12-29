'''
panorama
===================================

This plugin generates statistics from posts
'''

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from conf_factory import ConfFactory

logger = logging.getLogger(__name__)

from pelican import signals


def generate_all(generator):
    logger.info('panorama generation started')

    # initializing the conf factory
    conf_factory = ConfFactory()
    conf_factory.configure()

    # initializing the data factory
    data_factory = conf_factory.data_factory
    data_factory.parse_data(generator.articles)
    # initializing the chart factory
    chart_factory = conf_factory.chart_factory
    # initializing the results
    charts = {}
    # iterating over the confs to produce data and render the charts
    for conf_id, conf in conf_factory.confs.iteritems():
        series = data_factory.produce(producer=conf['producer'])
        chart = chart_factory.render(series=series, renderer=conf['renderer'])
        charts[chart.name] = chart
    # setting results in the context
    generator.context['panorama_charts'] = charts

    logger.info('panorama generation ended')
    # link for conf file http://stackoverflow.com/questions/5055042/whats-the-best-practice-using-a-settings-file-in-python


def register():
    signals.article_generator_finalized.connect(generate_all)