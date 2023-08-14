# Steps for creating postgresql tables in python
# Construct create table statements
# Connect postgresql database
# Create cursor object
# execute the statement CREATE TABLE
# Close the cursor and connection

import psycopg


def create_tables():
    """Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE vendors(
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,

        """
        CREATE TABLE parts(
            part_id SERIAL PRIMARY KEY,
            part_name VARCHAR(255) NOT NULL
        )
        """,

        """
        CREATE TABLE vendor_parts(
            vendor_id INTEGER NOT NULL,
            part_id INTEGER NOT NULL,
            PRIMARY KEY (vendor_id, part_id),
            
            FOREIGN KEY (vendor_id)
                REFERENCES vendors (vendor_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
                
            FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,

        """
        CREATE TABLE part_drawings(
            part_id INTEGER NOT NULL,
            file_extension VARCHAR(255) NOT NULL,
            drawing_data BYTEA NOT NULL,
            
            FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )

    conn = None
    try:
        # connect to postgresql server
        print("Connecting to PostgresSQL database...")
        conn = psycopg.connect(host="localhost", dbname='mybusiness', user='postgres', password='postgres', port=5432)

        # create cursor
        cur = conn.cursor()

        # execute sql commands
        for command in commands:
            cur.execute(command)

        # close communication with database
        cur.close()

        # commit the changes
        conn.commit()
    except (Exception, psycopg.DatabaseError) as error:
        print("error: ", error)

    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
