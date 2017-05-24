import hashlib
import sqlite3
import os
import time

#gets all the rooms, clubs, for a specific date
#date format: mmddyyyy
def getInfoDate(date):
    	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()

        request="SELECT * from rooms"+date[4:]+" WHERE date == "+date+";"
        info=og.execute(reqest)
        db.close()
        l=[]
        for thing in info:
                l.append(thing[0],thing[1],thing[2])
        return l

'''def getInfoRange(start, end):
    info=[]
    startN=int(start[
   ''' 
#gets all the rooms, clubs, for a specific date
#date format: mmddyyyy
def getInfoRoom(room):
    	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
        ## dd/mm/yyyy format
        date = (time.strftime("%d%m%Y"))
        request="SELECT * from rooms"+date[4:]+" WHERE room == "+room+";"
        info=og.execute(request)
        db.close()
        l=[]
        for thing in info:
                l.append(thing[0],thing[1],thing[2])
        return info

#gets all the rooms, clubs, for a specific date
#date format: mmddyyyy
def getInfoClub(clubName):
    	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
        date = (time.strftime("%d%m%Y"))
        request="SELECT * from rooms"+date[4:]+" WHERE clubName == "+clubName+";"
        info=og.execute(request)
        db.close()
        l=[]
        for thing in info:
                l.append(thing[0],thing[1],thing[2])
        return l
