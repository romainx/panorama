# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nvd3.discreteBarChart import discreteBarChart
from nvd3.pieChart import pieChart


class DataRenderer(object):
    def render(self, configurators):
        for configurator in configurators:
            data_renderer = configurator.renderer
            configurator.stats.chart = data_renderer.render(configurator.stats.data)
        return configurators


class ChartRenderer(object):
    def __init__(self):
        self.display_container = False
        self.height = 300
        self.width = 600

    def render(self, data):
        # sorting data by ascending
        xdata = sorted(data.keys())
        ydata = []
        extra_serie = {"tooltip": {"y_start": "", "y_end": " posts"}}
        # TODO(romainx): maybe there is a smarter way to do that ?
        for x in xdata:
            ydata.append(data.get(x))
        self.chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
        self.build()
        return self.chart

    def build(self):
        # building chart + container
        self.chart.buildcontent()


class DiscreteBarChartRenderer(ChartRenderer):
    def __init__(self, name):
        super(DiscreteBarChartRenderer, self).__init__()
        self.chart = discreteBarChart(name=name, display_container=self.display_container, height=self.height,
                                      width=self.width)


class PieChartRenderer(ChartRenderer):
    def __init__(self, name):
        super(PieChartRenderer, self).__init__()
        self.chart = pieChart(name=name, display_container=self.display_container, height=self.height, width=self.width)