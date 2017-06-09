from flask import Flask, render_template, request, session, redirect, url_for, Response, flash, jsonify, json
import hashlib
import time
from utils import users, club, room, reserve, myRooms
import os

app = Flask(__name__)
# app.secret_key = 'agedwhitecheddar'
app.secret_key = os.urandom(32)

# =====================
# main page
# =====================
@app.route('/', methods = ["GET", "POST"])
def main():
    print "SESSION: " + str(session)

    if 'username' in session:
        if users.signup_completed(session['username']):
            return redirect(url_for("homepage"))
        else:
            return redirect(url_for("enter_club_info"))

    return render_template("entry.html")

# =====================
# authentication
# =====================
@app.route("/authenticate/", methods = ["POST"])
def authenticate():
    print "SESSION: " + str(session)
    print "REQUEST: " + str(request.form)
    
    loginResponse = request.form
    username = loginResponse["email"]
    password = loginResponse["pw"]
    formMethod = loginResponse['enter']

    if formMethod == "login":
        if users.checkLogin(username, password):
            session['username'] = username
            adminLevel = users.getAdminLevel(username)[-1]
            if adminLevel == '2':
                session['master'] = True
            elif adminLevel == '1':
                session['admin'] = True
            else:
                if 'master' in session:
                    session.pop("master")
                if 'admin' in session:
                    session.pop("admin")

            return redirect(url_for("homepage"))
        else:
            flash("Login failed. Username not recognized or password is incorrect.")

    if formMethod == "register":
        code = loginResponse['code']
        pwConfirm = loginResponse["pwConfirm"]
        if pwConfirm != password:
            flash("Please confirm passwords match.")
            return redirect(url_for("main"))

        if users.validCred(username,code):
            if users.isStudent(code):
                users.createAccount(username, password, code)
                session['username'] = username
                return redirect(url_for('enter_club_info')) #asks for more info from students running clubs
            else:
                users.createAccount(username,password,code)
                session['username']= username
                adminLevel = users.getAdminLevel(username)[-1]
                if adminLevel == '2':
                    session['master'] = True
                    # print "Admin level: 2"
                elif adminLevel == '1':
                    session['admin'] = True
                    # print "Admin level: 1"
                else:
                    if 'master' in session:
                        session.pop("master")
                    if 'admin' in session:
                        session.pop("admin")

                return redirect(url_for('homepage')) # admins dont need additional info
        else:
            flash("Register failed. Email not approved yet.")

    return redirect(url_for("main"))

# =====================
# enter club info
# =====================
@app.route("/clubInfo/", methods = ["GET", "POST"])
def enter_club_info():
    print "SESSION: " + str(session)

    if 'username' not in session:
        return redirect(url_for("main"))

    # Prevents users from completing form twice
    if 'username' in session and users.signup_completed(session['username']):
        return redirect(url_for("homepage"))

    response = request.form
    if 'clubName' in response and 'adName' in response and 'adEmail' in response:
        clubName = response['clubName']
        adName = response['adName']
        adEmail = response['adEmail']
        club.addClub(clubName, session['username'], adName, adEmail)
        return redirect(url_for("homepage"))
    else:
        return render_template("clubRegister.html")

# =====================
# logged in users
# =====================
@app.route("/homepage/", methods=["POST","GET"])
def homepage():
    print "WHAT"
    print "SESSION: " + str(session)

    if 'username' not in session:
        print "ok"
        return redirect(url_for("main"))

    if 'username' in session and not users.signup_completed(session['username']):
        return redirect(url_for("enter_club_info"))

    if 'master' in session:
        action="Click a Date to Block or Reserve a Room"

    if 'admin' in session:
        action = "Click a Date to Block or Reserve a Room"

    if 'admin' not in session and 'master' not in session:
        action ="Click a Date to Reserve a Room"

    return render_template("homepage.html", action = action)

@app.route("/roomSched/")
def schedule():
    print "SESSION: " + str(session)
    
    #return render template of a calendar, calendar days will launch a link to an html where the message is generated from writeSchedule.py
    return render_template("roomSchedule.html", action = "Rooms Previously or Currently Being Reserved")

@app.route("/roomSched/<date>/")
def daySchedule(date):
    print "SESSION: " + str(session)

    d2 = date.split("-")
    data = room.getInfoDate(str(int(d2[0]) + 1),d2[1],d2[2])

    return render_template("dayRooms.html", message=data)

@app.route("/seeClubs/")
def seeClubs():
    print "SESSION: " + str(session)
    
    data = club.getAllClubs()
    return render_template("seeClubs.html", message=data)

@app.route("/homepage/<date>/", methods = ["GET"])
def find_floor(date):
    print "SESSION: " + str(session)

    if 'username' not in session:
        return redirect(url_for("main"))

    if 'username' in session and not users.signup_completed(session['username']):
        return redirect(url_for("enter_club_info"))

    if 'floor' in request.args and ('admin' in session or 'master' in session):
        if request.args['floor'] == '2':
            return render_template("map2A.html")
        if request.args['floor'] == '3':
            return render_template("map3A.html")
        if request.args['floor'] == '4':
            return render_template("map4A.html")

    if 'floor' in request.args:
        if request.args['floor'] == '2':
            return render_template("map2.html")
        if request.args['floor'] == '3':
            return render_template("map3.html")
        if request.args['floor'] == '4':
            return render_template("map4.html")
    return render_template("floors.html", message=date)

