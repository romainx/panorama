# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import defaultdict


class DataProducer(object):
    @staticmethod
    def compute(configurations, articles):
        for article in articles:
            for configuration_id, configuration in configurations.iteritems():
                data_processor = configuration.processor
                data_processor.process(article)
                configuration.stats.data = data_processor.data

        return configurations


class DataProcessor(object):
    def __init__(self):
        # By passing int to the class, all empty keys default to zero.
        # This allows to do += without setting the key first.
        self.data = defaultdict(int)

    def process(self, article):
        return


class ArticleByYear(DataProcessor):
    def process(self, article):
        self.data[article.date.year] += 1


class ArticleByTag(DataProcessor):
    def __init__(self, tag_position):
        super(ArticleByTag, self).__init__()
        self.tag_position = tag_position

    def process(self, article):
        self.data[article.tags[self.tag_position].name] += 1