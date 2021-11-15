import os
import numpy as np
import pandas as pd
import psycopg2
import nameFileTable
from dataTypes import dataTypes
from columnName import columnName
from dbConnection import cursor, conn

file_path = "./Import/201807-CPH.csv"
file_name = '201807-CPH.csv'

df = pd.read_csv(file_path)
df.head()

# drop table if exists
cursor.execute(f"drop table if exists cph;")
# create table
cursor.execute(f"create table cph ({columnName(df)});")

# insert into table

# save df to csv
df.to_csv('cph.csv', header=df.columns, index=False, encoding='utf-8')

# open csv file
my_file = open('cph.csv')
print('file opened in memory')

# upload to DB
SQL_STATEMENT = """
COPY cph from STDIN WITH 
    CSV
    HEADER
    DELIMITER AS ','
"""

cursor.copy_expert(sql=SQL_STATEMENT, file=my_file)

print('file copied to db')

cursor.execute("grant select on table cph to public")
conn.commit()

cursor.close()
conn.close()

print('table cph imported to db successfully')