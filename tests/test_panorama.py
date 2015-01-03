# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io

from pelican.generators import (ArticlesGenerator)
from pelican.tests.support import unittest, get_settings
from jinja2 import Environment, PackageLoader

from panorama import panorama
from panorama.conf_factory import ConfFactory
from panorama.data_factory import count_article_by_column_by_year


CUR_DIR = os.path.dirname(__file__)

TEST_DATA = os.path.join(CUR_DIR, 'test_data')
CONTENT_DIR = os.path.join(TEST_DATA, 'md')
TEST_DIR = os.path.join(CUR_DIR, 'test_output')
TEST_PAGE_TEMPLATE = 'test_page.html'

TEST_DATA_FILE = os.path.join(TEST_DATA, 'p/article_data.p')

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.settings = get_settings(filenames={})
        self.settings['CACHE_CONTENT'] = False  # cache not needed for this logic tests
        self.generator = ArticlesGenerator(
            context=self.settings.copy(), settings=self.settings,
            path=CONTENT_DIR, theme=self.settings['THEME'], output_path=None)
        # Registering plugin
        panorama.register()
        # Generating data from file
        self.generator.generate_context()
        # preparing template rendering for test page generation
        pl = PackageLoader('tests', 'template')
        jinja2_env = Environment(lstrip_blocks=True, trim_blocks=True, loader=pl)
        self.template_test_page = jinja2_env.get_template(TEST_PAGE_TEMPLATE)

    def test_render_all(self):
        with io.open(os.path.join(TEST_DIR, 'all_charts.html'), 'w', encoding='utf8') as output_file:
            output_file.write(self.template_test_page.render(panorama_charts=self.generator.context['panorama_charts']))


class TestData(unittest.TestCase):
    def setUp(self):
        # Initializing the conf factory
        self.conf_factory = ConfFactory()
        self.conf_factory.configure()
        # Initializing the data factory
        self.data_factory = self.conf_factory.data_factory
        self.data_factory.load_data(TEST_DATA_FILE)

    def test_count_article_by_column_by_year(self):
        data = self.data_factory.data
        self.assertEqual(len(count_article_by_column_by_year(data, 'genre')), 5)
