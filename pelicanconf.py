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
    'ipynb.liquid',
    'liquid_tags.video',
    'liquid_tags.img',
    'liquid_tags.literal',
    'liquid_tags.include_code',
]

IGNORE_FILES = ['.ipynb_checkpoints']


FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = './theme/'

ABOUT_PAGE = '/pages/about.html'
IMPRESSUM = '/pages/Impressum.html'
LICENSE = '/pages/license.html'
TWITTER_USERNAME = 'berendkapelle'
GITHUB_USERNAME = 'berend'
AUTHOR_BLOG = 'http://berend.github.io'
RELATIVE_URLS = True
ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'resources', 'favicon.ico', 'android-icon-144x144.png',
                'android-icon-192x192.png', 'android-icon-36x36.png', 'android-icon-48x48.png',
                'android-icon-72x72.png', 'android-icon-96x96.png', 'apple-icon-114x114.png',
                'apple-icon-120x120.png', 'apple-icon-144x144.png', 'apple-icon-152x152.png',
                'apple-icon-180x180.png', 'apple-icon-57x57.png', 'apple-icon-60x60.png',
                'apple-icon-72x72.png', 'apple-icon-76x76.png', 'apple-icon-precomposed.png',
                'apple-icon.png', 'browserconfig.xml', 'favicon-16x16.png', 'favicon-32x32.png',
                'favicon-96x96.png', 'manifest.json', 'ms-icon-144x144.png',
                'ms-icon-150x150.png', 'ms-icon-310x310.png', 'ms-icon-70x70.png']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'codehilite'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

ENABLE_MATHJAX = True
SHOW_FEED = True

GOOGLE_ANALYTICS = "UA-112772612-1"
GOOGLE_ANALYTICS_DOMAIN = "https://berend.github.io"
