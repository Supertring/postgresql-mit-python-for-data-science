# Inserting one row into a PostgreSQL table

import psycopg


def insert_vendor(vendor_name):
    # insert a new vendor into the vendors table
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""

    conn = None
    vendor_id = None

    try:
        # connect to the database server
        conn = psycopg.connect(host='localhost', dbname='mybusiness', user='postgres', password='postgres', port=5432)

        # create a new cursor
        cur = conn.cursor()

        # execute the INSERT statement
        cur.execute(sql, (vendor_name,))

        # get the generated vendor_id back
        vendor_id = cur.fetchone()[0]

        # commit the changes to the database
        conn.commit()

        # close communication with the database
        cur.close()

    except(Exception, psycopg.DatabaseError) as error:
        print("error: ", error)

    finally:
        if conn is not None:
            conn.close()

    return vendor_id


if __name__ == '__main__':
    # insert one vendor
    insert_vendor("you & co.")
    print("inserted successfully")

