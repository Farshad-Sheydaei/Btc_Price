import mysql.connector
from datetime import datetime


def now():
    now_time = datetime.now()
    date = now_time.strftime("%d/%m/%Y %H:%M:%S")
    return date

conn = mysql.connector.connect(host='localhost', user='root', password='', database='Btc_Price')
cursor = conn.cursor()
conn.close()