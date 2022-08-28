import mysql.connector
from datetime import datetime
from bs4 import BeautifulSoup
import requests

# function for receive date and time
def now():
    now_time = datetime.now()
    date = now_time.strftime("%d/%m/%Y %H:%M:%S")
    return date
Now = now()

url = 'https://www.coindesk.com/price/bitcoin/'

# connecting to database
conn = mysql.connector.connect(host='localhost', user='root', password='', database='Btc_Price')
cursor = conn.cursor()

# requests to site
r = requests.get(url)

# working with BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
price = soup.find('span',attrs={'class':'typography__StyledTypography-owin6q-0 jvRAOp'})
prices = price.text

# Insert into database and commit this
cursor.execute('INSERT INTO price VALUES(\'%s\',\'%s\')'%(prices,Now))
conn.commit()
conn.close()
