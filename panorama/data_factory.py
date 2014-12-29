# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pandas import DataFrame, Series, read_pickle


class DataFactory(object):
    """Responsible to produce data ready to be rendered.
    """

    def __init__(self, metadata_columns, tag_columns):
        """

        :param metadata_columns: the columns to extract
        :param tag_columns: the tags that will become columns
        """
        self.data = None
        self.metadata_columns = metadata_columns
        self.tag_columns = tag_columns

    def load_data(self, path):
        self.data = read_pickle(path)

    def parse_data(self, articles):
        # initializing dataframe with all columns
        self.data = DataFrame(columns=self.metadata_columns + self.tag_columns)
        # extracting only required metadata from articles
        x = 0
        for article in articles:
            # selecting metadata
            metadata_series = Series(
                dict([(i, article.metadata[i]) for i in self.metadata_columns if i in article.metadata]),
                self.metadata_columns)
            # selecting tags
            tags_series = Series([tag.name for tag in article.tags[:len(self.tag_columns)]], self.tag_columns)
            # merging metadata and tags and adding them to the dataframe
            self.data.loc[x] = metadata_series.append(tags_series)
            x += 1
            # self.data.save('article_data.tst')

    def produce(self, producer):
        return producer(data=self.data)


def count_article_by_column(data, column):
    return data.groupby(column)['title'].count()


def count_article_by_date(data):
    return data.groupby(lambda x: data['date'][x].year)['title'].count()
