import hashlib
import sqlite3
import os
import random

def hashp(x):
	h = hashlib.sha256()
	h.update(x)
	return h.hexdigest()

def createAccount(user, password, isAdmin):
	isAdmin = int(code[-1])
	f = "data/data.db"
	db = sqlite3.connect(f)

	sp = db.cursor()
	insert = "INSERT INTO users VALUES ('%s', '%s', '%d')" % (user, hashp(password), isAdmin)
	sp.execute(insert)

	db.commit()
	db.close()

'''
Makes sure that the username and password given are valid.
'''
def checkLogin(usern, pw):
	hashed = hashp(pw)

	f = "data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()

	s = "SELECT usern, pw FROM users WHERE usern = ? and pw = ?"
	t = sp.execute(s, (usern, hashed)).fetchone()

        if t is None:
                db.commit()
                db.close()

                return False
        else:
                db.commit()
                db.close()

                return True

'''
If true is returned, that means that the user
can sign up an account with the given email and code.
'''
def checkRegister(email, code):
	f = "data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()

	query = "SELECT email, code FROM accounts WHERE email = '" + email + "' AND code = '" + code + "';"
	t = sp.execute(query)

	res = t.fetchall()[0]
	if len(res) == 0:
                db.commit()
                db.close()
                return False

        db.commit()
	db.close()

	return True

# ================================
# ACCOUNT CODE CREATION
# ================================

'''
To be used by the person in charge of the room reservation
website so that clubs can create accounts.
'''
def storeCode(email, isAdmin):
	f = "data/data.db"
	db = sqlite3.connect(f)

	sp = db.cursor()
	code = generateCode(isAdmin)

	while codeCheck(code):
                code = generateCode(isAdmin)

	insert = "INSERT INTO accounts VALUES ('%s', '%s')" % (email, code)
	sp.execute(insert)

	db.commit()
	db.close()

def generateCode(isAdmin):
	return str(int(random.random()*10000)) + str(isAdmin)

# ================================
# ACCOUNT CODE CHECKING
# ================================
'''
Gets an admin level for a specific user.
'''
def getAdminLevel(email):
	f = "data/data.db"
	db = sqlite3.connect(f)
	sp = db.cursor()

	s = "SELECT code FROM accounts WHERE email ='" + email + "';"
        t = sp.execute(s)

	res = t.fetchall()

        db.commit()
	db.close()

        return res[0][-1]

'''
Checks if a code was used.
'''
def codeUsed(code):
        f = "data/data.db"
        db = sqlite3.connect(f)
        gt = db.cursor()

        request = "SELECT code FROM accounts;"
        codes = gt.execute(request).fetchall()

        for usedCode in codes:
                if usedCode[0] == code:
                        db.commit()
                        db.close()

                        return True

        db.commit()
        db.close()

        return False

def isStudent(code):
	return int(code[-1]) == 0

def isAdmin(code):
	return int(code[-1]) == 1 or int(code[-1]) == 2
