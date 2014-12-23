# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io

import panorama

from pelican.generators import (Generator, ArticlesGenerator)

from pelican.tests.support import unittest, get_settings
from jinja2 import Environment, PackageLoader

from data_producers import DataProducer
from data_renderers import DataRenderer

CUR_DIR = os.path.dirname(__file__)
CONTENT_DIR = os.path.join(CUR_DIR, 'test_data')
TEST_DIR = os.path.join(CUR_DIR, 'test_output')
TEST_PAGE_TEMPLATE = "./test_page.html"

class TestGenerator(unittest.TestCase):

	def setUp(self):
		self.settings = get_settings(filenames={})
		self.settings['CACHE_CONTENT'] = False   # cache not needed for this logic tests
		self.generator = ArticlesGenerator(
		    context=self.settings.copy(), settings=self.settings,
		    path=CONTENT_DIR, theme=self.settings['THEME'], output_path=None)
		# registering plugin
		panorama.register()
		# generating data from file
		self.generator.generate_context()

		# preparing template rendering for test page generation
		pl = PackageLoader('panorama', 'template')
		jinja2_env = Environment(lstrip_blocks=True, trim_blocks=True, loader=pl)
		self.template_test_page = jinja2_env.get_template(TEST_PAGE_TEMPLATE)

	def test_compute_nb_article_by_year(self):
		result_expected = {2007: 1, 2008: 2, 2014: 7}
		self.assertEqual(result_expected, self.generator.context["panorama_data"]["nb_article_by_year"])

	def test_render_all(self):
		with io.open(os.path.join(TEST_DIR, "all_charts.html"), "w") as output_file:
				output_file.write(self.template_test_page.render(charts=self.generator.context['panorama_charts']))

if __name__ == '__main__':
	unittest.main()