import os
MYSQL = {
'default': {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),          # Nombre de la base de datos
        'USER': os.getenv('DB_USER'),          # Usuario
        'PASSWORD': os.getenv('DB_PASSWORD'),  # Contraseña
        'HOST': os.getenv('DB_HOST'),          # Host
        'PORT': os.getenv('DB_PORT', '3306'),  # Puerto (3306 por defecto)
    }
    }
}
