# Inserting one row into a PostgreSQL table

import psycopg


def update_vendor(vendor_name, vendor_id):
    # insert a new vendor into the vendors table
    sql = """UPDATE vendors
                SET vendor_name=%s
                WHERE vendor_id=%s"""

    conn = None

    try:
        # connect to the database server
        conn = psycopg.connect(host='localhost', dbname='mybusiness', user='postgres', password='postgres', port=5432)

        # create a new cursor
        cur = conn.cursor()

        # execute the INSERT statement
        cur.execute(sql, (vendor_name, vendor_id))

        # get the number of updated rows
        updated_rows = cur.rowcount

        # commit the changes to the database
        conn.commit()

        # close communication with the database
        cur.close()

    except(Exception, psycopg.DatabaseError) as error:
        print("error: ", error)

    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    # insert one vendor
    update_vendor("Super Inc.", 1)
    print("updated successfully")

