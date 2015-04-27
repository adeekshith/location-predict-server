#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('../db/locationdata.db')
print "Opened database successfully"
conn = sqlite3.connect(config.connect.sqliteDBPath)
userListDB = conn.execute('''SELECT * FROM locationlog;''')
for user in userListDB:
    print str(user)
conn.close()
