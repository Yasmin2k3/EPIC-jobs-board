from fastapi import FastAPI
import pymysql
from pymysql import MySQLError

import dbinfo

def get_connection():
    try:
        db = pymysql.connect(
            host="localhost",
            user=dbinfo.username,
            password=dbinfo.password
        )
        print("Database successfully connected.")
        return db
    except MySQLError as e:
        print(f"Error connecting to MySQL database: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Server is running"}

@app.get("/listing")
def read_mysql():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(f"select * from epic.listing")
    result = cursor.fetchall()
    return result

@app.post("/listing/")
def create_listing(listing, company):
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(
            # TODO: Add ON DUPLICATE KEY UPDATE instead of IGNORE
            "INSERT IGNORE INTO company (name, email, website_link) VALUES (%s, %s, %s)",
            (company.name, company.email, company.website_link)
        )
        cursor.execute(
            #TODO: Add ON DUPLICATE KEY UPDATE instead of IGNORE
            "INSERT IGNORE INTO listing (first_name, last_name, score) VALUES (%s, %s, %s)",
            (listing.first_name, listing.last_name, listing.score)
        )
        db.commit()
        return {"message": "Student created"}
    finally:
        cursor.close()
        db.close()
