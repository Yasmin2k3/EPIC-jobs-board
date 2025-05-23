from fastapi import FastAPI
import pymysql

import dbinfo

mydb = pymysql.connect(
    host="localhost",
    user=dbinfo.username,
    password=dbinfo.password
)

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
    mycursor.execute("""select * from """ + dbinfo.dbName + """.in_agreement limit 2""")
    myresult = mycursor.fetchall()
    return myresult