import sqlite3
import time
#date format: mmddyyyy

def reserve_room(room, date, clubName):
    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    t=time.strftime("%Y")
    check = "SELECT club FROM rooms WHERE  room = ? AND month = ? and day = ? and year = ?"
    auth = c.execute(check, (room, int(date[0:2]) + 1, int(date[2:4]), int(date[4:]))).fetchone()
    print auth
    if auth is None:
        add_reservation = "INSERT INTO rooms (room, club, month, day, year) VALUES(?, ?, ?, ?, ?) "
        c.execute(add_reservation, (room, clubName, int(date[0:2]) + 1 , int(date[2:4]), int(date[4:])))
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
    unreserve = "DELETE FROM rooms WHERE room = ? and month = ? and day = ? and year = ?"
    c.execute(unreserve, (room, int(date[0:2]) , int(date[2:4]), int(date[4:])))

    c.close()

    db.commit()
    db.close()

# if room is being blocked, kick out people who already made a reservation
# prevent clubs from reserving room again
def block_room(room, date):
    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    kick_out_reserved = "DELETE FROM rooms WHERE room = ? and month = ? and day = ? and year = ? "
    c.execute(kick_out_reserved, (room, int(date[0:2]) + 1, int(date[2:4]), int(date[4:])))

    block_reservation = "INSERT INTO rooms (room, club, month, day, year) VALUES(?, ?, ?, ?, ?) "
    c.execute(block_reservation, (room, "Blocked", int(date[0:2]) + 1, int(date[2:4]), int(date[4:])))

    c.close()
    db.commit()
    db.close()

def unblock_room(room, date):
    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    unblock_reservation = "DELETE FROM rooms WHERE room = ? AND month = ? AND day = ? AND year = ?"
    c.execute(block_reservation, (room, "Blocked", int(date[0:2]) + 1, int(date[2:4]), int(date[4:])))

    c.close()
    db.commit()
    db.close()
