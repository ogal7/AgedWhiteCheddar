import sqlite3


def getRooms(club, date):
	f = "data/data.db"
	db = sqlite3.connect(f)
	og = db.cursor()

	request = "SELECT * from rooms WHERE club == '%s';" %(club)
    	info = og.execute(request)
    	li=[]
    	for thing in info:
       		li.append([thing[0],thing[1],thing[2]])
    	db.close()
    	return li