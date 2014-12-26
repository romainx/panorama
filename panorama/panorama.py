'''
panorama
===================================

This plugin generates statistics from posts
'''

from __future__ import unicode_literals

import logging

from data_statistics import DataConfigurator


logger = logging.getLogger(__name__)

from pelican import signals


def generate_all(generator):
    logger.info('panorama generation started')
    # getting the configuration
    data_configurator = DataConfigurator()
    # configuring the generation
    data_configurator.configure()
    # generating data
    data_configurator.process(generator.articles)
    # setting data in the Pelican context
    generator.context['panorama_data'] = data_configurator.get_result()
    logger.info('panorama generation ended')


def register():
    signals.article_generator_finalized.connect(generate_all)