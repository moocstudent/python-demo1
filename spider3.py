import requests
from bs4 import BeautifulSoup
import mysql.connector

url = 'http://chengyu.wx6.org/category_4zi.aspx'
response = requests.get(url)
htmlText = response.text

mydb = mysql.connector.connect(
    host="localhost",
    user="happy1",
    passwd="zhangqi1112",
    database="mathforhim",
    port=3306,
    autocommit=1
)

heCursor = mydb.cursor()
heCursor.execute("CREATE TABLE IF NOT EXISTS phrase_records (id int(10) auto_increment primary key,"
                 "name varchar(20),pinyin varchar(30), desc varchar(300))")

soup = BeautifulSoup(htmlText, 'lxml')
# print(response.text)
# print(soup.find_all('li'))

if (soup.find_all('li')):
    tuple = ()
    for four_a in soup.find_all('li'):
        # print(four_a.text.split())
        if (len(four_a.text.split()) == 6):
            singleTuple = []
            singleTuple.append(four_a.text.split()[0])
            singleTuple.append(' '.join(four_a.text.split()[1:5]))
            singleTuple.append(' '.join(four_a.text.split()[5]))
            print(singleTuple)

            tuple = tuple + singleTuple

    sql = "insert into phrase_records (name, pinyin,desc) VALUES (%s, %s, %s)"
    heCursor.executemany(sql, tuple)
    print(heCursor.rowcount, 'was inserted.')
