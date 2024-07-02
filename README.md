# CI/CD Project

This project aims to create a CI/CD pipeline for a web service that manages a database of cities. The project includes setting up a Postgres database, creating a Flask web service, writing tests, building Docker images, and deploying the application using Helm on k3s. The full code and detailed report are available at the [GitHub repository](https://github.com/lightsrh/CICD).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [CI/CD](#cicd)
- [Prerequisites](#prerequisites)
- [Questions](#questions)

## Installation

Create a virtual environment, activate it, and install the requirements:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Initialize the Database

To initialize the database, run the following script:

```bash
./init.sh
```

## Usage

To run the app:

```bash
python3 app/__main__.py
```

You can then go to <http://127.0.0.1:2022> and start playing (you will see the results of the endpoints in the vscode console or if you are using a software like Postman or APIDog)

## Contributing

- Sarah THEOULLE
- Giada Flora DE MARTINO
- Benoît PLANCHE

## CI/CD

A detailed report of the actions performed is expected. A link to a GitHub repository should be included.

## Prerequisites

- Docker
- Docker Compose

## Questions

### 1) Create a `docker-compose.yml` file and add a `db` service using the `postgres:latest` Docker image

### 2) Create a `city_api` database with a `city` table containing the following columns

- `id`: an unsigned integer, primary key;
- `department_code`: a non-null string;
- `insee_code`: a string;
- `zip_code`: a string;
- `name`: a non-null string;
- `lat`: a non-null float;
- `lon`: a non-null float.

### 3) Create a web service with the following specifications

- `POST /city` with a JSON body should return a `201` status code and save the city in the database.
- `GET /city` should return a `200` status code with the list of cities in JSON format.
- `GET /_health` should return a `204` status code.

### 4) Write the following tests

- A test to ensure that the insertion into the database works correctly.
- A test to ensure that retrieving the list of cities works correctly.
- A test to ensure that the health check endpoint works correctly.

### 5) Write a `Dockerfile` at the root of your project. Test that your Docker image is correct

### 6) Write a GitHub Actions workflow `ci` to run a linter on each push

### 7) Modify the workflow to run tests on each push

### 8) Modify the workflow to build the Docker image on each push

### 9) Modify the workflow to push the Docker image to DockerHub with the tag `city-api:latest`

### 10) Write a GitHub Actions `release` workflow to build and push the Docker image with a tag `city-api:X.X.X` when a `vX.X.X` tag is pushed

### 11) Modify the workflow to scan for CVEs in your Docker image

### 12) Install k3s on your local machine

### 13) Write a Helm chart to deploy the application. (not done)

### 14) Deploy your application in your k3s cluster. (not done)

### 15) Add a `/metrics` endpoint compatible with Prometheus

### 16) Add Prometheus to your `docker-compose` to scrape metrics from your application

### 17) Add Grafana to your `docker-compose` and create a dashboard to monitor your application. (not done)
