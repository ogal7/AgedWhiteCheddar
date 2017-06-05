import sqlite3
import time

def getRooms(club):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()

	request = "SELECT * from rooms WHERE club == '%s';" %(club)
    	info = og.execute(request)
    	li=[]
    	for thing in info:
       		li.append([thing[0],thing[1],thing[2], thing[3], thing[4]])
                #print thing[0]
                #print thing[1]
                #print thing[2]
                #print thing[3]
                #print thing[4]


    	db.close()
    	return li

def getBlockedRooms():
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()
        date = time.strftime("%d%m%Y")
        club = "N/A"
        request = "SELECT * from rooms WHERE club = ? and year >= ?"
        info = og.execute(request, (club,date[4:]))

        blocked_rooms = []
        for room in info:
            # print room
            if room[2]>=int(date[:2]) or (room[4]>int(date[4:]) and room[2]<int(date[:2])):
                blocked_rooms.append([room[0],room[1],room[2], room[3], room[4]])

        db.close()
        return blocked_rooms
