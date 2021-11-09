# SQLite3

import sqlite3

## connect

connection = sqlite3.connect('task09.db')

cursor = connection.cursor()

cursor.execute('create table people (first_name text, last_name text, age real)')

cursor.close()
connection.close()