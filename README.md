# Panorama - a statistics plugin for Pelican

## Overview

**Panorama** is a [Pelican](https://github.com/getpelican/pelican) plugin to generate statistics from blog posts (number of posts per month, categories and so on) display them as beautiful charts.

## Functional overview

Produce statistics based on posts metadata and display them by using several charts.
A set of data can only be displayed by a defined set of renderers.
The mapping between data and renderers is done by configuration.

Metadata data used:

	Title: My super title
	Date: 2010-12-03 10:20
	Category: Python
	Tags: pelican, publishing

### Posts per year

- **Description**: Display the number of posts per year.
- **Data**: A dictionary with dates as keys and the number of posts as values. 
- **Renderers**:
	- Bar Chart
	- Line Chart

### Posts per category

- **Description**: Display the number of posts per category.
- **Data**: A dictionary with categories as keys and the number of posts as values.
- **Renderers**:
	- Pie chart
	- Bar Chart

## Technical overview

This plugin uses:

- The Pelican [plugins feature](http://docs.getpelican.com/en/latest/plugins.html).
- The [Python Wrapper for NVD3](https://github.com/areski/python-nvd3).

### Design

Some design elements:

- The plugin mechanisms using [blinker](https://pypi.python.org/pypi/blinker). The signal to listen to is `article_generator_finalized`.
- A `DataProducer` using metadata to produce statistical data. Several `DataProducer` are available one for each data type.
- A `DataRenderer` using statistical data to render charts. Several `DataProducer` are available one for each rendering (chart). Each produces a `js` script stored in the Pelican output directory.
- A `ConfigurationManager` to map `DataProducer` to `DataRenderer`.

Generated charts (`js` scripts) can be used by any [Jinja](http://jinja.pocoo.org/) Pelican template to be integrated in the blog (in a dedicated `stats.html` template for example).

### Deployment

The [D3.js](http://d3js.org/) dependencies are deployed here:

	themes/<your_theme>/static/d3js/
	
The scripts are generated here

	output/panorama/

## Installation

A good [example](http://moparx.com/2014/04/adding-search-capabilities-within-your-pelican-powered-site-using-tipue-search/).

Download the following files from [NVD3](http://nvd3.org):

- `nv.d3.min.js`
- `nv.d3.css`

Download the following file from [D3JS](http://d3js.org)

- `d3.zip`

Put them in this folder `themes/<your_theme>/static/panorama/` as described below

```bash
	|- d3
	|   |-- d3.js
	|   |-- d3.min.js
	|   |-- LICENSE
	|- nvd3
	|   |-- nv.d3.min.js
	|   |-- src	
	|       |-- nv.d3.css
```

## Project Layout

- A `docs` directory containing project documentation.
- A directory named with the project's name which stores the actual Python package
- A `test` directory located in the package directory containing test code and resources

```bash
	|- LICENSE
	|- README.md
	|- TODO.md
	|- docs
	|   |-- conf.py
	|   |-- generated
	|   |-- index.rst
	|   |-- installation.rst
	|   |-- quickstart.rst
	|   |-- panorama.rst
	|   |-- history.rst
	|- panorama
	|   |-- __init__.py
	|   |-- panorama.py
	|   |-- test	
	|       |-- test_module.py
	|- requirements.txt
	|- setup.py
```

## Development environment installation

### Installing `virtualenv`

```bash
$ pip install virtualenv
```

Configure the `.bashrc` file

```bash
# pip should only run if there is a virtualenv currently activated
export PIP_REQUIRE_VIRTUALENV=true
# cache pip-installed packages to avoid re-downloading
export PIP_DOWNLOAD_CACHE=$HOME/.pip/cachecontent/*
```

Source the file

```bash
$ source .bashrc
```

### Creating and activating the virtual environment

```bash
$ mkdir virtualenvs
$ cd virtualenvs
$ virtualenv v_panorama
```

Activate the environment

```bash
$ source $HOME/virtualenvs/v_panorama/bin/activate
```

### Install the requirements

Go to the Git folder and install the requirements.

```bash
$ pip install -r requirements.txt
```

## Workflow

GitHub's "Issues" are used for the following:

- bug tracking
- feature requests
- planned features
- release/version management