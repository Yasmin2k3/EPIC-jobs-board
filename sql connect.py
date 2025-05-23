from fastapi import FastAPI
import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="xxx",
    password="xxx"
)

app = FastAPI()

mycursor = mydb.cursor()

@app.get("/")
def read_root():
    return {"msg": "Serveaaaaar is running"}

@app.get("/yaz")
def read_root2():
    return {"Hello": "Yaz"}

@app.get("/jpw")
def read_root3():
    return {"Hello": "boo"}

@app.get("/mysql")
def read_mysql():
    mycursor.execute("""select * from db.table""")
    myresult = mycursor.fetchall()
    return myresult