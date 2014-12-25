# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from data_producers import (ArticleByYear, ArticleByTag)
from data_renderers import (DiscreteBarChartRenderer, PieChartRenderer)


class DataStats(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class DataConfigurator(object):
    def __init__(self, stats, processor, renderer):
        self.stats = stats
        self.processor = processor
        self.renderer = renderer


class DataConfiguratorFactory(object):
    def __init__(self):
        self.configurators = []

    def configure(self):
        # configuration of the number of article by year
        data = DataStats(id='nb_article_by_year', name='Nombre d\'articles par année')
        conf = DataConfigurator(data, ArticleByYear(), DiscreteBarChartRenderer(data.id))
        self.configurators.append(conf)

        # configuration of the number of article by 1st tag (genre for my case)
        data = DataStats(id='nb_article_by_genre', name='Distribution par genre')
        conf = DataConfigurator(data, ArticleByTag(0), PieChartRenderer(data.id))
        self.configurators.append(conf)

        # configuration of the number of article by 2nd tag (ranking for my case)
        data = DataStats(id='nb_article_by_ranking', name='Distribution du classement')
        conf = DataConfigurator(data, ArticleByTag(1), DiscreteBarChartRenderer(data.id))
        self.configurators.append(conf)

        return self.configurators