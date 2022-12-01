import requests
from bs4 import BeautifulSoup
import mysql.connector

url = 'http://chengyu.wx6.org/category_4zi.aspx'
response = requests.get(url)
htmlText = response.text

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="zhangqi1112",
    autocommit=1
)
print('db operation')
heCursor = mydb.cursor()
heCursor.execute("CREATE DATABASE IF NOT EXISTS phrase")
heCursor.execute("use phrase")
heCursor.execute("CREATE TABLE IF NOT EXISTS phrase_records (id int(10) auto_increment primary key,"
                 "name varchar(20),pinyin varchar(30),description varchar(300))")

soup = BeautifulSoup(htmlText, 'lxml')
# print(response.text)
# print(soup.find_all('li'))

if (soup.find_all('li')):
    tupleData = []
    for four_a in soup.find_all('li'):
        # print(four_a.text.split())
        if (len(four_a.text.split()) == 6):
            singleTuple = ()
            singleTuple = (four_a.text.split()[0], ' '.join(four_a.text.split()[1:5]), ' '.join(four_a.text.split()[5]))

            print(singleTuple)

            tupleData.append(tuple(singleTuple))

    print(tupleData)
    sql = "insert into phrase_records (name, pinyin,description) VALUES (%s, %s, %s)"
    heCursor.executemany(sql, tupleData)
    print(heCursor.rowcount, 'was inserted.')

