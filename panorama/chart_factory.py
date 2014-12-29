# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class ChartFactory(object):
    def __init__(self):
        pass

    def render(self, series, renderer):
        # TODO extra series conf ?
        extra_series = {'tooltip': {'y_start': '', 'y_end': ' posts'}}
        chart = renderer()
        chart.add_serie(y=series.tolist(), x=series.index.get_values(), extra=extra_series)
        chart.buildcontent()
        return chart


def create_chart(chart, name):
    return chart(name=name, display_container=False, height=300,
                 width=600)