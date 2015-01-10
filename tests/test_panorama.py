# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from functools import partial
import os
import io
import sys

from pandas.util.testing import assert_series_equal
from pelican.generators import (ArticlesGenerator)
from pelican.tests.support import unittest, get_settings
from jinja2 import Environment, PackageLoader
from pandas import Series

from panorama import panorama
from panorama.chart_factory import ChartFactory, create_data_renderer
from panorama.conf_factory import ConfFactory
from panorama.data_factory import count_article_by_column_by_year, count_article_by_column, count_article_by_year, \
    top_article


CUR_DIR = os.path.dirname(__file__)

TEST_DATA = os.path.join(CUR_DIR, 'test_data')
CONTENT_DIR = os.path.join(TEST_DATA, 'md')
TEST_DIR = os.path.join(CUR_DIR, 'test_output')
TEST_PAGE_TEMPLATE = 'test_page.html'

TEST_DATA_FILE = os.path.join(TEST_DATA, 'p/article_data.p')

CONF_FILE = os.path.join(CUR_DIR, 'panorama.yml')

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


# TODO fix pickle to be usable in Python 2 & 3
@unittest.skipIf(sys.version_info > (3, 0),
                 "Not supported in Python 3.x due to test data decoding (pickle)")
class TestData(unittest.TestCase):
    def setUp(self):
        # Initializing the conf factory
        self.conf_factory = ConfFactory()
        self.conf_factory.configure(CONF_FILE)
        # Initializing the data factory
        self.data_factory = self.conf_factory.data_factory
        self.data_factory.load_data(TEST_DATA_FILE)

    def test_count_article_by_column_by_year(self):
        self.assertEqual(len(count_article_by_column_by_year(self.data_factory.data, 'genre')), 5)

    def test_count_article_by_column(self):
        expected_result = Series({'BD': 4, 'Divers': 1, 'Jeunesse': 1, 'Roman': 3, 'Roman Noir': 1})
        assert_series_equal(count_article_by_column(self.data_factory.data, 'genre'), expected_result)

    def test_count_article_by_year(self):
        expected_result = Series({2007: 1, 2008: 2, 2014: 7})
        assert_series_equal(count_article_by_year(self.data_factory.data), expected_result)

    def test_top_article(self):
        expected_result = Series({'Gallimard': 3})
        assert_series_equal(top_article(self.data_factory.data, 'publisher', 1), expected_result)


class TestChart(unittest.TestCase):
    def setUp(self):
        self.chart_factory = ChartFactory()

    def test_render(self):
        expected_chart_name = "test_chart"
        renderer = partial(create_data_renderer, class_name='discreteBarChart', name=expected_chart_name)
        data = Series({'BD': 4, 'Divers': 1, 'Jeunesse': 1, 'Roman': 3, 'Roman Noir': 1})
        chart = self.chart_factory.render(data=data, renderer=renderer)
        self.assertEqual(chart.name, expected_chart_name)
        self.assertIsNotNone(chart.htmlcontent)
        self.assertIsNotNone(chart.container)


class TestConf(unittest.TestCase):
    def setUp(self):
        self.conf_factory = ConfFactory()
        self.conf_factory.configure(CONF_FILE)

    def test_load_conf(self):
        pass
