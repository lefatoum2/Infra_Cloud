# Infra_Cloud

## Installation  EB CLI

```
pip install awsebcli --upgrade --user

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
