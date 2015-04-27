#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sqlite3


def getDataFromDB(uuid):
    conn = sqlite3.connect('../db/locationdata.db')
    sqlGetUserData = 'SELECT uuid, latitude, longitude, weekday, hour, minute_quant, repeated_count FROM locationlog WHERE uuid = "{}";'
    locationEntryDB = conn.execute(sqlGetUserData.format(uuid) )
    locationEntryList = []
    for locationEntry in locationEntryDB:
        locationEntryList.append(locationEntry)
    conn.close()
    return locationEntryList


def generatePredictedJson(uuid, predictedLat, predictedLon, statusSituation, statusAction):
    responseData = {}
    responseData['prediction'] = {}
    responseData['prediction']['latitude'] = predictedLat
    responseData['prediction']['longitude'] = predictedLon
    responseData['status'] = {}
    responseData['status']['situation'] = 'normal'
    responseData['status']['action'] = 'none'
    print responseData
    responseJson = json.dumps(responseData, indent=4, sort_keys=True)
    return responseJson


def locationPredict(uuid):
    predictedLat = 34.4455
    predictedLon = 76.6767
    statusSituation = 'normal'
    statusAction = 'none'
    print "uuid: "
    responseJson = generatePredictedJson(uuid, predictedLat, predictedLon, statusSituation, statusAction)
    return responseJson

# print getDataFromDB('apr0041')