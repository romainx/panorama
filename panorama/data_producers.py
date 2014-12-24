# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import defaultdict


class DataProducer(object):
    def __init__(self, generator):
        self.generator = generator

    def compute(self, configurators):
        for article in self.generator.articles:
            for configurator in configurators:
                data_processor = configurator.processor
                data_processor.process(article)
                configurator.stats.data = data_processor.data

        return configurators


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