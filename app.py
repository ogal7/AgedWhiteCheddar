from flask import Flask, render_template, request, session, redirect, url_for, Response
import hashlib
import time
from utils import users, clubInfo

app = Flask(__name__)
app.secret_key = 'agedwhitecheddar'

@app.route('/')
@app.route('/home/')
def main():
    if 'user' in session: 
        return redirect(url_for("homepage"))
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
    username = loginResponse["user"]
    password = loginResponse["pw"]
    formMethod = loginResponse['enter']
    if formMethod == "Login":
        if users.checkLogin(username,password) == True:
            session['user']= username
            return redirect(url_for("homepage"))
        else:
            message = "login failed"
            if 'user' in session:
                session.pop('user')
            return redirect(url_for("main"))
    if formMethod == "Register":
        return redirect(url_for("register"))
         
@app.route("/clubInfo/", methods =["POST"])
def clubForm():
    pass

@app.route("/logout/")
def logout():
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
