import hashlib
import sqlite3
import os

def addentry(usern, email, advisor, advisorEmail):
	f = "data/data.db"
	db = sqlite3.connect(f)
  	sp = db.cursor()
  	insert = "INSERT INTO users VALUES ('%s', '%s', '%s', '%s')"%(usern, email, advisor, advisorEmail) 
	sp.execute(insert)
	db.commit()
	db.close()
  	return True

def getData(username):
	f = "data/data.db"
	db = sqlite3.connect(f)
	c = db.cursor()
	checkUser = "SELECT * FROM users WHERE usern==?"
	c.execute(checkUser, (username,))
	r = c.fetchone()
	db.commit()
	db.close()
	return r

def getName(username):
	return getdata(username)[0] 

def getEmail(username):
	return getdata(username)[1] 

def getAdvisor(username):
	return getdata(username)[2] 

def getAdvisorEmail(username):
	return getdata(username)[3] 
