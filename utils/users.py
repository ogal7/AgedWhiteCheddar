import hashlib
import sqlite3
import os
from accounts import whatLevel

def hashp(x):
	h = hashlib.sha256()
	h.update(x)
	return h.hexdigest()

def createAccount(usern, unhashedp, isAdmin):
	isAdmin = int(code[len(code)-1:len(code)])
	f = "../sdata/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()
	insert = "INSERT INTO users VALUES ('%s', '%s', '%d')"%(usern, hashp(unhashedp), isAdmin)
	print "yo yo yo"
	sp.execute(insert)
	db.commit()
	db.close()

def checkLogin(usern, pw):
	hashed = hashp(pw)
	f = "data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()
	s = "SELECT usern, pw FROM users WHERE usern =='" + usern + "';"
	t = sp.execute(s)
	for record in t:
		if record[1] == hashed:
			print "hi"
			db.close()
			return True	
		else:
			print "hello"
			db.close()
			return False
	print "hi"
	db.close()
	return False

def addClub(name, email, advisorName, advisorEmail):
	f = "../data/data.db"
	db = sqlite3.connect(f)
	c = db.cursor()
	query = "INSERT INTO clubs (name, email, advisor, advisorEmail) VALUES (?, ?, ?, ?)"
	c.execute(query, (name, email, advisorName, advisorEmail))
	c.close()
	db.commit()
	db.close()



def isStudent(code):
	if code[len(code)-1:len(code)]=='0':
		return True
	return False

