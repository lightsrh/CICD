import os
import psycopg2
import json
from dotenv import load_dotenv

def insert_data(conn, cur, data):
    for record in data:
        id = record["id"]
        department_code = record["department_code"]
        insee_code = record["insee_code"]
        zip_code = record["zip_code"]
        name = record["name"]
        lat = record["lat"]
        lon = record["lon"]

        # SQL INSERT statement
        sql = "INSERT INTO city (id, department_code, insee_code, zip_code, name, lat, lon) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (id, department_code, insee_code, zip_code, name, lat, lon)

        # Execute the SQL statement
        cur.execute(sql, values)

load_dotenv()


conn = psycopg2.connect(
    host=os.environ.get('CITY_API_ADDR'),
    dbname=os.environ.get('POSTGRES_DB'),
    user=os.environ.get('POSTGRES_USER'),
    password=os.environ.get('POSTGRES_PASSWORD'),
    port=os.environ.get('POSTGRES_PORT')
)

cur = conn.cursor()

with open("cities.json", "r") as json_file:
    data = json.load(json_file)

insert_data(conn, cur, data)

conn.commit()

cur.close()
conn.close()
