import mysql.connector
from datetime import datetime
from bs4 import BeautifulSoup
import requests

url = 'https://www.coindesk.com/price/bitcoin/'


# function for receive date and time
def now():
    now_time = datetime.now()
    date = now_time.strftime("%d/%m/%Y %H:%M:%S")
    return date


Now = now()

# requests to site
r = requests.get(url)

# working with BeautifulSoup typography__StyledTypography-owin6q-0 jvRAOp
soup = BeautifulSoup(r.text, 'html.parser')

price = soup.find('span',attrs={'class':'typography__StyledTypography-owin6q-0 jvRAOp'})
prices = price.text

# connecting to database
conn = mysql.connector.connect(host='localhost', user='root', password='', database='Btc_Price')
cursor = conn.cursor()
cursor.execute('INSERT INTO price VALUES(\'%s\',\'%s\')'%(prices,Now))
conn.commit()
conn.close()
