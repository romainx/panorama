# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io

from nvd3 import discreteBarChart

class DataRenderer(object):

	def __init__(self, producer):
	    self.producer = producer
	    self.charts =  {}

	def build_nb_article_by_year(self):
		chart = discreteBarChart(name='discreteBarChart', display_container=False, height=400, width=400)
		# sorting data by date ascending
		xdata = sorted(self.producer.data["nb_article_by_year"].keys())
		ydata = [] 
		# maybe there is a smarter way to do that ?
		for x in xdata:
			ydata.append(self.producer.data["nb_article_by_year"].get(x))
		
		chart.add_serie(y=ydata, x=xdata)
		# building chart + container
		chart.buildcontent()
		self.charts["nb_article_by_year"] = chart

	def render_all(self):
		self.build_nb_article_by_year()