import os
import dj_database_url
MYSQL = {
    'default': dj_database_url.parse(os.environ.get('mysql://root:TRFCqihGtyBhmBNCBctCKQAKgwAtJNAm@mysql.railway.internal:3306/railway'))
}
