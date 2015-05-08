#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sqlite3
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer


def getDataFromDB(uuid, weekdayCurrent, hourCurrent, minuteQuantCurrent):
    conn = sqlite3.connect('../db/locationdata.db')
    sqlGetUserData = 'SELECT uuid, latitude, longitude, weekday, hour, minute_quant, repeated_count FROM locationlog WHERE uuid = "{}" AND weekday = {} AND hour = {} AND minute_quant = {};'
    locationEntryDB = conn.execute(sqlGetUserData.format(uuid, weekdayCurrent, hourCurrent, minuteQuantCurrent) )
    locationEntryList = list(locationEntryDB)
    return locationEntryList


def generatePredictedJson(uuid, predictedLat, predictedLon, statusSituation, statusAction):
    responseData = {}
    responseData['prediction'] = {}
    responseData['prediction']['latitude'] = predictedLat
    responseData['prediction']['longitude'] = predictedLon
    responseData['status'] = {}
    responseData['status']['situation'] = 'normal'
    responseData['status']['action'] = 'none'
    responseJson = json.dumps(responseData, indent=4, sort_keys=True)
    return responseJson


def locationPredict(uuid, latitudeCurrent, longitudeCurrent, weekdayCurrent, hourCurrent, minuteQuantCurrent):
    net = buildNetwork(3, 4, 2)
    ds = SupervisedDataSet(3, 2)
    userLocDataList = getDataFromDB(uuid, weekdayCurrent, hourCurrent, minuteQuantCurrent)
    print userLocDataList
    for userLocData in userLocDataList:
        latitudeDB = userLocData[1]
        longitudeDB = userLocData[2]
        weekdayDB = userLocData[3]
        hourDB = userLocData[4]
        minuteQuantDB = userLocData[5]
        repeatedCountDB = userLocData[6]
        for iter in range(repeatedCountDB):
            ds.addSample((weekdayDB,hourDB,minuteQuantDB), (latitudeDB, longitudeDB,))
    print("Dataset length: {}".format(len(ds)))
    trainer = BackpropTrainer(net, ds)
    # trainer.trainUntilConvergence()
    trainer.train()
    [predictedLat, predictedLon] = net.activate([weekdayCurrent, hourCurrent, minuteQuantCurrent])
    statusSituation = 'normal'
    statusAction = 'none'
    print "uuid: "
    responseJson = generatePredictedJson(uuid, predictedLat, predictedLon, statusSituation, statusAction)
    return responseJson

print locationPredict('apr0041', 17.45, 78.35, 1, 11, 2)