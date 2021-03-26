# Infra_Cloud

## Installation  EB CLI

```
pip install awsebcli --upgrade --user

```

## Docker-compse après la création de la base de données postgres sur RDS 

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
## Version EB CLI

```
eb --version
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
