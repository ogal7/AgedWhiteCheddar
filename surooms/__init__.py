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
    if 'user' in session:
        if users.signup_completed(session['user']):
            return redirect(url_for("homepage"))
        else:
            return redirect(url_for("enter_club_info"))
    return render_template("entry.html")

# =====================
# authentication
# =====================
@app.route("/auth/", methods = ["POST"])
def auth():
    loginResponse = request.form
    username = loginResponse["email"]
    password = loginResponse["pw"]
    formMethod = loginResponse['enter']
    # print "Form method: " + formMethod

    if formMethod == "login":
        if users.checkLogin(username, password):
            session['user'] = username
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
                session['user'] = username
                return redirect(url_for('enter_club_info')) #asks for more info from students running clubs
            else:
                users.createAccount(username,password,code)
                session['user']= username
                adminLevel = users.getAdminLevel(username)[-1]
                if adminLevel == '2':
                    session['master'] = True
                    print "Admin level: 2"
                elif adminLevel == '1':
                    session['admin'] = True
                    print "Admin level: 1"
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
    if 'user' not in session:
        return redirect(url_for("main"))

    # Prevents users from completing form twice
    if 'user' in session and users.signup_completed(session['user']):
        return redirect(url_for("homepage"))

    response = request.form
    if 'clubName' in response and 'adName' in response and 'adEmail' in response:
        clubName = response['clubName']
        adName = response['adName']
        adEmail = response['adEmail']
        club.addClub(clubName, session['user'], adName, adEmail)
        return redirect(url_for("homepage"))
    else:
        return render_template("clubRegister.html")

# =====================
# logged in users
# =====================
@app.route("/homepage/", methods=["POST","GET"])
def homepage():
    if 'user' not in session:
        return redirect(url_for("main"))

    if 'user' in session and not users.signup_completed(session['user']):
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
    #return render template of a calendar, calendar days will launch a link to an html where the message is generated from writeSchedule.py
    return render_template("roomSchedule.html", action = "Rooms Previously or Currently Being Reserved")

@app.route("/roomSched/<date>/")
def daySchedule(date):
    d2 = date.split("-")
    data = room.getInfoDate(str(int(d2[0]) + 1),d2[1],d2[2])

    return render_template("dayRooms.html", message=data)


@app.route("/seeClubs/")
def seeClubs():
    data = club.getAllClubs()
    return render_template("SeeClubs.html", message=data)

@app.route("/homepage/<date>/", methods = ["GET"])
def find_floor(date):
    if 'user' not in session:
        return redirect(url_for("main"))

    if 'user' in session and not users.signup_completed(session['user']):
        return redirect(url_for("enter_club_info"))

    if 'floor' in request.args and ('admin' in session or 'master' in session):
        if request.args['floor'] == '2':
            return render_template("map2A.html") #, floor = "2", date = date)
        if request.args['floor'] == '3':
            return render_template("map3A.html") #, floor = "3", date = date)
        if request.args['floor'] == '4':
            return render_template("map4A.html") #, floor = "4", date = date)

    if 'floor' in request.args:
        if request.args['floor'] == '2':
            return render_template("map2.html") #, floor = "2", date = date)
        if request.args['floor'] == '3':
            return render_template("map3.html") #, floor = "3", date = date)
        if request.args['floor'] == '4':
            return render_template("map4.html") #, floor = "4", date = date)
    return render_template("floors.html", message=date)

@app.route("/unreserve/", methods=["POST"])
def unRes():
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
    print date
    #431/5/8/2017
    reserve.unreserve_room_club(data[0], date, session['user'] )

    return redirect(url_for("my_rooms"))

@app.route("/unblock/", methods=["POST"])
def unBlock():
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
    print date
    #431/5/8/2017
    reserve.unblock_room(data[0], date)

    return redirect(url_for("block_rooms"))

@app.route('/myRooms/')
def my_rooms():
    if 'user' in session:
        user = session['user']
        data = myRooms.getRoomsNow(user)
        return render_template("myRooms.html", message = data, user=session['user'])
    else:
        return redirect(url_for("main"))

@app.route('/blockRooms/')
def block_rooms():
    if 'user' not in session or ('admin' not in session and 'master' not in session):
        return redirect(url_for("main"))
    else:
        user = session['user']
        data = myRooms.getBlockedRooms()
        return render_template("blockedRooms.html", message = data, user=session['user'])


@app.route("/reserve/<date>/", methods=["GET"])
def reserveR(date):
    if 'user' not in session:
        return redirect(url_for("main"))

    if 'user' in session and not users.signup_completed(session['user']):
        return redirect(url_for("enter_club_info"))

    d = date.strip().split("-")
    d2 = ""
    for i in d:
        d2 += str(i).zfill(2)

    room = request.args['room']
    if (reserve.reserve_room(room, d2 ,session['user'])):
        flash('Room Sucessfully Reserved')
        return redirect(url_for("my_rooms"))
    flash("Unable to Reserve Room. Please Make Another Selection")
    return redirect(url_for('main'))

@app.route("/block/<date>/", methods=["GET"])
def blockR(date):
    if 'user' not in session:
        return redirect(url_for("main"))

    if 'user' in session and not users.signup_completed(session['user']):
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
    return render_template("codes.html")

@app.route('/approve/', methods=["POST"])
def approve_clubs():
    if 'admin_level' in request.form and 'clubEmail' in request.form:
        users.storeCode(request.form['clubEmail'], request.form['admin_level'])
        flash('User Approved!')
        return redirect(url_for('addClubz'))
    else:
        flash("Unable to Approve User")
        return redirect(url_for('addClubz'))

@app.route('/settings/', methods = ['GET',"POST"])
def settings():
    return render_template("settings.html")

@app.route('/change/', methods = ["POST"])
def change():
    loginResponse = request.form
    old =  users.hashp(request.form['oldpass'])
    new = request.form['newpass']
    conf = request.form['confpass']
    print users.getPass(session['user'])[0]
    print old
    print new
    print conf
    if users.getPass(session['user'])[0] == old and new == conf:
        users.changePassword(session['user'],new)
        return redirect(url_for("main"))
    return render_template("settings.html")

@app.route('/archive/', methods = ["GET", "POST"])
def seeRooms():
    if 'year' in request.form:
        try:
            year = int(request.form['year'].strip())
            return render_template('seeRoom.html', message = room.getInfoYear(str(year)))
        except:
            return render_template('seeRoom.html', message = room.getInfoYear('2017'))

    return render_template('seeRoom.html', message = room.getInfoYear('2017'))


# @app.route('/seeit/', methods=['POST'])
# def seeit():
#     year =  request.form['username'];
#     return jsonify(room.getInfoYear(year))

# =====================
# log out
# =====================
@app.route("/logout/")
def logout():
    if 'user' in session:
        session.pop("user")
    if 'master' in session:
        session.pop("master")
    if 'admin' in session:
        session.pop("admin")
    return redirect(url_for("main"))

# =====================
# run app
# =====================
if __name__ == '__main__':
    app.debug = True
    app.run(threaded = True)
