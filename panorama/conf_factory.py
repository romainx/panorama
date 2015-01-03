# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from functools import partial

from nvd3 import discreteBarChart, pieChart, stackedAreaChart, multiBarChart

from chart_factory import create_chart, ChartFactory
from data_factory import count_article_by_column, DataFactory, count_article_by_year, count_article_by_column_by_year


class ConfFactory(object):
    def __init__(self):
        self.confs = {}
        self.data_factory = None
        self.chart_factory = None

    def append_conf(self, chart_id, producer, renderer):
        """
        Add a a new entry in the confs dict.

        :param chart_id: the id of the chart that will be used to identify it.
        :param producer: a data producer, a function returning a Series or a dict of Series.
        :param renderer: a data render, a function returning a Chart.
        """
        self.confs[chart_id] = {'producer': producer, 'renderer': renderer}

    def configure(self):
        """
        Configure all the rendering to perform.
        The confs dict is populated with created configurations.

        """
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

        # articles by genre and year as a multi bar chart
        chart_id = 'nb_article_by_genre_year'
        producer = partial(count_article_by_column_by_year, column='genre')
        renderer = partial(create_chart, chart=multiBarChart, name=chart_id)
        self.append_conf(chart_id=chart_id, producer=producer, renderer=renderer)

        # articles by genre and year as a stacked area chart
        chart_id = 'nb_article_by_ranking_year'
        producer = partial(count_article_by_column_by_year, column='ranking')
        renderer = partial(create_chart, chart=stackedAreaChart, name=chart_id)
        self.append_conf(chart_id=chart_id, producer=producer, renderer=renderer)