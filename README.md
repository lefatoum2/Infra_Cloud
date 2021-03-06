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




class DataB:

    @classmethod
    def connexion(cls):
        cls.host = 'database-1.cvuz5hbtumrs.us-east-2.rds.amazonaws.com'
        cls.port = 5432
        cls.user = 'postgres'
        cls.password = '******'
        cls.database = 'exercises'
        cls.con = psycopg2.connect(host=cls.host, port=5432, user=cls.user, password=cls.password,
                                   database=cls.database)
        cls.cur = cls.con.cursor()
        cls.con.autocommit = True

    @classmethod
    def disconnect(cls):
        cls.cur.close()
        cls.con.close()

    @classmethod
    def facilities(cls):
        DataB.connexion()
        sql = 'select * from cd.facilities'
        cls.cur.execute(sql)
        res = cls.cur.fetchall()
        return res

    @classmethod
    def costname(cls):
        DataB.connexion()
        sql = 'select name,membercost from cd.facilities'
        cls.cur.execute(sql)
        res = cls.cur.fetchall()
        return res


app = FastAPI(redoc_url=None)


@app.get("/facilities")
async def facilities():
    data = DataB.facilities()
    return data


@app.get("/costname")
async def costname():
    data = DataB.costname()
    return data


if __name__ == "__main__":
    uvicorn.run(app,host='0.0.0.0', port=8081)


```

## Connexion à l'instance EC2 créée

### Télécharger PuttyGen ,  Putty et WinScp

https://www.puttygen.com/download-putty

https://winscp.net/eng/download.php

Winscp permettra de gérer les fichiers et dossiers entre votre machine local et votre instance EC2.
Il faudra juste vous munir de la DNS public de votre EC2(ubuntu@ec2-3-15-193-106.us-east-2.compute.amazonaws.com), de la clé générée avec PuttyGen et votre nom utilisateur(pour moi , c'est ubuntu)

![title1a](./infra_cloud_images/winscp.png)

### Configuration de PuttyGen

![title1](./infra_cloud_images/puttygen.png)

Chargez la clé paire (.pem) que vous avez généré par l'instance EC2 et enregistré sur votre machine local.(Pour moi , c'est "my_key_pair.pem").
Ensuite générez votre propre clé et sauvegardez là pour l'utiliser dans l'outil Winscp.
![title2](./infra_cloud_images/keypem.png)

### Configuration de Putty
![title2a](./infra_cloud_images/instance.png)
Entrez à nouveau votre DNS public propre à l'instance.
![title3](./infra_cloud_images/putty.png)
Ensuite pour l'authentification(->Auth), chargez la clé générée par PuttyGen
![title4](./infra_cloud_images/keypem2.png)

### Autre type de connection

```
ssh -i "file.pem" <>@<DNS IPv4 public>
```

```
ssh -i "my_key_pair.pem" ubuntu@ec2-3-15-193-106.us-east-2.compute.amazonaws.com

```

### Configuration du groupe de sécurité
![title5](./infra_cloud_images/groupsecurity1.png)
![title6](./infra_cloud_images/groupsecurity2.png)
![title7](./infra_cloud_images/groupsecurity3.png)


### Terminal 
Le terminal est lancé. Entrez votre nom utilisateur(pour moi , c'est ubuntu). 
![title8](infra_cloud_images/terminal1.png)

N'oubliez pas de télécharger les modules nécessaires fournis dans requirements.txt:

```
pip3 freeze > requirements.txt fastapi uvicorn psycopg2-binary
```

```
pip3 install -r requirements.txt
```

Pour lancer l'application:
```
python3 api.py
```
### Sources

https://www.youtube.com/watch?v=oOqqwYI60FI
