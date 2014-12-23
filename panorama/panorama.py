'''
panorama
===================================

This plugin generates statistics from posts
'''

from collections import defaultdict
from pelican import signals

def generate_all(generator):
   data_generator = DataGenerator(generator)
   # generating data
   data_generator.generate_all()

def register():
    signals.article_generator_finalized.connect(generate_all)