# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from functools import partial

from nvd3 import discreteBarChart, pieChart, stackedAreaChart

from chart_factory import create_chart, ChartFactory
from data_factory import count_article_by_column, DataFactory, count_article_by_year, count_article_by_column_by_year


class ConfFactory(object):
    def __init__(self):
        self.confs = {}
        self.data_factory = None
        self.chart_factory = None

    def append_conf(self, chart_id, producer, renderer):
        self.confs[chart_id] = {'producer': producer, 'renderer': renderer}

    def configure(self):
        # configuring factories
        self.data_factory = DataFactory(metadata_columns=['title', 'date', 'category'],
                                        tag_columns=['genre', 'ranking'])
        self.chart_factory = ChartFactory()

        # articles by ranking
        chart_id = 'nb_article_by_ranking'
        producer = partial(count_article_by_column, column='ranking')
        renderer = partial(create_chart, chart=discreteBarChart, name=chart_id)
        self.append_conf(chart_id=chart_id, producer=producer, renderer=renderer)

        # articles by genre
        chart_id = 'nb_article_by_genre'
        producer = partial(count_article_by_column, column='genre')
        renderer = partial(create_chart, chart=pieChart, name=chart_id)
        self.append_conf(chart_id=chart_id, producer=producer, renderer=renderer)

        # articles by year
        chart_id = 'nb_article_by_year'
        producer = partial(count_article_by_year)
        renderer = partial(create_chart, chart=discreteBarChart, name=chart_id)
        self.append_conf(chart_id=chart_id, producer=producer, renderer=renderer)

        # articles by genre and year
        chart_id = 'nb_article_by_genre_year'
        producer = partial(count_article_by_column_by_year, column='genre')
        renderer = partial(create_chart, chart=stackedAreaChart, name=chart_id)
        self.append_conf(chart_id=chart_id, producer=producer, renderer=renderer)