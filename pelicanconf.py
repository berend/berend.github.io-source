#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Berend Kapelle'
SITENAME = 'Notes for myself and others'
SITESUBTITLE = u'Documenting a developers journey in data science'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'


NOTEBOOK_DIR = 'resources/notebooks'
CODE_DIR = 'resources/code'

MARKUP = ['md']
PLUGIN_PATHS = ['./plugins']
PLUGINS = [
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal',
]

IGNORE_FILES = ['.ipynb_checkpoints']

#will be overwritten in publishconf.py
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


THEME = './theme/'

ABOUT_PAGE = './pages/about.html'
TWITTER_USERNAME = 'berendkapelle'
GITHUB_USERNAME = 'berend'
AUTHOR_BLOG = 'http://berend.github.io'
RELATIVE_URLS = True
ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'resources', 'favicon.ico']

LICENSE_URL = "https://raw.githubusercontent.com/berend/berend.github.io-source/master/LICENSE"
LICENSE = "MIT"


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'codehilite'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

ENABLE_MATHJAX = True