import os
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 

def get_env_variable(var_name):
	try:
		return os.environ[var_name]
	except KeyError:
		error_msg = "Environment variable %s not set!" % var_name
		raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('SECRET_KEY')

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
	'django.contrib.auth',
	'django.contrib.admin',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'mysite.core',
	'flat',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			os.path.join(BASE_DIR, 'mysite/templates')
		],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'

CELERY_BROKER_URL = 'amqp://localhost'
CELERYD_HIJACK_ROOT_LOGGER = False

# Logging config
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
     'formatters': {
        'detailed': {
            'format': '[%(levelname)s] %(asctime)s [FileName: %(filename)s FuncName: %(funcName)s() LineNo: %(lineno)d] %(message)s',
        },
        'simple': {
            'format': '[%(levelname)s] %(asctime)s %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logFile.log',
            'formatter': 'detailed',
            'maxBytes': 1024*1024*10 # 10MB
        },
    },
     'loggers': {
        'general': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}