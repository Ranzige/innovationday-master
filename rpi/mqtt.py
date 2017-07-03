import ibmiotf.device
import combineData
try:
    options = {
        "org": "034pt5",
        "type": "MQTTDevice",
        "id": "donniemqttdevice1",
        "auth-method": "token",
        "auth-token": "zaq12wsx",
        "clean-session": "true"
    }
    client = ibmiotf.device.Client(options)
    client.connect()
    myData = combineData.main()
    client.publishEvent("status", "json", myData)
except ibmiotf.ConnectionException  as e:
        print e
