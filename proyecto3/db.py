import os
import dj_database_url
MYSQL = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
