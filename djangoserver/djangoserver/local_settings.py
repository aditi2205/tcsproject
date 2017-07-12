import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'd19ukjm63886sq',
       'USER': 'kauabkvvkfjhmn',
       'PASSWORD': 'e88c871484514d90615e1e7d467c90115950678e6558eaacc57722f89879ca20',
       'HOST': 'ec2-54-247-189-64.eu-west-1.compute.amazonaws.com',
       'PORT': '5432',
    }
    #'default': {
     #   'ENGINE': 'django.db.backends.postgresql',
      #  'NAME': 'tcs',
       # 'USER': 'root',
        #'PASSWORD': '1234',
        #'HOST': 'localhost',
        #'PORT': '5432',
    #}

}

DEBUG = True
