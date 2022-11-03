# Clone repository
git clone https://github.com/academygit/flask-crud-postgres.git
cd flask-crud-postgres

# Create a new database and table and insert demo data
    CREATE DATABASE RESTAPIDEMO;

    CREATE TABLE person(
        id SERIAL PRIMARY KEY,
        username VARCHAR(255)
    );

    INSERT INTO person (username) VALUES ('Test User');

# Crete database.ini file to src/data/database.ini path.
    [postgresql]
    host=
    database=
    port=
    user=
    password=

# Open command prompt in VSCode editor

## Create python virtual environment
    python -m venv venv
    .\venv\Scripts\activate

## Install libraries
    pip install -r requirements.txt

## Start server
    cd src\data
    py person_api.py

