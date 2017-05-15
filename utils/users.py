import hashlib
import sqlite3
import os

def hash(x):
	h = hashlib.sha256()
	h.update(x)
	return h.hexdigest()

def createAccount(usern, unhashedp, isAdmin):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	insert = "INSERT INTO users VALUES ('%s', '%s', '%d')"%(usern, hash(unhashedp), isAdmin)
	og.execute(insert)
	db.commit()
	db.close()

def checkLogin(usern, pw):
	hashed = hash(pw)
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



def checkRegister(usern):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
	s = "SELECT usern FROM users"
	t = og.execute(s)
	for record in t:
		if record[0] == usern:
			#username already taken
			return False 
	return True

