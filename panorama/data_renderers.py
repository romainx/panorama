# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nvd3 import discreteBarChart

class DataRenderer(object):

	def __init__(self, producer):
	    self.producer = producer

	def render_nb_article_by_year(self):
		#Open File for test
		output_file = open('test_output/test_discreteBarChart.html', 'w')

		chart = discreteBarChart(name='discreteBarChart', height=400, width=400)
		chart.assets_directory = "./theme/bower_components/"
		# sorting data by date ascending
		xdata = sorted(self.producer.nb_article_by_year.keys())
		ydata = [] 
		# maybe there is a smarter way to do that ?
		for x in xdata:
			ydata.append(self.producer.nb_article_by_year.get(x))
		
		chart.add_serie(y=ydata, x=xdata)
		chart.buildhtml()
		
		output_file.write(chart.htmlcontent)

		#close Html file
		output_file.close()

	def render_all(self):
		self.render_nb_article_by_year()