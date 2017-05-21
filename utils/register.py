import hashlib
import sqlite3
import os
import random

def addCode(email):
    f = "../data/data.db"
    db = sqlite3.connect(f)
    og = db.cursor()

    code=random.randint(1000000000,9999999999)
    print code
    while(badCode(code)):
        code=random.randint(1000000000,9999999999)

    insert="INSERT INTO accounts VALUES ('%s', '%s')"%(email, code)
    og.execute(insert)
    db.commit()
    db.close()

def badCode(code):
    f = "../data/data.db"
    db = sqlite3.connect(f)
    og = db.cursor()

    request="SELECT code from accounts"
    codes=og.execute(request)
    for thing in codes:
        if thing[0]==codes:
            return false

    db.close()
    
    
def checkCode(email, code):
    L=[email, code]
    f = "../data/data.db"
    db = sqlite3.connect(f)
    og = db.cursor()

    request="SELECT * from accounts"
    codes=og.execute(request)
    for things in codes:
        if((email, code) == things):
            return True

addCode('lol')
print checkCode('lol', '8002752771')
