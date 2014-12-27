# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io

from pelican.generators import (ArticlesGenerator)
from pelican.tests.support import unittest, get_settings
from jinja2 import Environment, PackageLoader

from panorama import panorama


CUR_DIR = os.path.dirname(__file__)
CONTENT_DIR = os.path.join(CUR_DIR, 'test_data')
TEST_DIR = os.path.join(CUR_DIR, 'test_output')
TEST_PAGE_TEMPLATE = 'test_page.html'


class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.settings = get_settings(filenames={})
        self.settings['CACHE_CONTENT'] = False  # cache not needed for this logic tests
        self.generator = ArticlesGenerator(
            context=self.settings.copy(), settings=self.settings,
            path=CONTENT_DIR, theme=self.settings['THEME'], output_path=None)
        # registering plugin
        panorama.register()
        # generating data from file
        self.generator.generate_context()

        # preparing template rendering for test page generation
        pl = PackageLoader('tests', 'template')
        jinja2_env = Environment(lstrip_blocks=True, trim_blocks=True, loader=pl)
        self.template_test_page = jinja2_env.get_template(TEST_PAGE_TEMPLATE)

    def test_compute_all(self):
        result_expected = {'nb_article_by_year': {2007: 1, 2008: 2, 2014: 7},
                           'nb_article_by_genre': {'BD': 4, 'Roman': 3, 'Divers': 1, 'Jeunesse': 1, 'Roman Noir': 1},
                           'nb_article_by_ranking': {'2 étoiles': 1, '4 étoiles': 6, '5 étoiles': 3},
                           'nb_article_by_tag_year': {'BD': {2014: 4},
                                                      'Roman': {2007: 1, 2008: 1, 2014: 1},
                                                      'Divers': {2014: 1},
                                                      'Jeunesse': {2014: 1},
                                                      'Roman Noir': {2008: 1}
                           }
        }
        for stat_id, stat in self.generator.context['panorama_data'].iteritems():
            self.assertEqual(result_expected[stat_id], stat.data)

    def test_render_all(self):
        with io.open(os.path.join(TEST_DIR, 'all_charts.html'), 'w', encoding='utf8') as output_file:
            output_file.write(self.template_test_page.render(panorama_data=self.generator.context['panorama_data']))