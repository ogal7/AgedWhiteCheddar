import sqlite3
import os
import hashlib 
def createAvailableAccount(usern, isAdmin): 
	f = "data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()
	code = str(int(random.random()*10000)) + str(isAdmin)
	insert = "INSERT INTO users VALUES ('%s', '%s')"%(usern, code)
	sp.execute(insert)
	db.commit()
	db.close()

def whatLevel(usern): 
	f = "data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()
	s = "SELECT code FROM accounts WHERE usern=='" + usern + "';"
	t = sp.execute(s)
	db.commit()
	db.close()
	return t.fetchall()[0][-1]