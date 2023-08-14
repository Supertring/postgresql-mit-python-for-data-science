# Inserting one row into a PostgreSQL table

import psycopg


def insert_many_vendor(vendor_list):
    # insert a new vendor into the vendors table
    sql = """INSERT INTO vendors(vendor_name) VALUES(%s)"""
    conn = None
    try:
        # connect to the database server
        conn = psycopg.connect(host='localhost', dbname='mybusiness', user='postgres', password='postgres', port=5432)

        # create a new cursor
        cur = conn.cursor()

        # execute the INSERT statement
        cur.executemany(sql, vendor_list)

        # commit the changes to the database
        conn.commit()

        # close communication with the database
        cur.close()

    except(Exception, psycopg.DatabaseError) as error:
        print("error: ", error)

    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    # insert one vendor
    insert_many_vendor([
        ('GI-J Inc.',),
        ('Inn Inc.',),
        ('Donaube Ltd.',),
        ('Illz rv.',)
    ])
    print("inserted multiple data successfully")

