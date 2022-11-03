import psycopg2
from config import config

def query_person():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = 'SELECT *FROM person;'
        cursor.execute(SQL)
        row = cursor.fetchone()
        print(row)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

if __name__ == '__main__':
    query_person()