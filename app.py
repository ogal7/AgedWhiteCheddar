from flask import Flask, render_template, request, session, redirect, url_for, Response
#from utils import

app = Flask(__name__)
app.secret_key = 'agedwhitecheddar'

@app.route('/')
@app.route('/home/')
def home():
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
            
@app.route('/login/')
def login_page():
    if 'username' in request.form:
        # valid = authenticate(request.form['username'], request.form['password'])
        # if valid:
        #     return redirect(url_for('homepage'))
        return redirect(url_for('homepage'))
        
@app.route('/settings/')
def settings():
    pass

@app.route('/floors/')
def choose_floor():
    pass

if __name__ == '__main__':
    app.debug = True
    app.run(threaded = True)
