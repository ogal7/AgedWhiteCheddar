import hashlib
import sqlite3
import os

def addCode(email):
    f = "data/data.db"
    db = sqlite3.connect(f)
    og = db.cursor()

    request="SELECT code from accounts"
    codes=og.execute(request)
    code=os.random(32)
    while(code in codes):
        code=os.random(32)

    insert="INSERT INTO accounts VALUES ('%s', '%s')"%(email, code)
    og.execute(insert)
    db.commit()
    db.close()

def checkCode(email, code):
    L=[email, code]
    f = "data/data.db"
    db = sqlite3.connect(f)
    og = db.cursor()

    request="SELECT * from accounts"
    codes=og.execute(request)
    return (L in codes)
