import pandas as pd
import pymysql

# read by default 1st sheet of an excel file
df = pd.read_excel("C:\\Users\\yasmi\\Documents\\student list.xlsx")
#
# df[['first_name', 'last_name']] = df['Unnamed: 0'].str.strip().str.split(n=1, expand=True)
# df['score'] = df.index + 1

def get_connection():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="epic"
    )
    return db

mydb = get_connection()
cursor = mydb.cursor()

cursor.execute("select id, available_places from listing")
result = cursor.fetchall()
print(result)

#mydb.commit()
cursor.close()
mydb.close()

print("done!")