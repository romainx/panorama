# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pandas import DataFrame, Series, read_pickle


class DataFactory(object):
    """ Responsible to produce data ready to be rendered.
    """

    def __init__(self, metadata_columns, tag_columns):
        """ Store the definition of data (the columns).

        :param metadata_columns: the columns to extract.
        :param tag_columns: the tags that will become columns.
        """
        self.data = None
        self.metadata_columns = metadata_columns
        self.tag_columns = tag_columns

    def load_data(self, path):
        """ Used, for test purpose, to load data from a pickle file.

        :param path: the path of the file.
        """
        self.data = read_pickle(path)

    def save_data(self, path):
        """ Used, for test purpose, to save data to a pickle file.

        :param path: the path of the file.
        """
        self.data.to_pickle(path)

    def parse_data(self, articles):
        """ Responsible to parse articles in order to extract data.
        Data is extracted as a DataFrame containing the following columns:
        - Article metadata
        - Article tags
        Data is indexed by a generated ID (integer).

        :param articles: The articles to parse.
        """
        # initializing the DataFrame with all columns
        self.data = DataFrame(columns=self.metadata_columns + self.tag_columns)
        # extracting only required metadata from articles
        x = 0
        for article in articles:
            # Selecting metadata
            metadata_series = Series(
                dict([(i, article.metadata[i]) for i in self.metadata_columns if i in article.metadata]),
                self.metadata_columns)
            # Selecting tags
            tags_series = Series([tag.name for tag in article.tags[:len(self.tag_columns)]], self.tag_columns)
            # Merging metadata and tags and adding them to the dataframe
            self.data.loc[x] = metadata_series.append(tags_series)
            x += 1

    def produce(self, producer):
        """ Call the producer method by passing it the data and simply returns the result.
        Producer methods are intended to return:
        - a Series
        - a dict of Series

        :param producer: the producer method to call.
        :return: the
        """
        return producer(data=self.data)


def count_article_by_column(data, column):
    """ Count the number of articles in data grouped by the specified column.

    :param data: the DataFrame containing articles
    :param column: the column used to group data
    :return: a Series containing the number of articles indexed by column
    """
    return count_article(data.groupby(column))


def count_article_by_year(data):
    """ Count the number of articles in data grouped by year.

    :param data: the DataFrame containing articles
    :return: a Series containing the number of articles indexed by year
    """
    return count_article(data.groupby(lambda x: data['date'][x].year))


def count_article(data):
    """ Count the number of articles in data.

    :param data: the DataFrame containing articles
    :return: a Series containing the number of articles
    """
    return data['title'].count()


def count_article_by_column_by_year(data, column):
    """ Count the number of articles grouped by the specified column over the years.

    :param data: the DataFrame containing articles
    :param column: the column used to group data
    :return: a dict of Series
    """
    # TODO maybe there is a better way to do that, but it works ;-)
    # Computing a range of year to reindex series and filling the gaps
    y_range = range(min(data['date']).year, max(data['date']).year + 1)
    result = []
    # Grouping data by column
    groups = data.groupby([column])
    for group_name, group in groups:
        # Counting by year for each group
        series = count_article_by_year(group)
        series.name = group_name
        # Indexing data to obtain the full year range
        series = series.reindex(y_range)
        # Filling missing values
        series = series.fillna(0)
        result.append(series)
    return result