import psycopg2


conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='')
cursor = conn.cursor()