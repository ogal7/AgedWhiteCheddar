import sqlite3


def getRooms(date):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()

	request = "SELECT * from rooms WHERE day == %s and month == %s and year == %s;" %(date[2:4],date[:2],date[4:])
    	info = og.execute(request)
    	li=[]
    	for thing in info:
       		li.append([thing[0],thing[1],thing[2]])
    	db.close()
    	return li
