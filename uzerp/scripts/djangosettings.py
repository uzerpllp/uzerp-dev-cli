# -*- coding: utf-8 -*-
#
# Copyright (C) 2007-2015 by frePPLe bvba
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

r"""
Main Django configuration file.
"""
import os, sys

from django.utils.translation import gettext_lazy as _

try:
    DEBUG = "runserver" in sys.argv
except Exception:
    DEBUG = False
DEBUG_JS = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

# ================= START UPDATED BLOCK BY WINDOWS INSTALLER =================
# Make this unique, and don't share it with anybody.
SECRET_KEY = "%@mzit!i8b*$zc&6oev96=RANDOMSTRING"

# FrePPLe only supports the postgresql database.
# Create additional entries in this dictionary to define scenario schemas.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "frepple",
        "USER": "frepple",  # Role name when using md5 authentication.
        # Leave as an empty string when using peer or
        # ident authencation.
        "PASSWORD": "frepple",  # Role password when using md5 authentication.
        # Leave as an empty string when using peer or
        # ident authencation.
        "HOST": "localhost",  # When using TCP sockets specify the hostname,
        # the ip4 address or the ip6 address here.
        # Leave as an empty string to use Unix domain
        # socket ("local" lines in pg_hba.conf).
        "PORT": "5432",  # Leave to empty string when using Unix domain sockets.
        # Specify the port number when using a TCP socket.
        "OPTIONS": {},  # Backend specific configuration parameters.
        "TEST": {
            "NAME": "frepple"  # Database name used when running the test suite.
        },
        "FILEUPLOADFOLDER": os.path.normpath(
            os.path.join(FREPPLE_LOGDIR, "data", "default")
        ),
        # Role name for executing custom reports and processing sql data files.
        # Make sure this role has properly restricted permissions!
        # When left unspecified, SQL statements run with the full read-write
        # permissions of the user specified above. Which can be handy, but is not secure.
        "SQL_ROLE": "report_role",
        "SECRET_WEBTOKEN_KEY": SECRET_KEY,
    },
    "scenario1": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "scenario1",
        "USER": "frepple",  # Role name when using md5 authentication.
        # Leave as an empty string when using peer or
        # ident authencation.
        "PASSWORD": "frepple",  # Role password when using md5 authentication.
        # Leave as an empty string when using peer or
        # ident authencation.
        "HOST": "",  # When using TCP sockets specify the hostname,
        # the ip4 address or the ip6 address here.
        # Leave as an empty string to use Unix domain
        # socket ("local" lines in pg_hba.conf).
        "PORT": "",  # Leave to empty string when using Unix domain sockets.
        # Specify the port number when using a TCP socket.
        "OPTIONS": {},  # Backend specific configuration parameters.
        "TEST": {
            "NAME": "test_scenario1"  # Database name used when running the test suite.
        },
        "FILEUPLOADFOLDER": os.path.normpath(
            os.path.join(FREPPLE_LOGDIR, "data", "scenario1")
        ),
        # Role name for executing custom reports and processing sql data files.
        # Make sure this role has properly restricted permissions!
        # When left unspecified, SQL statements run with the full read-write
        # permissions of the user specified above. Which can be handy, but is not secure.
        "SQL_ROLE": "report_role",
        "SECRET_WEBTOKEN_KEY": SECRET_KEY,
    },
    "scenario2": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "scenario2",
        "USER": "frepple",  # Role name when using md5 authentication.
        # Leave as an empty string when using peer or
        # ident authencation.
        "PASSWORD": "frepple",  # Role password when using md5 authentication.
        # Leave as an empty string when using peer or
        # ident authencation.
        "HOST": "",  # When using TCP sockets specify the hostname,
        # the ip4 address or the ip6 address here.
        # Leave as an empty string to use Unix domain
        # socket ("local" lines in pg_hba.conf).
        "PORT": "",  # Leave to empty string when using Unix domain sockets.
        # Specify the port number when using a TCP socket.
        "OPTIONS": {},  # Backend specific configuration parameters.
        "TEST": {
            "NAME": "test_scenario2"  # Database name used when running the test suite.
        },
        "FILEUPLOADFOLDER": os.path.normpath(
            os.path.join(FREPPLE_LOGDIR, "data", "scenario2")
        ),
        # Role name for executing custom reports and processing sql data files.
        # Make sure this role has properly restricted permissions!
        # When left unspecified, SQL statements run with the full read-write
        # permissions of the user specified above. Which can be handy, but is not secure.
        "SQL_ROLE": "report_role",
        "SECRET_WEBTOKEN_KEY": SECRET_KEY,
    },
    "scenario3": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "scenario3",
        "USER": "frepple",  # Role name when using md5 authentication.
        # Leave as an empty string when using peer or
        # ident authencation.
        "PASSWORD": "frepple",  # Role password when using md5 authentication.
        # Leave as an empty string when using peer or
        # ident authencation.
        "HOST": "",  # When using TCP sockets specify the hostname,
        # the ip4 address or the ip6 address here.
        # Leave as an empty string to use Unix domain
        # socket ("local" lines in pg_hba.conf).
        "PORT": "",  # Leave to empty string when using Unix domain sockets.
        # Specify the port number when using a TCP socket.
        "OPTIONS": {},  # Backend specific configuration parameters.
        "TEST": {
            "NAME": "test_scenario3"  # Database name used when running the test suite.
        },
        "FILEUPLOADFOLDER": os.path.normpath(
            os.path.join(FREPPLE_LOGDIR, "data", "scenario3")
        ),
        # Role name for executing custom reports and processing sql data files.
        # Make sure this role has properly restricted permissions!
        # When left unspecified, SQL statements run with the full read-write
        # permissions of the user specified above. Which can be handy, but is not secure.
        "SQL_ROLE": "report_role",
        "SECRET_WEBTOKEN_KEY": SECRET_KEY,
    },
}

