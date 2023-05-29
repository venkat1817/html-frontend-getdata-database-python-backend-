#Thise code interact with first elastic cache to check the data is there or not next request go to database to get data display to frontend html code. 
from flask import Flask, render_template
from flask_caching import Cache
import mysql.connector
import redis

app = Flask(__name__)
cache = Cache(app)


app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_URL'] = 'redis://clustercfg.database-chache.v49ygn.use1.cache.amazonaws.com:6379'

cnx = mysql.connector.connect(
    host="database-reddy.cdcacngfasur.us-east-1.rds.amazonaws.com",
    user="admin",
    password="lkjhgfdsa",
    database="application_db"
)

cursor = cnx.cursor()


@app.route('/', methods=['GET'])
@cache.cached(timeout=60)
def index():
    data = cache.get('data')

    if data is None:
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        cache.set('data', data)

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
