import sqlite3
import time
import datetime

def getRoomsNow(club):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()

	request = "SELECT * from rooms WHERE club = ?"
    	info = og.execute(request, (club,))
    	li = []

        d = time.strftime("%d/%m/%Y").split("/")

    	for rooms in info:
                if datetime.date(int(d[2]), int(d[1]), int(d[0])) <= datetime.date(rooms[4], rooms[2], rooms[3]):
                        li.append([rooms[0], rooms[1], rooms[2], rooms[3], rooms[4]])

        og.close()
        db.commit()
    	db.close()
    	return li

def getPreviousRooms(club):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()

	request = "SELECT * from rooms WHERE club = ?"
    	info = og.execute(request, (club,))
    	li = []

        d = time.strftime("%d/%m/%Y").split("/")

    	for rooms in info:
                if datetime.date(int(d[2]), int(d[1]), int(d[0])) > datetime.date(rooms[4], rooms[2], rooms[3]):
                        li.append([rooms[0], rooms[1], rooms[2], rooms[3], rooms[4]])

        og.close()
        db.commit()
    	db.close()
    	return li

def getBlockedRooms():
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
        date = time.strftime("%d%m%Y")
        club = "Not Available"
        request = "SELECT * from rooms WHERE club = ? and year >= ?"
        info = og.execute(request, (club,date[4:]))

        blocked_rooms = []
        for room in info:
            # print room
            if room[2]>=int(date[:2]) or (room[4]>int(date[4:]) and room[2]<int(date[:2])):
                blocked_rooms.append([room[0],room[1],room[2], room[3], room[4]])

        og.close()
        db.commit()
        db.close()
        return blocked_rooms