LANGUAGE_CODE = "en"

# uzERP database connection settings
UZERP_DB = {
	'NAME': 'uzerp',
	'USER': 'frepple',
	'PASSWORD': 'frepple',
	'HOST': 'localhost',
	'PORT': ''
}

# uzERP connector settings
UZERP_SETTINGS = {
	'EXPORT': {
		'wo_documentation': ('26', '9'),
			# Database id's of the uzERP work order
			# documentation injector classes
		'wo_release_fence': 2,
			# Planned purchase orders due to start after this
			# number of days from today will not be exported
		'po_release_fence': 2
			# Planned purchase orders due to start after this
			# number of days from today will not be exported
	}
}

# Google analytics code to report usage statistics to.
# The value None disables this feature.
GOOGLE_ANALYTICS = None  # "UA-1950616-4"

# ================= END UPDATED BLOCK BY WINDOWS INSTALLER =================

# If passwords are set in this file they will be used instead of the ones set in the database parameters table
ODOO_PASSWORDS = {"default": "", "scenario1": "", "scenario2": "", "scenario3": ""}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Europe/London"

# A boolean that specifies if datetimes will be timezone-aware by default or not.
# If this is set to True, we will use timezone-aware datetimes internally.
# Otherwise, we use naive datetimes in local time.
USE_TZ = False  # TODO Test with this parameter set to True

# Supported language codes, sorted by language code.
# Language names and codes should match the ones in Django.
# You can see the list supported by Django at:
#    https://github.com/django/django/blob/master/django/conf/global_settings.py
LANGUAGES = (
    ("en", _("English")),
    ("fr", _("French")),
    ("de", _("German")),
    ("he", _("Hebrew")),
    ("it", _("Italian")),
    ("ja", _("Japanese")),
    ("nl", _("Dutch")),
    ("pt", _("Portuguese")),
    ("pt-br", _("Brazilian Portuguese")),
    ("ru", _("Russian")),
    ("es", _("Spanish")),
    ("zh-cn", _("Simplified Chinese")),
    ("zh-tw", _("Traditional Chinese")),
)

