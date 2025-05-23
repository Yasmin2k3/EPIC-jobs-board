from fastapi import FastAPI
import pymysql
from pymysql import MySQLError

import dbinfo

try:
    mydb = pymysql.connect(
        host="localhost",
        user=dbinfo.username,
        password=dbinfo.password
    )
    print("Database successfully connected.")
except MySQLError as e:
    print(f"Error connecting to MySQL database: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

app = FastAPI()

mycursor = mydb.cursor()

@app.get("/")
def read_root():
    return {"msg": "Server is running"}

@app.get("/yaz")
def read_root2():
    return {"Hello": "Yaz"}

@app.get("/jpw")
def read_root3():
    return {"Hello": "boo"}

@app.get("/mysql")
def read_mysql():
    mycursor.execute(f"select * from {dbinfo.dbName}.{dbinfo.tableName}")
    myresult = mycursor.fetchall()
    return myresult
