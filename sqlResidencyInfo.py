#from fastapi import FastAPI, HTTPException, Request, status
import pymysql
#from pydantic import BaseModel
from pymysql import MySQLError
import residencyAlgorithm
#import dbinfo

def get_connection():
    try:
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="mysql",
            database = "epicdb"
        )
        print("Database successfully connected.")
        return mydb
    except MySQLError as e:
        print(f"Error connecting to MySQL database: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

mydb = get_connection()
cursor = mydb.cursor()

cursor.execute("select id, company_id, available_places from listing")
listingTupple = cursor.fetchall()
print(listingTupple)
listingIDs=list(map(lambda x:x[0], listingTupple))
companyIDs=list(map(lambda x:x[1], listingTupple))
placesList=list(map(lambda x:x[2], listingTupple))

cursor.execute("select id, name from company")
nameinfo=cursor.fetchall()
companyNames=[]
companyNames.append(list(map(lambda x:x[0], nameinfo)))
companyNames.append(list(map(lambda x:x[1], nameinfo)))
print(companyNames)

cursor.execute("select * from student")
studentTupple = cursor.fetchall()
studentIDS = list(map(lambda x:x[0],studentTupple))
studentFirstNames = list(map(lambda x:x[1],studentTupple))

cursor.execute("select * from residency_ranking")
result=cursor.fetchall()
residencyInput =[]
for x in range(len(result)):
    residencyInput.append(list(result[x][1:5]))
    #convert the listing id to company id
    listing_id = residencyInput[x][1]
    #uncomment below if you want to return based on residencyID rather than listing ID
    #studentList[x][1]=companyIDs[listingIDs.index(listing_id)]
    pass

residencyInput.sort()

residencyPairings = residencyAlgorithm.calculateResidencies(residencyInput, studentIDS, listingIDs, placesList)

for x in residencyPairings :
    listingToCompanyID = companyIDs[listingIDs.index(x[1])]
    #print(listingToCompanyID)
    print(studentFirstNames[studentIDS.index(x[0])] + " is paired with " + companyNames[1][companyNames[0].index(listingToCompanyID)])

cursor.close()
mydb.close()