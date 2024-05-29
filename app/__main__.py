import os
from dotenv import load_dotenv
from app import app

if __name__ == "__main__":
    load_dotenv()
    print(f"City API running on {os.getenv('CITY_API_ADDR')}:{os.getenv('CITY_API_PORT')}")
    app.run(host=os.getenv("CITY_API_ADDR"), port=os.getenv("CITY_API_PORT"), debug=True)