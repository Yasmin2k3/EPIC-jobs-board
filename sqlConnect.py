from fastapi import FastAPI, HTTPException, Request, status
import pymysql
from pydantic import BaseModel
from pymysql import MySQLError

import dbinfo

def get_connection():
    try:
        mydb = pymysql.connect(
            host="localhost",
            user=dbinfo.username,
            password=dbinfo.password,
            database = "epic"
        )
        print("Database successfully connected.")
        return mydb
    except MySQLError as e:
        print(f"Error connecting to MySQL database: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


app = FastAPI()
db = get_connection()
cursor = db.cursor()

@app.get("/")
def read_root():
    return {"msg": "Server is running"}

@app.get("/student",
         tags=["student APIs"])
def get_all_student():
    try:
        cursor.execute(f"select * from student")
        result = cursor.fetchall()
        return result
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))

@app.get("/student/{id}",
         tags=["student APIs"])
def get_student(id: int):
    try:
        cursor.execute(f"select * from student WHERE id=%s", (id,))
        result = cursor.fetchone()
        return result
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))


class Company(BaseModel):
    name: str
    email: str
    website_link: str = None

class CompanyUpdate(BaseModel):
    name: str=None
    email: str=None
    website_link: str = None

@app.get("/company",
         tags=["company APIs"])
def get_all_company():
    try:
        cursor.execute(f"select * from company")
        result = cursor.fetchall()
        return result
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))

@app.get("/company/{id}",
         tags=["company APIs"])
def get_company(id: int):
    try:
        cursor.execute(f"select * from company WHERE id=%s", (id,))
        result = cursor.fetchall()
        return result
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))

@app.post("/company",
          tags=["company APIs"])
def create_company(company: Company):
    try:
        cursor.execute(
            "INSERT INTO company (name, email, website_link) VALUES (%s, %s, %s)",
            (company.name, company.email, company.website_link)
        )
        db.commit()
        return {"message": "Company created"}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))

@app.put("/company/{id}",
         tags=["company APIs"])
def update_company(id: str, company: CompanyUpdate):
    try:
        sql="""UPDATE company SET name = '%s', email='%s', website_link='%s' WHERE id = %s""" %(company.name, company.email, company.website_link, id)
        cursor.execute(sql)
        db.commit()
        return {"message": "Company updated: "}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))

@app.delete("/company",
            tags=["company APIs"])
def delete_listing(id: int):
    try:
        cursor.execute("DELETE FROM company WHERE id = %s", (id,))
        db.commit()
        deleted = cursor.rowcount
        if deleted == 0:
            raise HTTPException(status_code=404, detail="No company found")
        return {"message": f"Deleted company"}
    except pymysql.MySQLError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

class Listing(BaseModel):
    job_title: str
    description: str
    available_places: int
    residency_number: str
    accommodation_support: str = None
    work_mode: str=None

class ListingUpdate(BaseModel):
    job_title: str=None
    description: str=None
    available_places: int=None
    residency_number: str=None
    accommodation_support: str = None
    work_mode: str = None

@app.get("/listing",
         tags=["listing APIs"])
def get_all_listing():
    cursor.execute(f"select * from listing")
    result = cursor.fetchall()
    return result

@app.get("/listing/{id}",
         tags=["listing APIs"])
def get_listing(id: int):
    cursor.execute(f"select * from listing WHERE id=%s", (id,))
    result = cursor.fetchone()
    return result

@app.post("/listing/{company_id}",
          tags=["listing APIs"])
def create_listing(company_id: int, listing: Listing):
    try:
        cursor.execute(
            """INSERT INTO listing (job_title, description, available_places, residency_number, accommodation_support, work_mode, company_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (listing.job_title, listing.description, listing.available_places, listing.residency_number, listing.accommodation_support, listing.work_mode,
             company_id)
        )
        db.commit()
        return {"message": "Listing created"}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))

#TODO: fix
@app.put("/listing/{company_id}",
          tags=["listing APIs"])
def update_listing(id: int, listing: ListingUpdate):
    try:
        sql=("""UPDATE listing SET job_title='%s', description='%s', available_places=%s, residency_number='%s', 
            accommodation_support='%s', work_mode='%s' WHERE id=%s"""
             %(listing.job_title, listing.description, listing.available_places, listing.residency_number, listing.accommodation_support, listing.work_mode, id))
        cursor.execute(sql)
        db.commit()
        return {"message": "Listing updated"}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))

@app.delete("/listing",
            tags=["listing APIs"])
def delete_listing(id: int):
    try:
        cursor.execute("DELETE FROM listing WHERE id = %s", (id,))
        db.commit()
        deleted = cursor.rowcount
        if deleted == 0:
            raise HTTPException(status_code=404, detail="No listing found")
        return {"message": f"Deleted listing"}
    except pymysql.MySQLError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

class ResidencyRanking(BaseModel):
    student_ranking: int =None
    company_ranking: int=None

@app.get("/residency_ranking",
         tags=["residency ranking APIs"])
def get_all_residency_rankings():
    cursor.execute("select * from residency_ranking")
    result = cursor.fetchall()
    return result

@app.get("/residency_ranking/{id}",
         tags=["residency ranking APIs"])
def get_residency_ranking(id: int):
    cursor.execute("select * from residency_ranking WHERE id=%s", (id,))
    result = cursor.fetchone()
    return result

@app.post("/residency_ranking/",
          tags=["residency ranking APIs"])
def create_residency_ranking(student_id: int, company_id: int, residencyRanking: ResidencyRanking):
    try:
        cursor.execute(
            """INSERT INTO residency_ranking (student_id, company_id, student_ranking, company_ranking)
            VALUES (%s, %s, %s, %s)""",
            (student_id, company_id, residencyRanking.student_ranking, residencyRanking.company_ranking)
        )
        db.commit()
        return {"message": "Residency ranking created"}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))

@app.delete("/residency_ranking/",
          tags=["residency ranking APIs"])
def delete_residency_ranking(id: int):
    try:
        cursor.execute(
            """DELETE FROM residency_ranking
            WHERE id=%s""",
            (id,))
        db.commit()
        return {"message": "Residency ranking deleted"}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))
