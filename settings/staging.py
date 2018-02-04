import dj_database_url

from settings.base import *

DEBUG = False
 
# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}