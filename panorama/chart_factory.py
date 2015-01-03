# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pandas import Series


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
    return chart(name=name, display_container=False, height=300,
                 width=600, use_interactive_guideline=True)