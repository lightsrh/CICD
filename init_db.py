import os
import psycopg2
import json

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
        sql = "INSERT INTO your_table_name (id, department_code, insee_code, zip_code, name, lat, lon) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (id, department_code, insee_code, zip_code, name, lat, lon)

        # Execute the SQL statement
        cur.execute(sql, values)

conn = psycopg2.connect(
    host=os.getenv("CITY_API_ADDR"),
    database=os.getenv("CITY_API_DB_URL"),
    user=os.getenv("CITY_API_DB_USER"),
    password=os.getenv("CITY_API_DB_PWD"),
    port=os.getenv("CITY_API_PORT")
)

cur = conn.cursor()

with open("cities.json", "r") as json_file:
    data = json.load(json_file)

insert_data(conn, cur, data)

conn.commit()

cur.close()
conn.close()
