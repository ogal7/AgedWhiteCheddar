from flask import Flask, render_template, request, session, redirect, url_for, Response

app = Flask(__name__)
app.secret_key = 'agedwhitecheddar'

@app.route('/')
def home():
    return render_template("entry.html")


if __name__ == '__main__':
    app.debug = True
    app.run(threaded = True)
