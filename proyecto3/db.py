import os
import dj_database_url
MYSQL = {
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQLDATABASE'),
        'USER': os.environ.get('MYSQLUSER'),
        'PASSWORD': os.environ.get('MYSQLPASSWORD'),
        'HOST': os.environ.get('MYSQLHOST'),
        'PORT': os.environ.get('MYSQLPORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
