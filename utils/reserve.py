def reserve_room(room, date, clubName):
    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    add_reservation = "INSERT INTO rooms2017 (room, date, clubName) VALUES(?, ?, ?)"
    c.execute(add_reservation, (room, date, clubName))
    
    c.close()

    db.commit()
    db.close()

# can unreserve if the club that reserved the room
def unreserve_room_club(room, date, clubName):
    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    
def block_room(room, date, is_admin):
    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    if is_admin:
        kick_out_reserved = "DELETE FROM rooms2017 where room = ? and date = ?"
        c.execute(kick_out_reserved, (room, date))
    
    block_reservation = "INSERT INTO rooms2017 (room, date, clubName) VALUES(?, ?, ?)"
    c.execute(block_reservation, (room, date, "N/A"))
    
    c.close()

    db.commit()
    db.close()
    
