#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dai Yu'
SITENAME = "Dai's Blog"
SITETITLE = "Dai Yu"
SITESUBTITLE = "Thinking Out Loud"
SITEURL = "https://lfeyao.github.io"

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll


# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/daiyu'),
    ('facebook', 'https://www.facebook.com/dai.dan.yu'),
    ('plane', 'http://www.dai-yu.com'),
)

DEFAULT_PAGINATION = 10

THEME = "/Users/daiyu/pelican-themes/Flex"

PLUGIN_PATHS = '/Users/daiyu/pelican-plugins'
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
