import hashlib
import sqlite3
import os

def addClub(name, email, advisorName, advisorEmail):
        f = "data/data.db"
	db = sqlite3.connect(f)
	c = db.cursor()

	query = "INSERT INTO clubs (name, email, advisor, advisorEmail) VALUES (?, ?, ?, ?)"
	c.execute(query, (name, email, advisorName, advisorEmail))

	c.close()
	db.commit()
	db.close()

def getClub(username):
	f = "data/data.db"
	db = sqlite3.connect(f)
	c = db.cursor()

	checkUser = "SELECT * FROM users WHERE usern = ?"
	c.execute(checkUser, (username,))

	r = c.fetchone()

	db.commit()
	db.close()

	return r

def getClubName(username):
	return getClub(username)[0]

def getClubEmail(username):
	return getClub(username)[1]

def getAdvisor(username):
	return getClub(username)[2]

def getAdvisorEmail(username):
	return getClub(username)[3]
