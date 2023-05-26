# Thise code connect to mysql database get data from display data from  the frontend application.
#first create one folder and create file app.py for example from same folder with templates folder create index.html save run the python3 app.py and get ip address from frontend display data.
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


cnx = mysql.connector.connect(
    host="database-reddy.cdcacngfasur.us-east-1.rds.amazonaws.com",
    user="admin",
    password="lkjhgfdsa",
    database="application_db"
)

cursor = cnx.cursor()


@app.route('/', methods=['GET'])
def index():
   
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()


    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)