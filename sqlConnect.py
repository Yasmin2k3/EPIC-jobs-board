from fastapi import FastAPI, HTTPException, Request, status
import pymysql
from pydantic import BaseModel
from pymysql import MySQLError

import dbinfo

def get_connection():
    try:
        db = pymysql.connect(
            host="localhost",
            user=dbinfo.username,
            password=dbinfo.password,
            database = "epic"
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
def get_all_listing():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(f"select * from epic.listing")
    result = cursor.fetchall()
    return result

@app.get("/company")
def get_all_comapny():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(f"select * from epic.company")
    result = cursor.fetchall()
    return result

@app.get("/student")
def get_all_student():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(f"select * from epic.student")
    result = cursor.fetchall()
    return result





class Company(BaseModel):
    name: str
    email: str
    website_link: str = None

@app.post("/company",
          tags=["company APIs"])
def create_company(company: Company):
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO company (name, email, website_link) VALUES (%s, %s, %s)",
            (company.name, company.email, company.website_link)
        )
        db.commit()
        cursor.close()
        db.close()
        return {"message": "Company created"}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))

@app.put("/company/{id}",
         tags=["company APIs"])
def update_company(id: str, company: Company):
    db = get_connection()
    cursor = db.cursor()
    try:
        sql="""UPDATE company SET name = '%s', email='%s', website_link='%s' WHERE id = %s""" %(company.name, company.email, company.website_link, id)
        print(sql)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return {"message": "Company updated: "}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))







@app.post("/listing/")
def create_listing(listing, company):
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute(
            # TODO: Add ON DUPLICATE KEY UPDATE instead of IGNORE
            "SELECT * FROM company WHERE email",
            (company.name, company.email, company.website_link)
        )
        cursor.execute(
            # TODO: Add ON DUPLICATE KEY UPDATE instead of IGNORE
            "INSERT IGNORE INTO listing (first_name, last_name, score) VALUES (%s, %s, %s)",
            (listing.first_name, listing.last_name, listing.score)
        )
        db.commit()
        cursor.close()
        db.close()
        return {"message": "Listing created"}
    finally:
        cursor.close()
        db.close()
@app.delete("/listing")
def delete_listing(resNo, idCompany):
    try:
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM epic.listing WHERE residency_number = %s AND idCompany=%s", (resNo, idCompany))
        db.commit()
        deleted = cursor.rowcount
        cursor.close()
        db.close()

        if deleted == 0:
            raise HTTPException(status_code=404, detail="No listing found")
        return {"message": f"Deleted listing"}

    except pymysql.MySQLError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
