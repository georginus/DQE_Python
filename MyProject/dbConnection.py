import psycopg2


conn = psycopg2.connect(host='localhost', dbname='georginus', user='georginus', password='')
cursor = conn.cursor()