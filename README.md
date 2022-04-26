# Project informations

Name: New York Real Estate Backend <br />
Start date: 04/25/2022 <br />
Version: 001 <br />
Author's name: Rodrigo Wanderley <br />
E-mail: <boaventurarodrigo@yahoo.com.br> <br />
Git hub profile: <https://github.com/Rodrigowb> <br />
Linkedin profile: <https://www.linkedin.com/in/rodrigowanderleyboaventura> <br />

# Deployed project

# About the project

This project aims to build a Rest API to use as a backend, including data from New York City real estate prices.

# API endpoints

| Request | Endpoint | Description |
--- | --- | ---
GET | /apartments | Return all apartments from the db
POST | /apartments | Add a new apartment to the db
GET | /apartments/id/id | Return the specific apartment according to the id
PUT | /apartments/id/id | Update an apartment according to the id
DELETE | /apartments/id/id | Delete an apartment according to the id  

# Files description

| File | Description |
--- | --- | ---
db/database.py | Connect to the SQL Postgres database and create the models
seed/seed.py | Seed the database with initial information
server/server.py | Connect to the server using Flask and defining the API endpoints

# Technologies used

1. Python
2. SQL
3. Postgres
4. Peewee
5. Flask
6. Git