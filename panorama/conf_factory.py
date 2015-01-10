# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from functools import partial

import yaml

# import * are necessary since functions will be dynamically called
from .chart_factory import *
from .data_factory import *
from nvd3 import *


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

    def configure(self, yaml_file):
        """
        Configure all the rendering to perform.
        The confs dict is populated with created configurations.

        :param yaml_file: the configuration file to use
        """
        with open(yaml_file, 'r') as f:
            panorama_conf = yaml.load(f)

        # Configuring factories to:
        # - get only title, date and category from article metadata
        # - rename the first 4 tags with the names defined below

        self.data_factory = DataFactory(metadata_columns=panorama_conf['metadata_columns'],
                                        tag_columns=panorama_conf['tag_columns'])
        self.chart_factory = ChartFactory()

        # Creating the configurations
        for yaml_conf in panorama_conf['confs']:
            chart_id = yaml_conf['chart_id']
            producer = create_producer(yaml_conf['producer'])
            renderer = create_renderer(yaml_conf['renderer'], chart_id)
            self.append_conf(chart_id=chart_id, producer=producer, renderer=renderer)


def create_producer(yaml_producer):
    """
    Create a producer from a piece of yaml configuration.

    :param yaml_producer: the producer part of the configuration loaded from the yaml file
    :return: the producer function
    """
    if 'args' in yaml_producer:
        return partial(eval(yaml_producer['function']), **yaml_producer['args'])
    else:
        return partial(eval(yaml_producer['function']))


def create_renderer(yaml_renderer, name):
    """
    Create a renderer from a piece of yaml configuration.

    :param yaml_renderer: the renderer part of the configuration loaded from the yaml file
    :param name: the name of the renderer
    :return: the renderer function
    """
    return partial(create_chart, chart=eval(yaml_renderer['chart']), name=name)