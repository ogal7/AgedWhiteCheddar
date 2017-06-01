import sqlite3


def getRooms(date):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()

	request = "SELECT * from rooms"+date[4:]+" WHERE date == '%s';" %(date)
    	info = og.execute(request)
    	li=[]
    	for thing in info:
       		li.append([thing[0],thing[1],thing[2]])
    	db.close()
    	return li