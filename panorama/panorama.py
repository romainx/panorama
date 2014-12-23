'''
panorama
===================================

This plugin generates statistics from posts
'''

from __future__ import unicode_literals

from data_producers import DataProducer
from data_renderers import DataRenderer

import logging
logger = logging.getLogger(__name__)

from pelican import signals

def generate_all(generator):
   logger.info("panorama generation started")
   # generating data
   data_producer = DataProducer(generator)
   data_producer.compute_all()
   # rendering data
   data_renderer = DataRenderer(data_producer)
   data_renderer.render_all()
   # putting data & charts in context
   generator.context['panorama_data'] = data_producer.data
   generator.context['panorama_charts'] = data_renderer.charts
   logger.info("panorama generation ended")

def register():
    signals.article_generator_finalized.connect(generate_all)