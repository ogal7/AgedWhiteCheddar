import sqlite3
import os
import hashlib 
import random 

def createAvailableAccount(email, isAdmin): 
	f = "../data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()
	code = generateCode(isAdmin)
	while (codeCheck(code)):
		code - generateCode(isAdmin)
	insert = "INSERT INTO accounts VALUES ('%s', '%s')"%(email, code)
	sp.execute(insert)
	db.commit()
	db.close()

def generateCode(isAdmin):
	return str(int(random.random()*10000)) + str(isAdmin)

def whatLevel(email): 
	f = "../data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()
	s = "SELECT code FROM accounts WHERE email=='" + email + "';"
	t = sp.execute(s)
	res = t.fetchall()
	db.commit()
	db.close()
	return res[0][-1]

def codeCheck(code):
    f = "../data/data.db"
    db = sqlite3.connect(f)
    gt = db.cursor()
    request="SELECT code FROM accounts" + ";"
    codes=gt.execute(request)
    for thing in codes:
        if thing[0]==codes:
            return False
    db.commit()
    db.close()
    
def checkRegister(email, code):
	f = "../data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()
	s = "SELECT email, code FROM accounts WHERE email == '" + email + "' AND code =='" + code + "';"
	t = sp.execute(s)
	res = t.fetchall()[0]
	if len(res) == 0:
				db.commit()
				db.close()
				return False 
   	db.commit()
	db.close()
	return True
    