#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('../db/locationdata.db')
print "Opened database successfully"

conn.execute('''CREATE TABLE `locationlog` (
	`id`	INTEGER NOT NULL UNIQUE,
	`uuid`	TEXT NOT NULL,
	`latitude`	REAL NOT NULL,
	`longitude`	REAL NOT NULL,
	`weekday`	INTEGER NOT NULL,
	`hour`	INTEGER NOT NULL,
	`minute_quant`	INTEGER NOT NULL,
	`repeated_count`	INTEGER,
	CONSTRAINT unq UNIQUE (uuid, latitude, longitude, weekday, hour, minute_quant),
	PRIMARY KEY(id)
);''')
print "Table created successfully"

conn.close()
