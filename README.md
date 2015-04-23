# Location Predict Server

Logs data from provided by the client and predicts the location based on previously logged data.

####WARNING
This project is still in an incubator stage. It is under development and not yet ready for production purposes. Feel free to fork it and contribute.

## API

### Storing location data

#### Syntax
`http://mydomain.com/location-predict/api/v1/logdata/<userid>/<float:latitude>/<float:longitude>/<int:weekday>/<int:hour>/<int:minutesQuant>`

#### Depricated Syntax
`http://mydomain.com/logdata/<string uuid>/<float latitude>/<float longitude>/<int weekday>/<int hour>/<int minutes_quantized>`

#### Sample response

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

#### Syntax
`http://mydomain.com/location-predict/api/v1/predict-res/<userid>`

#### Depricated Syntax
`http://mydomain.com/logdata/<uuid>/predictlocation`

#### Sample response

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
