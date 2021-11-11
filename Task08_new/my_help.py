# SQLite3

import sqlite3

## connect

# with sqlite3.connect('task09.db') as connection:
#
#      cursor = connection.cursor()
#
#      # if table not exist:
#          #cursor.execute('create table people (first_name text, last_name text, age real)')
#      #cursor.execute("insert into people values ('George', 'Chichenkov', '42')")
#      #cursor.execute("insert into people values ('Vika', 'Chichenkova', '22')")
#
#
#      connection.commit()
#
#      cursor.execute("select * from people")
#
#      result = cursor.fetchall()
#      print(result)
#      print(result[0].last_name)
#      print(result[1][0])
#
#      cursor.close()
#      #connection.close()


# ## pyodbc
import pyodbc
import textwrap

print(pyodbc.drivers())

connection = pyodbc.connect('DRIVER={SQLite3 ODBC Driver};'
                            'Direct=True;'
                            'Database=task09.db;'
                            'String Types=Unicode',
                            autocommit=True)

# sql = textwrap.dedent("""
# select p.date_of_birth,
#            p.email,
#            a.city
#     from person as p
#     left outer join address as a on a.address_id = p.address_id
#     where p.status = 'active'
#       and p.name = ?
# """)
# rows = cursor.execute(sql, 'John Smith').fetchall()