# The remember-me checkbox on the login page allows to keep a session cookie
# active in your browser. The session will expire after the age configured
# in the setting below (epxressed in seconds).
# Set the value to 0 to force users to log in for every browser session.
SESSION_COOKIE_AGE = 3600 * 24 * 3  # 3 days

MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # Uncomment the next line to automatically log on as the admin user,
    # which can be useful for development or for demo models.
    # 'freppledb.common.middleware.AutoLoginAsAdminUser',
    "freppledb.common.middleware.MultiDBMiddleware",
    "freppledb.common.middleware.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
)

# Installed applications.
# The order is important: urls, templates and menus of the earlier entries
# take precedence over and override later entries.
INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bootstrap3",
    "freppledb.boot",
    # Add any project specific apps here
    # "freppledb.odoo",
    "uzerp",
    #'freppledb.erpconnection',
    "freppledb.input",
    "freppledb.output",
    "freppledb.metrics",
    "freppledb.execute",
    "freppledb.common",
    "django_filters",
    "rest_framework",
    "django_admin_bootstrapped",
    "django.contrib.admin",
    # The next two apps allow users to run their own SQL statements on
    # the database, using the SQL_ROLE configured above.
    "freppledb.reportmanager",
    # "freppledb.executesql",
)

# Custom attribute fields in the database
# After each change of this setting, the following commands MUST be
# executed to create the fields in the database(s).
#   frepplectl makemigrations
#   frepplectl migrate     OR     frepplectl migrate --database DATABASE
#
# The commands will create migration files to keep track of the changes.
# You MUST use the above commands and the generated migration scripts. Manually
# changing the database schema will work in simple cases, but will get you
# in trouble in the long run!
# You'll need write permissions in the folder where these are stored.
#
# See https://docs.djangoproject.com/en/1.8/topics/migrations/ for the
# details on the migration files. For complex changes to the attributes
# an administrator may need to edit, delete or extend these files.
#
# Supported field types are 'string', 'boolean', 'number', 'integer',
# 'date', 'datetime', 'duration' and 'time'.
# Example:
#  ATTRIBUTES = [
#    ('freppledb.input.models.Item', [
#      ('attribute1', ugettext('attribute_1'), 'string'),
#      ('attribute2', ugettext('attribute_2'), 'boolean'),
#      ('attribute3', ugettext('attribute_3'), 'date'),
#      ('attribute4', ugettext('attribute_4'), 'datetime'),
#      ('attribute5', ugettext('attribute_5'), 'number'),
#      ]),
#    ('freppledb.input.models.Operation', [
#      ('attribute1', ugettext('attribute_1'), 'string'),
#      ])
#    ]
ATTRIBUTES = []

import django.contrib.admindocs

LOCALE_PATHS = (
    os.path.normpath(os.path.join(FREPPLE_HOME, "locale", "django")),
    os.path.normpath(os.path.join(FREPPLE_HOME, "locale", "auth")),
    os.path.normpath(os.path.join(FREPPLE_HOME, "locale", "contenttypes")),
    os.path.normpath(os.path.join(FREPPLE_HOME, "locale", "sessions")),
    os.path.normpath(os.path.join(FREPPLE_HOME, "locale", "admin")),
    os.path.normpath(os.path.join(FREPPLE_HOME, "locale", "messages")),
    os.path.normpath(os.path.join(FREPPLE_APP, "freppledb", "locale")),
    os.path.normpath(
        os.path.join(os.path.dirname(django.contrib.admindocs.__file__), "locale")
    ),
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # os.path.normpath(os.path.join(FREPPLE_HOME,'templates')),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "builtins": ["freppledb.common.templatetags"],
            "context_processors": [
                "freppledb.common.contextprocessors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.static",
            ],
        },
    }
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "null": {"level": "DEBUG", "class": "logging.NullHandler"},
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "mail_admins": {
            "level": "CRITICAL",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        # A handler to log all SQL queries.
        # The setting "DEBUG" also needs to be set to True higher up in this file.
        #'django.db.backends': {
        #    'handlers': ['console'],
        #    'level': 'DEBUG',
        #    'propagate': False,
        # },
        "django": {"handlers": ["console"], "level": "INFO"},
        "freppledb": {"handlers": ["console"], "level": "INFO"},
        "freppleapps": {"handlers": ["console"], "level": "INFO"},
    },
}

