# TODO

- [x] License definition with [choose a license](http://choosealicense.com) ?
- [x] Use Pelican mock objects for test data
- [x] Define the design of the `DataProducer` and the `DataRenderer`
- [x] Create [unit tests](http://pytest.org/latest/)
- [x] Create a demo page

- [ ] Code improvements
	- [x] Improve the data structure cf. [Goodreads Activity](https://github.com/getpelican/pelican-plugins/tree/master/goodreads_activity) 
	- [x] Make things configurable i.e. map between producers and renderers
	- [ ] Externalize configuration
	- [x] Finish test cases
	- [ ] Build more charts
- [x] Write the installation doc
- [ ] Deployment tests [Tox](http://tox.readthedocs.org/en/latest/)
- [ ] Check [cookiecutter](https://github.com/audreyr/cookiecutter)
- [ ] Generate the documentation using [Sphinx](http://sphinx-doc.org)
- [ ] Publish the documentation on [Read the Docs](https://readthedocs.org/)
- [x] Deploy on [Travis](https://travis-ci.org/) CI platform
- [x] Measure code coverage with [Coveralls](https://coveralls.io)
- [ ] Use Code linters
	- [ ] jcrocholl/pep8
	- [ ] pre-commit/pre-commit
- [ ] Make a pull request to integrate it in the [Pelican Plugins](https://github.com/getpelican/pelican-plugins)
- [ ] Publish on [PyPI](https://pypi.python.org) ?
	- Use a realease [checklist](https://gist.github.com/audreyr/5990987)

# Notes

Group by syntax:

```python
df.groupby([pd.Grouper(freq='1M',key='Date'),'Buyer']).sum()
df.groupby(['b', 'c'])['a'].transform('count')
```