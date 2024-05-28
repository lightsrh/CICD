#!/bin/bash
source .env

#créer .pgpass
echo "$CITY_API_ADDR:$CITY_API_PORT:$CITY_API_DB_URL:$CITY_API_DB_USER:$CITY_API_DB_PWD" > ~/.pgpass
chmod 600 ~/.pgpass
cat ~/.pgpass

docker compose down --remove-orphans
docker compose up -d

#attendre que le container soit prêt
sleep 5

psql -h $CITY_API_ADDR -U $POSTGRES_USER -d $POSTGRES_DB -p $POSTGRES_PORT -f $(pwd)/dataset/init.sql

#start init_db.py
python3 init_db.py