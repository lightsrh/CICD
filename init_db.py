import os
# import psycopg2
import json
from dotenv import load_dotenv

def create_sequence(conn, cur):
    # SQL CREATE SEQUENCE statement
    sql = "CREATE SEQUENCE IF NOT EXISTS city_id_seq"

    # Execute the SQL statement
    cur.execute(sql)

    # Commit the changes
    conn.commit()

def create_table(conn, cur):

    # SQL CREATE TABLE statement
    sql = "CREATE TABLE IF NOT EXISTS city ( id SERIAL PRIMARY KEY, department_code VARCHAR(255) NOT NULL, insee_code VARCHAR(255), zip_code VARCHAR(255), name VARCHAR(255) NOT NULL, lat FLOAT, lon FLOAT)"

    # Execute the SQL statement
    cur.execute(sql)

    # Commit the changes
    conn.commit()

def create_sequence(conn, cur):
    # SQL CREATE SEQUENCE statement
    sql = "CREATE SEQUENCE IF NOT EXISTS city_id_seq"

    # Execute the SQL statement
    cur.execute(sql)

    # Commit the changes
    conn.commit()

def create_table(conn, cur):

    # SQL CREATE TABLE statement
    sql = "CREATE TABLE IF NOT EXISTS city ( id SERIAL PRIMARY KEY, department_code VARCHAR(255) NOT NULL, insee_code VARCHAR(255), zip_code VARCHAR(255), name VARCHAR(255) NOT NULL, lat FLOAT, lon FLOAT)"

    # Execute the SQL statement
    cur.execute(sql)

    # Commit the changes
    conn.commit()

def insert_data(conn, cur, data):
    for record in data:
        department_code = record["department_code"]
        insee_code = record["insee_code"]
        zip_code = record["zip_code"]
        name = record["name"]
        lat = record["lat"]
        lon = record["lon"]

        # SQL INSERT statement
        sql = "INSERT INTO city (id, department_code, insee_code, zip_code, name, lat, lon) VALUES ((SELECT nextval('city_id_seq')), %s, %s, %s, %s, %s, %s)"
        values = (department_code, insee_code, zip_code, name, lat, lon)

        # Execute the SQL statement
        cur.execute(sql, values)
load_dotenv()


load_dotenv()


conn = psycopg2.connect(
    host=os.environ.get('POSTGRES_HOST'),
    dbname=os.environ.get('POSTGRES_DB'),
    user=os.environ.get('POSTGRES_USER'),
    password=os.environ.get('POSTGRES_PASSWORD'),
    port=os.environ.get('POSTGRES_PORT')
)

cur = conn.cursor()

create_sequence(conn, cur)

create_table(conn, cur)

with open("cities.json", "r") as json_file:
    data = json.load(json_file)

insert_data(conn, cur, data)

conn.commit()

cur.close()
conn.close()
