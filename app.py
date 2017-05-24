from flask import Flask, render_template, request, session, redirect, url_for, Response
import hashlib
import time
from utils import users, club, room, reserve
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
        return redirect(url_for("homepage"))
    return render_template("entry.html")

# =====================
# authentication
# =====================

# TODO - check if password and confirm password matches as well - for later
# TODO - should display an auth error message on entry page - possibly by flashing messages
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
            message = "login failed"

    if formMethod == "register":
        code = loginResponse['code']
        # users.checkRegister(username, code): # code/email match is valid
        if True:
            if users.isStudent(code):
                #print "student"
                users.createAccount(username,password,code)
                session['user'] = username
                return redirect(url_for('enter_club_info')) #asks for more info from students running clubs
            else:
                #print "admin"
                users.createAccount(username,password,code)
                session['user']= username
                return redirect(url_for('homepage')) # admins dont need additional info
        else:
            message = "register failed"

    return redirect(url_for("main"))

# =====================
# enter club info
# =====================
@app.route("/clubInfo/", methods = ["GET", "POST"])
def enter_club_info():
    response = request.form
    print request.form
    if 'clubname' in response and 'adName' in response and 'adEmail' in response:
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
    return render_template("homepage.html")

@app.route("/roomSched/")
def sched():
    #return render template of a calendar, calendar days will launch a link to an html where the message is generated from writeSchedule.py
    pass

@app.route("/homepage/<date>/", methods = ["GET"])
def date(date):
    if 'floor' in request.args:
        if request.args['floor'] == '2':
            return render_template("map2.html")
        if request.args['floor'] == '3':
            return render_template("map3.html")
        if request.args['floor'] == '4':
            return render_template("map4.html")
    return render_template("floors.html", message=date)

@app.route('/floors/')
def choose_floor():
    pass

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
