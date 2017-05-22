import hashlib
import sqlite3
import os
import random

def addCode(email, adminLevel):
    f = "../data/data.db"
    db = sqlite3.connect(f)
    gt = db.cursor()

    code=10*random.randint(1000000000,9999999999)+adminLevel
    print code
    while(badCode(code)):
        code=10*random.randint(1000000000,9999999999)+adminLevel

    insert="INSERT INTO accounts VALUES ('%s', '%s')"%(email, code)
    gt.execute(insert)
    db.commit()
    db.close()

def badCode(code):
    f = "../data/data.db"
    db = sqlite3.connect(f)
    gt = db.cursor()

    request="SELECT code from accounts"
    codes=gt.execute(request)
    for thing in codes:
        if thing[0]==codes:
            return false

    db.close()
    
    
def checkCode(email, code):
    L=[email, code]
    f = "../data/data.db"
    db = sqlite3.connect(f)
    gt = db.cursor()



addCode('lol')
print checkCode('lol', '8002752771')
