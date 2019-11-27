from model import *
import mysql.connector


def databaseInit():
    db = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="root",
      database="sys"
    )
    cursor = db.cursor()
    return db,cursor

def readBreedDB(Id):
    db,cursor=databaseInit()
    if Id != "ALL":
         Id=int(Id)
         cursor.execute(f"SELECT * FROM BREED where id={Id}")
    else: cursor.execute(f"SELECT * FROM BREED")
    return cursor.fetchall()


def readPupperDB(Id):
    db,cursor=databaseInit()
    # result = ""
    if Id != "ALL":
        Id=int(Id)
        cursor.execute(f"select * from PUPPER as p inner join BREED as b on p.breed_id=b.id where b.id={Id}")
    else: cursor.execute(f"SELECT * FROM PUPPER")
    return cursor.fetchall()

def writeDB(rowobject,tablename):
    db,cursor=databaseInit()
    if tablename == "BREED":
        sql = "INSERT INTO  breed (name, temperament, coat) VALUES (%s, %s , %s)"
        val = (rowobject.name,rowobject.temperaament,rowobject.coat)
    elif tablename == "PUPPER":
        sql = "INSERT INTO  PUPPER (name, sex, weight, height, color, date_of_birth, breed_id) VALUES (%s, %s,%s,%s,%s ,%s,%s)"
        val = (rowobject.name, rowobject.sex, rowobject.weight,rowobject.height,rowobject.color,rowobject.date_of_birth,rowobject.breed_id)

    cursor.execute(sql, val)

    db.commit()
    print(cursor.rowcount, "record inserted.")


def deletePupperDB(Id):
    db, cursor = databaseInit()
    sql = f"DELETE FROM  PUPPER  WHERE  id={Id}"
    cursor.execute(sql)

    db.commit()
    print(cursor.rowcount, "record(s) deleted.")

