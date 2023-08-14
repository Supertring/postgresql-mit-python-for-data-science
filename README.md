# Getting Started mit postgresql and python for data science

> PostgreSQL Python
* Connecting to the PostgreSQL database server
* Creating new PostgreSQL tables in Python
* Inserting data into the PostgreSQL table in Python
* Updating data in the PostgreSQL table in Python
* Transaction
* Querying data from PostgreSQL tables
* Calling a PostgreSQL function in Python
* Calling a PostgreSQL stored procedure in Python
* Handling PostgreSQL BLOB data in Python
* Deleting data from PostgreSQL tables in Python

## Create a new database

Log into the PostgreSQL database server using pgAdmin or psql and create a database in the database server

### Install Postgresql
Update apt
```bash
sudo apt update 
```

Install postgresql
```bash
sudo apt install postgresql postgresql-contrib
```

start the service
```bash
sudo systemctl start postgresql.service
```

set password for -user postgres
```bash
sudo -u postgres psql postgres
```

enter the following cmd and set password for postgres user
```bash
\password postgres
```

```bash
CREATE DATABASE mybusiness;
```

> Create table

> Construct STATEMENT
```commandline
 CREATE TABLE
 ```
> Connect to the PostgreSQL database

> Create a cursor

> Execute the sql statements

> Finally close the cursor and connection

> Run the cmd on psql to enter into the database: mybusiness
```commandline
\c mybusiness
```
```commandline
mybusiness=# \dt
```
