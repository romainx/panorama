# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nvd3 import multiBarChart, stackedAreaChart
from pandas import Series

DEFAULT_CONF = {
    'DEFAULT': {'name': None, 'display_container': False, 'height': 300, 'width': 600, 'color_category': 'category20'},
    stackedAreaChart: {'use_interactive_guideline': True, 'x_axis_format': ''},
    multiBarChart: {'x_axis_format': ''}
}
class ChartFactory(object):
    def __init__(self):
        # TODO extra series conf ?
        self.extra_series = {'tooltip': {'y_start': '', 'y_end': ' posts'}}


    def render(self, data, renderer):
        chart = renderer()
        if isinstance(data, Series):
            self.add_series(series=data, chart=chart)
        elif isinstance(data, list):
            for series in data:
                self.add_series(series=series, chart=chart)
        chart.buildcontent()
        return chart

    def add_series(self, series, chart):
        chart.add_serie(name=series.name, y=series.tolist(), x=series.index.get_values(), extra=self.extra_series)


def create_chart(chart, name):
    # Initializing with default values
    conf = DEFAULT_CONF['DEFAULT'].copy()
    if chart in DEFAULT_CONF:
        # Overwriting with specific chart values if defined
        conf.update(DEFAULT_CONF[chart])
    # Setting the chart name
    conf['name'] = name
    # Passing the dictionary as keywords
    return chart(**conf)