#!/bin/bash
source .env

echo "POSTGRES_HOST: $POSTGRES_HOST, POSTGRES_PORT: $POSTGRES_PORT, POSTGRES_DB: $POSTGRES_DB, POSTGRES_USER: $POSTGRES_USER, POSTGRES_PASSWORD: $POSTGRES_PASSWORD"
#créer .pgpass
echo "$POSTGRES_HOST:$POSTGRES_PORT:$POSTGRES_DB:$POSTGRES_USER:$POSTGRES_PASSWORD" > ~/.pgpass
chmod 600 ~/.pgpass
cat ~/.pgpass

# docker compose down --remove-orphans
# docker compose up -d


#attendre que le container soit prêt
sleep 5

#start init_db.py
python3 init_db.py

