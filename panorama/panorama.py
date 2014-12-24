'''
panorama
===================================

This plugin generates statistics from posts
'''

from __future__ import unicode_literals

import logging

from data_producers import DataProducer
from data_renderers import DataRenderer
from data_statistics import DataConfiguratorFactory


logger = logging.getLogger(__name__)

from pelican import signals


def generate_all(generator):
    logger.info("panorama generation started")
    # getting the configuration
    data_configurators = DataConfiguratorFactory().configure()
    # generating data
    data_producer = DataProducer(generator)
    data_producer.compute(data_configurators)
    # rendering data
    data_renderer = DataRenderer()
    data_renderer.render(data_configurators)
    # putting data & charts in context
    # getting the output list
    # TODO(romainx): can be done in a better way
    data = []
    for data_configurator in data_configurators:
        data.append(data_configurator.stats)

    generator.context['panorama_data'] = data
    logger.info("panorama generation ended")


def register():
    signals.article_generator_finalized.connect(generate_all)