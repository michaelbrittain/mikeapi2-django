from .base import *
import os

#installed Apps

INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR', '.')
NOSE_ARGS = [
    '--verbosity=2',                # verbose output
    '--nologcapture',               # don't output log capture
    '--with-coverage',              # activate coverage report
    '--cover-package=todo',        # coverage reports will apply to these packages
    '--with-spec',                  # spec style tests
    '--spec-color',
    '--with-xunit',                 # enable xunit plugin
    '--xunit-file=%s/unittests.xml' % TEST_OUTPUT_DIR,
    '--cover-xml',                   # produce xml coverage information
    '--cover-xml-file=%s/coverage.xml' % TEST_OUTPUT_DIR
]


#database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('MYSQL_DATABASE', 'mikeapidb'),
#         'USER': os.environ.get('MYSQL_USER', 'wonderousink'),
#         'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'sofia1234'),
#         'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
#         'PORT': os.environ.get('MYSQL_PORT', '5432')
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
