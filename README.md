# Location Predict Server

Logs data from provided by the client and predicts the location based on previously logged data.

# API


## Response

### Storing location data

Syntax:
`http://mydomain.com/logdata/<string uuid>/<float latitude>/<float longitude>/<int weekday>/<int hour>/<int minutes_quantized>`

Sample response:

```json
{
   "error":{
      "code":0,
      "comment":"valid"
   }
}
```

- error/code is `0` when there is no error and is `1` when there the given input is not valid.

### Get predicted location

Syntax: 
`http://mydomain.com/logdata/<uuid>/predictlocation`

Sample response:

```json
{
   "prediction":{
      "latitude":34.4455,
      "longitude":76.6767
   },
   "status":{
      "action":"none",
      "situation":"normal"
   }
}
```