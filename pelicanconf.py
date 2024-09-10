# Author Info
AUTHOR = "yusabari"
AUTHOR_INFO = {
    "GITHUB": "yusabari",
    "DESCRIPTION": "Hi<br>"
}
SITENAME = 'yusabari blog'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'ko'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme Settings
THEME = "./themes/twinkle"
THEME_STATIC_DIR = 'theme'

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# JINJA
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.loopcontrols']
}

# PLUGINS
PLUGIN_PATHS = ['./plugins']
PLUGINS = [
    'pelican.plugins.sitemap',
    'representative_image',
    'share_post',
    'neighbors'
]

# PLUGIN - sitemap
SITEMAP = {
    'format': 'xml'
}

# Author Links
LINKS = (
    ("home", "https://yusabari.com", "fontawesome"),
    ("velog", "https://velog.io/@developer_khj", "image"),
    ("github", "https://github.com/yusabari", "image"),
    ("gmail", "mailto:yumesaki.kr@gmail.com", "image")
#    ("twitter", "https://twitter.com/yusabari", "image")
)

# LINKS = (("twitter", "<img src=\"https://upload.wikimedia.org/wikipedia/commons/6/6f/Logo_of_Twitter.svg\">", "image"))

# type: fontawesome | image
# if link has type "image"
#   then create icon '<img src="images/{id}.svg">'
# else
#   then create icon '<i class="fas fa-{id}"></i>

# OG METADATA
OG_TITLE = SITENAME
OG_DESCRIPTION = AUTHOR_INFO["DESCRIPTION"]