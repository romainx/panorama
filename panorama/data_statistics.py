# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from data_producers import (ArticleByYear, ArticleByTag, DataProducer)
from data_renderers import (DiscreteBarChartRenderer, PieChartRenderer, DataRenderer)


class DataStats(object):
    """Data object containing metadata, data and the chart"""

    def __init__(self, name):
        self.name = name
        self.description = None
        self.data = None
        self.chart = None


class DataConfiguration(object):
    """ A configuration unit holding a renderer, a processor and the result """
    def __init__(self, stats, processor, renderer):
        # the data object containing the result after the processing
        self.stats = stats
        self.processor = processor
        self.renderer = renderer


class DataConfigurator(object):
    """ A data manager able to generate output data from articles """
    def __init__(self):
        self.configurations = {}

    def configure(self):

        # configuration of the number of article by year
        configuration_id = 'nb_article_by_year'
        data = DataStats(name='Nombre d\'articles par année')
        conf = DataConfiguration(data, ArticleByYear(), DiscreteBarChartRenderer(configuration_id))
        self.configurations[configuration_id] = conf

        # configuration of the number of article by 1st tag (genre for my case)
        configuration_id = 'nb_article_by_genre'
        data = DataStats(name='Distribution par genre')
        conf = DataConfiguration(data, ArticleByTag(0), PieChartRenderer(configuration_id))
        self.configurations[configuration_id] = conf

        # configuration of the number of article by 2nd tag (ranking for my case)
        configuration_id = 'nb_article_by_ranking'
        data = DataStats(name='Distribution du classement')
        conf = DataConfiguration(data, ArticleByTag(1), DiscreteBarChartRenderer(configuration_id))
        self.configurations[configuration_id] = conf

    def process(self, articles):
        # generating data
        self.configurations = DataProducer.compute(configurations=self.configurations, articles=articles)
        # rendering data
        self.configurations = DataRenderer.render(configurations=self.configurations)

    def get_result(self):
        # getting the output list
        # TODO(romainx): can be done in a better way
        data = {}
        for configuration_id, configuration in self.configurations.iteritems():
            data[configuration_id] = configuration.stats
        return data