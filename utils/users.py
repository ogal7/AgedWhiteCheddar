import hashlib
import sqlite3
import os
import random
from approve import sendEmail
f = "data/data.db"

def hashp(x):
    h = hashlib.sha256()
    h.update(x)
    return h.hexdigest()

def createAccount(user, password, code):
    isAdmin = int(code[-1])
    db = sqlite3.connect(f)

    sp = db.cursor()
    insert = "INSERT INTO users VALUES ('%s', '%s', '%d')" % (user, hashp(password), isAdmin)
    sp.execute(insert)

    sp.close()
    db.commit()
    db.close()

'''
Makes sure that the username and password given are valid.
'''
def checkLogin(usern, pw):
    hashed = hashp(pw)
    print f
    print "hi"
    db = sqlite3.connect(f)
    sp = db.cursor()

    s = "SELECT usern, pw FROM users WHERE usern = ? and pw = ?"
    t = sp.execute(s, (usern, hashed)).fetchone()

    if t is None:
        sp.close()
        db.commit()
        db.close()

        return False
    else:
        sp.close()
        db.commit()
        db.close()

        return True

def getPass(usern):
    db = sqlite3.connect(f)
    sp = db.cursor()

    s = "SELECT pw FROM users WHERE usern = '%s' "%(usern)
    t = sp.execute(s).fetchone()

    sp.close()
    db.commit()
    db.close()

    return t

def changePassword(usern,pw):
    hashed = hashp(pw)
    db = sqlite3.connect(f)
    sp = db.cursor()
    s = "UPDATE users SET pw = '%s' WHERE usern = '%s'"%(hashed,usern)
    sp.execute(s)

    sp.close()
    db.commit()
    db.close()

'''
If true is returned, that means that the user
can sign up an account with the given email and code.
'''
def checkRegister(email, code):
    db = sqlite3.connect(f)
    sp = db.cursor()

    query = "SELECT email, code FROM codes WHERE email = '" + email + "' AND code = '" + code + "';"
    t = sp.execute(query)

    res = t.fetchone()
    if res is None:
        sp.close()
        db.commit()
        db.close()

        return False

    sp.close()
    db.commit()
    db.close()

    return True

def signup_completed(user):
    db = sqlite3.connect(f)
    sp = db.cursor()

    admin_level_query = "SELECT isAdmin from users WHERE usern = ?"
    r = sp.execute(admin_level_query, (user,)).fetchone()

    signed_up_query = "SELECT email from clubs WHERE email = ?"
    r2 = sp.execute(signed_up_query, (user,)).fetchone()

    signed_up = False
    if r != None: # student signed up
        if int(r[0]) > 0:
            signed_up = True
        if int(r[0]) == 0 and r2 != None: # signed up the club
            signed_up = True

    sp.close()
    db.commit()
    db.close()

    return signed_up

# ================================
# ACCOUNT CODE CREATION
# ================================

'''
To be used by the person in charge of the room reservation
website so that clubs can create accounts.
'''
def storeCode(email, isAdmin):
	if emailUsed(email):
		return "email already approved"
	db = sqlite3.connect(f)
	sp = db.cursor()
	code = generateCode(isAdmin)
	while codeUsed(code):
		code = generateCode(isAdmin)

	insert = "INSERT INTO codes VALUES ('%s', '%s')" % (email, code)
	sp.execute(insert)
	sp.close()
	db.commit()
	db.close()

	sendEmail(email, code)

def generateCode(isAdmin):
    return str(int(random.random()*10000)) + str(isAdmin)

# ================================
# ACCOUNT CODE CHECKING
# ================================
'''
Gets an admin level for a specific user.
'''

def getAdminLevel(email):
    db = sqlite3.connect(f)
    sp = db.cursor()

    s = "SELECT code FROM codes WHERE email ='" + email + "';"
    t = sp.execute(s)

    res = t.fetchall()

    sp.close()
    db.commit()
    db.close()

    return res[0][-1]


'''
Checks if a code was used.
'''
def codeUsed(code):
    db = sqlite3.connect(f)
    sp = db.cursor()

    request = "SELECT code FROM codes;"
    codes = sp.execute(request).fetchall()

    for usedCode in codes:
        if usedCode[0] == code:
            sp.close()
            db.commit()
            db.close()

            return True

    sp.close()
    db.commit()
    db.close()

    return False

def emailUsed(email):
    db = sqlite3.connect(f)
    sp = db.cursor()

    request = "SELECT email FROM codes;"
    codes = sp.execute(request).fetchall()

    for usedEmail in codes:
        if usedEmail[0] == email:
            sp.close()
            db.commit()
            db.close()

            return True

    sp.close()
    db.commit()
    db.close()

    return False

def validCred(email,code):
	db = sqlite3.connect(f)
	sp = db.cursor()
	s = "SELECT email, code FROM codes WHERE email = ? and code = ?"
	t = sp.execute(s, (email, code)).fetchone()
	if t is None:
            sp.close()
            db.commit()
            db.close()

            return False
	else:
            sp.close()
            db.commit()
            db.close()

            return True

def isStudent(code):
	return int(code[-1]) == 0
