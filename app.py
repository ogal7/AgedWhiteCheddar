from flask import Flask, render_template, request, session, redirect, url_for, Response
import hashlib
import time
from utils import users, clubInfo

app = Flask(__name__)
app.secret_key = 'agedwhitecheddar'

@app.route('/', methods = ["GET", "POST"])
@app.route('/home/', methods = ["GET", "POST"])
def main():
    if 'user' in session: 
        # return redirect(url_for("homepage"))
        pass
    return render_template("entry.html")

# @app.route('/register/', methods = ['POST'])
# def register_page():
#     if 'email' in request.form:
#         if 'club_name' in request.form and 'admin' not in request.form:
#             registered = register_club(request.form['email'], request.form['club_name'], request.form['code'])
#             if registered:
#                 return redirect(url_for('homepage'))
#             else:
#                 return render_template("register.html", error = "Club signup failed. Club code invalid.")
#         elif 'admin' in request.form:
#             registered = register_admin(request.form['email'], request.form['admin_name'], request.form['code'])
#             return render_template("register.html", error = "Admin signup failed. Admin code invalid.")
#     return 

@app.route("/auth/", methods = ["POST"])
def auth():
    loginResponse = request.form
    username = loginResponse["email"]
    password = loginResponse["pw"]
    formMethod = loginResponse['enter']
    print formMethod

    if formMethod == "login":
        if users.checkLogin(username,password) == True:
            session['user']= username
            return redirect(url_for("homepage"))
        else:
            message = "login failed"
            if 'user' in session:
                session.pop('user')
            return redirect(url_for("main"))

    if formMethod == "register":
        code = loginResponse['code']
        if users.checkRegister(username, code) == True:#code/user match is valid
            print "hi"
            if users.isStudent(code) == True:
                #print "student"
                users.createAccount(username,password,code)
                session['user'] = username
                return redirect(url_for('register'))#asks for more info from students running clubs
            else:
                #print "hi again! this is an admin account"
                users.createAccount(username,password,code)
                session['user']= username
                return redirect(url_for('homepage'))#admins dont need additional info
        return redirect(url_for("register"))

    return redirect(url_for("main"))

# work on fixing register         
@app.route("/register/", methods=["POST", "GET"])
def register():
    session["user"] = "ok@gmail.com"
    return render_template("clubRegister.html")

@app.route("/homepage/", methods=["POST","GET"])
def homepage():
    return render_template("homepage.html")

@app.route("/clubInfo/", methods =["POST"])
def clubForm():
    response = request.form
    clubName = response['clubName'] 
    adName = response['adName']
    adEmail = response['adEmail']
    users.addClub(clubName, session['user'], adName, adEmail)
    return redirect(url_for("main"))

@app.route("/roomSched/")
def sched():
    #return render template of a calendar, calendar days will launch a link to an html where the message is generated from writeSchedule.py
    pass

@app.route("/logOut/")
def logout():
    if 'user' in session:
        session.pop("user")
    return redirect(url_for("main"))

@app.route('/settings/')
def settings():
    pass

@app.route('/floors/')
def choose_floor():
    pass

if __name__ == '__main__':
    app.debug = True
    app.run(threaded = True)
