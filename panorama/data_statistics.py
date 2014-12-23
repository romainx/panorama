# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io

from data_producers import ArticleByYear
from data_renderers import DiscreteBarChartRenderer

class DataStats(object):

	def __init__(self, id, name):
	    self.id = id
	    self.name =  name

class DataConfigurator(object):

	def __init__(self, stats, processor, renderer):
		self.stats = stats
		self.processor = processor
		self.renderer = renderer

class DataConfiguratorFactory(object):
	
	def __init__(self):
		self.configurators = []

	def configure(self):
		# configuration of the number of article by year
		data = DataStats("nb_article_by_year", "Nombre d'articles par année")
		conf = DataConfigurator(data, ArticleByYear(), DiscreteBarChartRenderer())
		self.configurators.append(conf)
		return self.configurators