@app.route("/unreserve/", methods=["POST"])
def unRes():
    print "SESSION: " + str(session)
    print "REQUEST: " + str(request.form)
    
    if 'room' in request.form and 'username' in session:
        data = request.form['room']
        data = data.split("/")

        if int(data[2]) < 10:
            data[2] = "0" + data[2]
        if int(data[1]) < 10:
            data[1] = "0" + data[1]

        date = data[1] + data[2] + data[3]

        #431/5/8/2017
        reserve.unreserve_room_club(data[0], date, session['username'])

    return redirect(url_for("my_rooms"))

@app.route("/unblock/", methods=["POST"])
def unBlock():
    print "SESSION: " + str(session)

    #for i in request.form:
    #    print i + " " + str(request.form[i])
    data = request.form['room']
    data = data.split("/")
    #print data
    if int(data[2]) < 10:
        data[2] = "0" + data[2]
    if int(data[1]) < 10:
        data[1] = "0" + data[1]

    date = data[1] + data[2] + data[3]
    # print date
    #431/5/8/2017
    reserve.unblock_room(data[0], date)

    return redirect(url_for("block_rooms"))

@app.route('/myRooms/')
def my_rooms():
    print "SESSION: " + str(session)

    if 'username' in session:
        user = session['username']
        data = myRooms.getRoomsNow(user)
        print data
        return render_template("myRooms.html", message = data, user = session['username'])
    else:
        return redirect(url_for("main"))

@app.route('/blockRooms/')
def block_rooms():
    print "SESSION: " + str(session)

    if 'username' not in session or ('admin' not in session and 'master' not in session):
        return redirect(url_for("main"))
    else:
        user = session['username']
        data = myRooms.getBlockedRooms()
        return render_template("blockedRooms.html", message = data, user=session['username'])

@app.route("/reserve/<date>/", methods=["GET"])
def reserveR(date):
    print "SESSION: " + str(session)

    if 'username' not in session:
        return redirect(url_for("main"))

    if 'username' in session and not users.signup_completed(session['username']):
        return redirect(url_for("enter_club_info"))

    d = date.strip().split("-")
    d2 = ""
    for i in d:
        d2 += str(i).zfill(2)

    room = request.args['room']
    if (reserve.reserve_room(room, d2 ,session['username'])):
        flash('Room Sucessfully Reserved')
        return redirect(url_for("my_rooms"))
    flash("Unable to Reserve Room. Please Make Another Selection")
    return redirect(url_for('main'))

@app.route("/block/<date>/", methods=["GET"])
def blockR(date):
    print "SESSION: " + str(session)

    if 'username' not in session:
        return redirect(url_for("main"))

    if 'username' in session and not users.signup_completed(session['username']):
        return redirect(url_for("enter_club_info"))

    d = date.strip().split("-")
    d2 = ""
    for i in d:
        d2 += str(i).zfill(2)

    room = request.args['room']
    reserve.block_room(room, d2)
    flash('Room Blocked')
    return redirect(url_for("main"))

@app.route("/addClub/")
def addClubz():
    print "SESSION: " + str(session)

    return render_template("codes.html")

@app.route('/approve/', methods=["POST"])
def approve_clubs():
    print "SESSION: " + str(session)

    if 'admin_level' in request.form and 'clubEmail' in request.form:
        users.storeCode(request.form['clubEmail'], request.form['admin_level'])
        flash('User Approved!')
        return redirect(url_for('addClubz'))
    else:
        flash("Unable to Approve User")
        return redirect(url_for('addClubz'))

@app.route('/settings/', methods = ['GET',"POST"])
def settings():
    print "SESSION: " + str(session)

    return render_template("settings.html")

@app.route('/change/', methods = ["POST"])
def change():
    print "SESSION: " + str(session)

    loginResponse = request.form
    old =  users.hashp(request.form['oldpass'])
    new = request.form['newpass']
    conf = request.form['confpass']
    if users.getPass(session['username'])[0] == old and new == conf:
        users.changePassword(session['username'],new)
        return redirect(url_for("main"))
    return render_template("settings.html")

@app.route('/archive/', methods = ["GET", "POST"])
def seeRooms():
    print "SESSION: " + str(session)

    if 'year' in request.form:
        try:
            year = int(request.form['year'].strip())
            return render_template('seeRoom.html', message = room.getInfoYear(str(year)))
        except:
            return render_template('seeRoom.html', message = room.getInfoYear('2017'))

    return render_template('seeRoom.html', message = room.getInfoYear('2017'))

# =====================
# log out
# =====================
@app.route("/logout/")
def logout():
    session.clear()
    print "SESSION: " + str(session)

    return redirect(url_for("main"))

# =====================
# run app
# =====================
if __name__ == '__main__':
    app.debug = True
    app.run(threaded = True)
