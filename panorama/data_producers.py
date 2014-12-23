# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pelican.generators import (Generator, ArticlesGenerator)
from collections import defaultdict

class DataProducer(object):

	def __init__(self, generator):
	    self.generator = generator
	    self.data = {}
	
	def compute_nb_article_by_year(self):
	    # By passing int to the class, all empty keys default to zero. 
	    # This allows to do += without setting the key first.
	    self.nb_article_by_year = defaultdict(int)

	    for article in self.generator.dates:
	        self.nb_article_by_year[article.date.year] += 1
		
		self.data["nb_article_by_year"] = self.nb_article_by_year

	def compute_all(self):
		self.compute_nb_article_by_year()