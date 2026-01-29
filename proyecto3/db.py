import os
MYSQL = {
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL")
    )
    }

