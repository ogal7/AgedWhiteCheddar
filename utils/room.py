import hashlib
import sqlite3
import os
import time

#gets all the rooms, clubs, for a specific date
#date format: mmddyyyy
def getInfoDate(date):
    f = "data.db"
    db = sqlite3.connect(f)
    og = db.cursor()
    request="SELECT room, club from rooms WHERE month = ? and day = ? and year = ?;"
    info = og.execute(request, (int(date[0:2]), int(date[2:4]), int(date[4:])))
    l=[]
    for thing in info:
        print thing[0]
        print thing[1]
    db.close()
    return l

'''def getInfoRange(start, end):
    info=[]
    startN=int(start[
   ''' 
#gets all the rooms, clubs, for a specific date
#date format: mmddyyyy
def getInfoRoom(room):
    f = "data.db"
    db = sqlite3.connect(f)
    og = db.cursor()
    ## dd/mm/yyyy format
    date = (time.strftime("%d%m%Y"))
    request="SELECT * from rooms WHERE day = ? and month = ? and year = ? and room = ?;"
    info=og.execute(request, (int(date[2:4]), int(date[:2]), int(date[4:]), room))
    
    de()
    l=[]
    for thing in info:
        print thing
    return info

#gets all the rooms, clubs, for a specific date
#date format: mmddyyyy
def getInfoClub(clubName):
    f = "data.db"
    db = sqlite3.connect(f)
    og = db.cursor()
    date = (time.strftime("%d%m%Y"))
    request="SELECT * from rooms WHERE day = ? and month = ? and year = ? and clubName = ?;"
    info=og.execute(request, (int(date[2:4]), int(date[:2]), int(date[4:]), clubName))
    db.close()
    l=[]
    for thing in info:
        l.append(thing[0],thing[1],thing[2])
    return l
