AUTHOR = 'Nataniella Ogogo'
SITENAME = "Jamila's Resume (COMP 2600 A2)"
SITEURL = ""

PATH = "content"

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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

DEFAULT_PAGINATION = False

MARKUP = ('md',)

SITEURL = 'https://github.com/nataniella-o/comp2600_a2.git'

STATIC_PATHS = ['theme', 'static', 'extra']
THEME_STATIC_DIR = 'theme'
EXTRA_PATH_METADATA = {
    'theme/css/main.css': {'path': 'theme/css/main.css'},
}

THEME = "pelican-themes/Flex"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
