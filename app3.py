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
