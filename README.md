# Infra_Cloud

## Installation  EB CLI

```
pip install awsebcli --upgrade --user

```
## Version EB CLI

```
eb --version
```

## Docker-compose.yml après la création de la base de données postgres sur RDS 

```
version: '3.1'
services:
  db:
    image: postgres
    container_name: postgres_db
    restart: always
    environment:
      POSTGRES_USER: root
      POSTGRES_PASSWORD: root
    volumes:
      - ./data:/var/lib/postgresql/data
    ports:
      - 5432:5432
      
  pgadmin:
    image: dpage/pgadmin4
    container_name: postgres_admin
    links:
      - db
    depends_on:
      - db
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: pwdpwd
    volumes:
      - ./pgadmin:/var/lib/pgadmin
    ports:
      - 8080:80

```

## Lancer docker-compose.yml

```
docker compose -d up
```

## Connection à la base de données AWS-RDS

``` Python
import psycopg2
import pandas as pd
import streamlit as st

connection = psycopg2.connect(
    host='database-1.cvuz5hbtumrs.us-east-2.rds.amazonaws.com',
    port=5432,
    user='postgres',
    password='********',
    database='exercises'
)

cursor = connection.cursor()
sql = 'select * from cd.members'
res = cursor.execute(sql)

df = pd.read_sql(sql, con=connection)
st.title("Une infra dans le Cloud")
st.dataframe(df)


# print(type(res))
#connection.commit()



```
## API

```Python
import psycopg2
import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

import pymysql
import mysql.connector as mysqlpyth


class DataB:

    @classmethod
    def connexion_(cls):
        cls.host = 'database-1.cvuz5hbtumrs.us-east-2.rds.amazonaws.com'
        cls.port = 5432
        cls.user = 'postgres'
        cls.password = '*******'
        cls.database = 'exercises'
        cls.con = psycopg2.connect(host=cls.host, port=5432, user=cls.user, password=cls.password,
                                   database=cls.database)
        cls.cur = cls.con.cursor()

    @classmethod
    def disconnect(cls):
        cls.con.commit()
        cls.con.close()
        cls.cur.close()

    @classmethod
    def send1(cls, sql):
        cls.cur.execute(sql)

    @classmethod
    def facilities(cls):
        sql = ''
        cls.cur.execute(sql)

    @classmethod
    def costname(cls):
        sql = ''
        cls.cur.execute(sql)


app = FastAPI(redoc_url=None)


@app.get("/facilities")
async def facilities():
    DataB.connexion()
    data = DataB.facilities()
    return data


@app.get("/costname")
async def costname():
    DataB.connexion()
    data = DataB.costname()
    return data


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)

```
