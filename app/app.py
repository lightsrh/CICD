import json
import os
from prometheus_client import Counter, Gauge, start_http_server, generate_latest
import random
import psycopg2
import dotenv
from flask import Response, Flask, request, jsonify

# Charger les variables d'environnement à partir du fichier .env
dotenv.load_dotenv()

app = Flask(__name__)

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

number_of_requests = Counter(
    'number_of_requests',
    'The number of requests, its a counter so the value can increase or reset to zero.'
)

current_memory_usage = Gauge(
    'current_memory_usage_locally',
    'The current value of memory usage, its a gauge so it can go up or down.',
    ['server_name']
)

# Fonction pour établir une connexion à la base de données


def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT")
    )
    return conn


@app.route('/city', methods=['POST'])
def createCity():
    data = request.get_json()
    print(data)

    if not isinstance(data, list):
        return jsonify({"error": "Request body must be a list of objects"}), 400

    # Établir une connexion à la base de données
    conn = get_db_connection()
    cur = conn.cursor()
    print("database connection established")

    for record in data:
        department_code = record.get('department_code')
        insee_code = record.get('insee_code')
        zip_code = record.get('zip_code')
        name = record.get('name')
        lat = record.get('lat')
        lon = record.get('lon')
        # Vérifier si les champs requis sont présents
        if not all([department_code, insee_code, zip_code, name, lat, lon]):
            conn.rollback()
            cur.close()
            conn.close()
            return jsonify({"error": "Missing fields in one of the records"}), 400

        # Insérer les données dans la base de données
        query = "INSERT INTO city (department_code, insee_code, zip_code, name, lat, lon) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
        values = (department_code, insee_code, zip_code, name, lat, lon)
        cur.execute(query, values)
        print("data inserted")

    # Commit la transaction
    conn.commit()

    # Fermer le curseur et la connexion
    cur.close()
    conn.close()
    print("database connection closed")

    # Retourner les données et le code de statut HTTP
    return jsonify({"message": "Cities added successfully"}), 201

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get('/city')
def city_get():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM city")
    cities = cur.fetchall()
    cities_json = json.dumps(cities)
    cur.close()

    return cities_json, 200


@app.route("/_health")
def health_check():
    try:
        conn = get_db_connection()
        conn.close()
        return "", 204
    except psycopg2.Error:
        return "", 500



@app.route('/metrics', methods=['GET'])
def get_data():
    """Returns all data as plaintext."""
    number_of_requests.inc()
    current_memory_usage.labels('server-a').set(random.randint(10000,90000))
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
