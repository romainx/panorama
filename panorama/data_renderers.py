# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nvd3.discreteBarChart import discreteBarChart
from nvd3.pieChart import pieChart
from nvd3.stackedAreaChart import stackedAreaChart

class DataRenderer(object):
    @staticmethod
    def render(configurations):
        for configuration_id, configuration in configurations.iteritems():
            configuration.stats.chart = configuration.renderer.render(configuration.stats.data)
        return configurations


class SingleChartRenderer(object):
    def __init__(self):
        self.chart = None
        self.display_container = False
        self.height = 300
        self.width = 600

    def render(self, data):
        # sorting data by ascending
        x_data = sorted(data.keys())
        y_data = []
        extra_serie = {'tooltip': {'y_start': '', 'y_end': ' posts'}}
        # TODO(romainx): maybe there is a smarter way to do that ?
        for x in x_data:
            y_data.append(data.get(x))
        self.chart.add_serie(y=y_data, x=x_data, extra=extra_serie)
        self.build()
        return self.chart

    def build(self):
        # building chart + container
        self.chart.buildcontent()


class DiscreteBarChartRenderer(SingleChartRenderer):
    def __init__(self, name):
        super(DiscreteBarChartRenderer, self).__init__()
        self.chart = discreteBarChart(name=name, display_container=self.display_container, height=self.height,
                                      width=self.width)


class PieChartRenderer(SingleChartRenderer):
    def __init__(self, name):
        super(PieChartRenderer, self).__init__()
        self.chart = pieChart(name=name, display_container=self.display_container, height=self.height, width=self.width)


class MultiChartRenderer(SingleChartRenderer):
    def __init__(self):
        super(MultiChartRenderer, self).__init__()
        self.use_interactive_guideline = True

    def render(self, data):
        # TODO(romainx) to be improved
        # Initializing the extra serie
        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " min"}}
        # Creating the x serie
        x_data_set = set()
        for serie_name, serie in data.iteritems():
            x_data_set.update(serie.keys())
        x_data = sorted(list(x_data_set))
        # Creating the series
        for serie_name, serie in data.iteritems():
            y_data = []
            for date in x_data:
                if date not in serie.keys():
                    y_data.append(0)
                else:
                    y_data.append(serie[date])
            self.chart.add_serie(name=serie_name, y=y_data, x=x_data, extra=extra_serie)
        self.build()
        return self.chart


class StackedAreaChartRenderer(MultiChartRenderer):
    def __init__(self, name):
        super(StackedAreaChartRenderer, self).__init__()
        self.chart = stackedAreaChart(name=name, display_container=self.display_container, height=self.height,
                                      width=self.width, use_interactive_guideline=self.use_interactive_guideline,
                                      x_axis_format='')