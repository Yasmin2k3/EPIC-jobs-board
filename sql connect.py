from fastapi import FastAPI
import pymysql

#user is whatever username u set up and password is whatever password we set up
mydb = pymysql.connect(
    host="localhost",
    user="xxx",
    password="xxx"
)

app = FastAPI()

mycursor = mydb.cursor()

@app.get("/")
def read_root():
    return {"msg": "Server is running"}

@app.get("/mysql")
def read_mysql():
    mycursor.execute("""select * from db.table""")
    myresult = mycursor.fetchall()
    return myresult
