CREATE SEQUENCE city_id_seq;

CREATE TABLE city (
    id SERIAL PRIMARY KEY,
    department_code VARCHAR(255) NOT NULL,
    insee_code VARCHAR(255),
    zip_code VARCHAR(255),
    name VARCHAR(255) NOT NULL,
    lat FLOAT NOT NULL,
    lon FLOAT NOT NULL
);
