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


class ArticleByTagAndYear(ArticleByTag):
    """ Produce {tag1:{year1:nb_article,year2:nb_article},
    tag2:{year1:nb_article,year2:nb_article}}
    """

    def __init__(self, tag_position):
        super(ArticleByTagAndYear, self).__init__(tag_position)
        self.data = dict()

    def process(self, article):
        if article.tags[self.tag_position].name not in self.data.keys():
            # there is no entry for this tag, initializing a new defaultdict to store the tuple date:nb_article
            self.data[article.tags[self.tag_position].name] = defaultdict(int)
        self.data[article.tags[self.tag_position].name][article.date.year] += 1