import psycopg


# Introduction to the transaction in psycopg

def add_part(part_name, vendor_list):
    # insert a new row into the part table
    insert_part = "INSERT INTO parts(part_name) VALUES (%s) RETURNING part_id;"

    # insert a new row into the vendor parts table
    assign_vendor = "INSERT INTO vendor_parts(vendor_id,  part_id) VALUES(%s, %s)"

    conn = None
    try:
        conn = psycopg.connect(host="localhost", dbname='mybusiness', user='postgres', password='postgres', port=5432)
        cur = conn.cursor()

        # insert a new part
        cur.execute(insert_part, (part_name,))

        # get the part id
        part_id = cur.fetchone()[0]

        # assign parts provided by vendors
        for vendor_id in vendor_list:
            cur.execute(assign_vendor, (vendor_id, part_id))

        # commit changes
        conn.commit()
        print("Committed successfully")
    except(Exception, psycopg.DatabaseError) as error:
        print("Error: ", error)

    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    add_part('transistor', (1, 2))
    add_part('motion sensor', (2, 3))
    add_part('acoustic sensor', (4, 5))

    # add an invalid vendor id to demonstrate foreign key violations, must not add row
    add_part('heat sensor', (99, 100, 200))
    # Error:  insert or update on table "vendor_parts" violates foreign key constraint "vendor_parts_vendor_id_fkey"
    # DETAIL:  Key (vendor_id)=(99) is not present in table "vendors".
