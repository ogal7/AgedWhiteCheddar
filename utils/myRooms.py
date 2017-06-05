import sqlite3

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
