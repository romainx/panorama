# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io

from nvd3 import discreteBarChart

class DataRenderer(object):

	def render(self, configurators):
		for configurator in configurators:
			data_renderer = configurator.renderer		
			configurator.stats.chart = data_renderer.render(configurator.stats.data)
		return configurators


class ChartRenderer(object):
	
	def __init__(self):
		self.display_container=False
		self.height=400
		self.width=600
	
	def render(self, data):
		return

	def build(self):
		# building chart + container
		self.chart.buildcontent()

class DiscreteBarChartRenderer(ChartRenderer):
	
	def __init__(self):
		super(DiscreteBarChartRenderer, self).__init__()
		self.chart = discreteBarChart(name='discreteBarChart', display_container=self.display_container, height=self.height, width=self.width)

	def render(self, data):
		# sorting data by date ascending
		xdata = sorted(data.keys())
		ydata = [] 
		# TODO(romainx): maybe there is a smarter way to do that ?
		for x in xdata:
			ydata.append(data.get(x))
		self.chart.add_serie(y=ydata, x=xdata)
		self.build()
		return self.chart