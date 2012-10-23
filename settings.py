import os
import sys

# App configuration (see README for details)
# You will need to change these
APP_ID = '3bdc36a7-730f-4532-845b-224fa64a17aa'
APP_THUMBPRINT = '0655AB192E95BC35F96128FFF9F529D6FD0206EF'
APP_PUBLIC_KEY = '0x00cc1f3ca8a75dc0ab84d5e7b5c27f6a59b3732e53acc6faddde276df8102964418ab9516e5418ded69d44c794de9cad7b805c6ccb1bbcbd1acfb9178b68913ae1e49112975aabbe4493a46dbf5edb05d4fb31de428868838f74b17bc62040e79ea93481cb712f6e44febe74b4508e2d1c127d558fbb1d2892eb933435b50ea9b4fa184c4968c7a8c4faf2273dc238749d186a9514572bc4d2e8a82d048aa396f7e8ad5bc64acd269d3f2304a730c07df9afc9ef335c1d4d66e374a31bf77f6063f0fcddd1878c3e76e520480dc95d54112c4380cc15473d2267c41001f0023c666cd92e059b492d8f20f4bebc332485b9e43c35e64c126f7d989b90737ca41565'
APP_PRIVATE_KEY = '0x00cb3f2f3f1fa7927936c366fcecb5c2479f0f4949b7f849433239409e88392ec2b446e27660f682ac5fdc647e2f4b02d2be75493ed457925468117d082b0eb0facc844766bdb9d4b2a3f04df707943eb25b8cc42aab78a5c6ea02efa3cfe9d0b782f3ed698d4215224e25863f2516ec83cf454d34d8b3a7fae2e6a84df202afa6e5385ee5f636524152f241d98198544dbb84c936826d6fb07317950a77235cbe1531969c1f96b8477792e7aabfe445db7e5e14a4b1e82d0ed7b020b8299b4e80238beeb64436e7f760d35b82fac5df1902b84083cb21b10e82db26a197640b78eca69294f7deb7ea6c518fefc7f004113535263ec71e7c382eee65561e152b01'

# probably won't need to change these for development
# todo: should we not be encoding here?
APP_ACTION_URL = 'http://localhost:8000/mvaultaction'
HV_SHELL_URL = 'https://account.healthvault-ppe.com'
HV_SERVICE_SERVER = 'platform.healthvault-ppe.com'

# django configuration
#############################################################################

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
git_sub_modules = BASE_DIR+'/healthvault' # Relative paths ok too
for dir in os.listdir(git_sub_modules):
    path = os.path.join(git_sub_modules, dir)
    if not path in sys.path:
        sys.path.append(path)

ROOT_URLCONF = 'urls'
TEMPLATE_DIRS = (BASE_DIR+'/app')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS

DATABASE_ENGINE = ''   # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''     # Or path to database file if using sqlite3.
DATABASE_USER = ''     # Not used with sqlite3.
DATABASE_PASSWORD = '' # Not used with sqlite3.
DATABASE_HOST = ''     # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''     # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
MEDIA_ROOT = ''
MEDIA_URL = ''
ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'xr--(48l1whu9keemewf@9j(og2i$3+ty9m%&97o6xkw1g$a#d'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
)
