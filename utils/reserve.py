import sqlite3
#date format: mmddyyyy

def reserve_room(room, date, clubName):
    f = "data.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    check = "SELECT clubName FROM rooms2017 WHERE  room = ? AND date = ?"
    auth = c.execute(check, (room, date)).fetchone()
    if auth is None and auth[0] != "N/A":
    	add_reservation = "INSERT INTO rooms2017 (room, date, clubName) VALUES(?, ?, ?)"
    	c.execute(add_reservation, (room, date, clubName))
    	print "room reserved" + room + " for " + date + " by " + clubName
    	c.close()
    	db.commit()
    	db.close()
    	return True
    c.close()
    db.commit()
    db.close()
    print "Failed to Reserve" 
    return False

# can unreserve if the club that reserved the room
def unreserve_room_club(room, date, clubName):
    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    unreserve = "DELETE FROM rooms2017 WHERE room = ? and date = ?"
    c.execute(unreserve, (room, date))

    c.close()

    db.commit()
    db.close()

# if room is being blocked, kick out people who already made a reservation
# prevent clubs from reserving room again
def block_room(room, date):
    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    kick_out_reserved = "DELETE FROM rooms2017 WHERE room = ? and date = ?"
    c.execute(kick_out_reserved, (room, date))

    block_reservation = "INSERT INTO rooms2017 (room, date, clubName) VALUES(?, ?, ?)"
    c.execute(block_reservation, (room, date, "N/A"))

    c.close()
    db.commit()
    db.close()
