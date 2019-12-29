DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'hodgimoto.com']
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'hodgimoto',
        'USER': 'postgres',
    }
}
