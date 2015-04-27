#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sqlite3


class Data:

    'Data class. Verifies input data, saves and generates output.'

    def __init__(self, uuid, latitude, longitude, weekday, hour, minuteQuantized):
        self.uuid = str(uuid)
        truncateToDigits = 6
        self.latitude = round(latitude, truncateToDigits)
        self.longitude = round(longitude, truncateToDigits)
        self.weekday = weekday
        self.hour = hour
        self.minuteQuantized = minuteQuantized
        self.inputValidity = self.validateInput()
        if self.inputValidity == 'valid':
            self.saveDataToDb()

    def validateInput(self):
        if self.latitude > 90.0 or self.latitude < -90.0:
            return "Latitude {} is not in the range between +/-180.0".format(self.latitude)
        elif self.longitude > 180.0 or self.longitude < -180.0:
            return "Longitude {} is not in the range between +/-180.0".format(self.longitude)
        elif self.weekday > 6:
            return "Weekday {} is not in the range (0, 6)".format(self.weekday)
        elif self.hour > 23:
            return "Hour {} is not in the range (0, 23)".format(self.hour)
        elif self.minuteQuantized > 3:
            return "Quantized minute {} is not in the range (0, 3)".format(self.minuteQuantized)
        else:
            return "valid"

    def generateResponseJson(self):
        responseData = {}
        responseData['error'] = {}
        if self.inputValidity == 'valid':
            responseData['error']['code'] = 0
        else:
            responseData['error']['code'] = 1
        responseData['error']['comment'] = self.inputValidity
        responseJson = json.dumps(responseData, indent=4, sort_keys=True)
        return responseJson

    def saveDataToDb(self):
        print "Entered saveData"
        conn = sqlite3.connect('db/locationdata.db')
        print "Connected to database"
        insertSQL = 'INSERT INTO locationlog (uuid, latitude, longitude, weekday, hour, minute_quant, repeated_count) VALUES ("{}", {}, {}, {}, {}, {}, 1);'
        insertSQL = insertSQL.format(
            self.uuid, self.latitude, self.longitude, self.weekday, self.hour, self.minuteQuantized)
        updateSQL = 'UPDATE locationlog SET repeated_count= repeated_count+1 WHERE EXISTS (SELECT * FROM locationlog WHERE uuid = "{}" AND latitude={} AND longitude={} AND weekday={} AND hour={} AND minute_quant={});'
        updateSQL = updateSQL.format(
            self.uuid, self.latitude, self.longitude, self.weekday, self.hour, self.minuteQuantized)
        try:
            conn.execute(insertSQL)
        except:
            conn.execute(updateSQL)
        print "Table created successfully"
        conn.commit()
        conn.close()
        return 0