# Maximum allowed memory size for the planning engine. Only used on Linux!
MAXMEMORYSIZE = None  # limit in MB, minimum around 230, use None for unlimited

# Maximum allowed memory size for the planning engine. Only used on Linux!
MAXCPUTIME = None  # limit in seconds, use None for unlimited

# Max total log files size in MB, if the limit is reached deletes the oldest.
MAXTOTALLOGFILESIZE = 200

# A list of available user interface themes.
# If multiple themes are configured in this list, the user's can change their
# preferences among the ones listed here.
# If the list contains only a single value, the preferences screen will not
# display users an option to choose the theme.
THEMES = [
    "earth",
    "grass",
    "lemon",
    "odoo",
    "openbravo",
    "orange",
    "snow",
    "strawberry",
    "water",
]

# A default user-group to which new users are automatically added
DEFAULT_USER_GROUP = None

# The default user interface theme
DEFAULT_THEME = "earth"

# The default number of records to pull from the server as a page
DEFAULT_PAGESIZE = 100

# Configuration of the default dashboard
DEFAULT_DASHBOARD = [
    {
        "rowname": _("Welcome"),
        "cols": [
            {"width": 6, "widgets": [("welcome", {})]},
            {"width": 6, "widgets": [("news", {})]},
        ],
    },
    {
        "rowname": _("sales"),
        "cols": [
            {
                "width": 9,
                "widgets": [
                    ("late_orders", {"limit": 20}),
                    ("short_orders", {"limit": 20}),
                ],
            },
            {
                "width": 3,
                "widgets": [
                    ("demand_alerts", {}),
                    ("delivery_performance", {"green": 90, "yellow": 80}),
                ],
            },
        ],
    },
    {
        "rowname": _("purchasing"),
        "cols": [
            {
                "width": 9,
                "widgets": [
                    ("purchase_orders", {"fence1": 7, "fence2": 30}),
                    # ("purchase_queue",{"limit":20}),
                    ("purchase_order_analysis", {"limit": 20}),
                ],
            },
            {
                "width": 3,
                "widgets": [
                    ("inventory_by_location", {"limit": 5}),
                    ("inventory_by_item", {"limit": 10}),
                ],
            },
        ],
    },
    {
        "rowname": _("distribution"),
        "cols": [
            {
                "width": 12,
                "widgets": [
                    ("distribution_orders", {"fence1": 7, "fence2": 30}),
                    # ("shipping_queue",{"limit":20}),
                ],
            }
        ],
    },
    {
        "rowname": _("manufacturing"),
        "cols": [
            {
                "width": 9,
                "widgets": [
                    ("manufacturing_orders", {"fence1": 7, "fence2": 30}),
                    # ("resource_queue",{"limit":20}),
                ],
            },
            {
                "width": 3,
                "widgets": [
                    ("capacity_alerts", {}),
                    ("resource_utilization", {"limit": 5, "medium": 80, "high": 90}),
                ],
            },
        ],
    },
    {
        "rowname": _("activity"),
        "cols": [
            {"width": 6, "widgets": [("recent_comments", {"limit": 10})]},
            {"width": 6, "widgets": [("recent_actions", {"limit": 10})]},
        ],
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 8},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "your_email@domain.com"
SERVER_EMAIL = "your_email@domain.com"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "your_email@domain.com"
EMAIL_HOST_PASSWORD = "frePPLeIsTheBest"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# Port number when not using Apache
PORT = 8000
