from flask import Flask, render_template, request, session, redirect, url_for, Response, flash
import hashlib
import time
from utils import users, club, room, reserve, myRooms, dayRooms
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
    print "Form method: " + formMethod

    if formMethod == "login":
        if users.checkLogin(username, password):
            session['user'] = username
            return redirect(url_for("homepage"))
        else:
            flash("Login failed. Username not recognized or password is incorrect.")

    if formMethod == "register":
        code = loginResponse['code']
        pwConfirm = loginResponse["pwConfirm"]
        if pwConfirm != password:
            flash("Please confirm passwords match.")
            return redirect(url_for("main"))            
            
        # users.checkRegister(username, code): # code/email match is valid
        if users.validCred(username,code):
            if users.isStudent(code):
                #print "student"
                users.createAccount(username, password, code)
                session['user'] = username
                return redirect(url_for('enter_club_info')) #asks for more info from students running clubs
            else: 
                #print "admin"
                users.createAccount(username,password,code)
                session['user']= username
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
        print "ok"
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

    return render_template("homepage.html")

@app.route("/roomSched/")
def schedule():
    if 'user' not in session:
        return redirect(url_for("main"))
    
    if 'user' in session and not users.signup_completed(session['user']):
        return redirect(url_for("enter_club_info"))

    #return render template of a calendar, calendar days will launch a link to an html where the message is generated from writeSchedule.py

    return render_template("roomSchedule.html")

@app.route("/roomSched/<date>/")
def daySchedule(date):
    if 'user' not in session:
        return redirect(url_for("main"))
    
    if 'user' in session and not users.signup_completed(session['user']):
        return redirect(url_for("enter_club_info"))

    d2 = date.split("-")
    date1 = ""
    for i in d2:
        date1+=i
    data = dayRooms.getRooms(date1)
    return render_template("dayRooms.html", message=data)


@app.route("/homepage/<date>/", methods = ["GET"])
def find_floor(date):
    if 'user' not in session:
        return redirect(url_for("main"))
    
    if 'user' in session and not users.signup_completed(session['user']):
        return redirect(url_for("enter_club_info"))
        
    if 'floor' in request.args:
        if request.args['floor'] == '2':
            return render_template("map2.html")
        if request.args['floor'] == '3':
            return render_template("map3.html")
        if request.args['floor'] == '4':
            return render_template("map4.html")
    return render_template("floors.html", message=date)

@app.route('/myRooms/')
def my_rooms():
    if 'user' in session:
        user = session['user']
        date= (time.strftime("%d/%m/%Y"))
        print date
        data = myRooms.getRooms(user, date[6:])
        for li in data:
            li[1] = li[1][:2] + "/" + li[1][2:4] + "/" + li[1][4:]
            print li[1]

        return render_template("myRooms.html", message=data, user=session['user'])
    else:
        return redirect(url_for("main"))

@app.route("/reserve/<date>/", methods=["GET"])
def reserveR(date):
    if 'user' not in session:
        return redirect(url_for("main"))

    if 'user' in session and not users.signup_completed(session['user']):
        return redirect(url_for("enter_club_info"))

    print "ughHH"
    d = date.split("-");
    d2 = ""
    for i in d:
        d2 += str(i)
    #date=request.form['date']
    room=request.args['room']
    reserve.reserve_room(room,d2,session['user'])
    return redirect(url_for("homepage"))

@app.route('/settings/')
def settings():
    pass

# =====================
# log out
# =====================
@app.route("/logout/")
def logout():
    if 'user' in session:
        session.pop("user")
    return redirect(url_for("main"))

# =====================
# run app
# =====================
if __name__ == '__main__':
    app.debug = True
    app.run(threaded = True)
