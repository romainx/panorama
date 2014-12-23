# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

import panorama

from pelican.generators import (Generator, ArticlesGenerator)

from pelican.tests.support import unittest, get_settings

from data_producers import DataProducer
from data_renderers import DataRenderer

CUR_DIR = os.path.dirname(__file__)
CONTENT_DIR = os.path.join(CUR_DIR, 'test_data')

class TestGenerator(unittest.TestCase):

	def setUp(self):
		self.settings = get_settings(filenames={})
		self.settings['CACHE_CONTENT'] = False   # cache not needed for this logic tests
		self.generator = ArticlesGenerator(
		    context=self.settings.copy(), settings=self.settings,
		    path=CONTENT_DIR, theme=self.settings['THEME'], output_path=None)
		# generating data from file
		self.generator.generate_context()
		# initializing the data generator
		self.data_producer = DataProducer(self.generator)
		# producing data
		self.data_producer.compute_all()
		# initializing the renderer
		self.data_renderer = DataRenderer(self.data_producer)

	def test_compute_nb_article_by_year(self):
		result_expected = {2007: 1, 2008: 2, 2014: 7}
		self.assertEqual(result_expected, self.data_producer.nb_article_by_year)

	def test_render_nb_article_by_year(self):
		self.data_renderer.render_nb_article_by_year()

if __name__ == '__main__':
	unittest.main()