import psycopg
#from config import config


def connect():
    # connect to postgresql database server
    conn = None
    try:
        # read connection parameters
        #params = config()

        # connect to postgresql server
        print("Connecting to PostgresSQL database...")
        conn = psycopg.connect(host="localhost", dbname='mybusiness', user='postgres', password='postgres', port=5432)

        # create curser
        cur = conn.cursor()

        # run a sql statement
        print('PostgresSQL database version:')
        cur.execute('SELECT version()')

        # print server version
        version = cur.fetchone()
        print(version)

        # close the communication
        cur.close()

    except (Exception, psycopg.DatabaseError) as error:
        print("error: ", error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection is closed.')


if __name__ == '__main__':
    connect()
