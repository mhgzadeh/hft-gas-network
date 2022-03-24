import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i#xxkz@ve66c-o#tv=x2!6xs4!t$(%7fhk43gp7$k_ex@dhu+p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
NAME = 'gas_network'
USER = 'Mohammad'
PASSWORD = 'mhgz1996'
HOST = 'localhost'
PORT = 5432

# Gdal path
if os.name == 'nt':
    VENV_BASE = os.environ['VIRTUAL_ENV']
    os.environ['PATH'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo') + ';' + os.environ['PATH']
    os.environ['PROJ_LIB'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo\\data\\proj') + ';' + os.environ['PATH']
