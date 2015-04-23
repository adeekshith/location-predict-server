#!/usr/bin/python
# -*- coding: utf-8 -*-
import json


class Data:

    'Data class. Verifies input data, saves and generates output.'

    def __init__(self, uuid, latitude, longitude, weekday, hour, minuteQuantized):
        self.uuid = str(uuid)
        self.latitude = latitude
        self.longitude = longitude
        self.weekday = weekday
        self.hour = hour
        self.minuteQuantized = minuteQuantized
        self.inputValidity = self.validateInput()

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

