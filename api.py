import psycopg2
import uvicorn
from fastapi import FastAPI


class DataB:

    @classmethod
    def connexion(cls):
        cls.host = 'database-1.cvuz5hbtumrs.us-east-2.rds.amazonaws.com'
        cls.port = 5432
        cls.user = 'postgres'
        cls.password = '**********'
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
    uvicorn.run(app,host='0.0.0.0',port=8081)

