#!/usr/bin/env python
import sys

from django.conf import settings
from django.core.management import execute_from_command_line


if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.contrib.redirects.middleware.RedirectFallbackMiddleware'
        ),
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.admin',
            'django.contrib.redirects',

            'opps.core',
            'opps.channels',
            'opps.boxes',
            'opps.sources',
            'opps.articles',
            'opps.images',
            'opps.sitemaps',
            'opps.containers',
            'opps.archives',
            'opps.flatpages',

            'opps.hubcasts',
            'taggit',
            'south',

        ),
        SITE_ID = 1,
        ROOT_URLCONF = "opps.urls",
        TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner',
        HAYSTACK_CONNECTIONS = {
            'default': {
                'ENGINE': 'haystack.backends.simple_backend.SimpleEngine'
            }
        }
    )


def runtests():
    argv = [sys.argv[0], 'test', 'hubcasts']
    execute_from_command_line(argv)
    sys.exit(0)


if __name__ == '__main__':
    runtests()
