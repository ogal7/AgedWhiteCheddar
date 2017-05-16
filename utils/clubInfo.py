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
