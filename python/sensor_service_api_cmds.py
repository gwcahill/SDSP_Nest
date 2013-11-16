# Standard Python imports
import requests
import time

TEMPERATURE = "temp"
LIGHT = "light"
PRESSURE = "pressure"
HUMIDITY = "humidity"
MOTION = "motion"
SENSOR_API = "http://einstein.sv.cmu.edu/sensors"
    
def _getCurrentTimestamp():
    current_time = int(str(time.time()).split('.')[0])*1000
    return current_time

def getDeviceCurrentTemperature(device_uri):
    current_time = _getCurrentTimestamp()
    response = requests.get("%s/%s/%s/%s/json" % (SENSOR_API, device_uri, current_time, TEMPERATURE))
    return response.json()['value']
    
def getDeviceCurrentLight(device_uri):
    current_time = _getCurrentTimestamp()
    response = requests.get("%s/%s/%s/%s/json" % (SENSOR_API, device_uri, current_time, LIGHT))
    return response.json()['value']

def getDeviceCurrentPressure(device_uri):
    current_time = _getCurrentTimestamp()
    response = requests.get("%s/%s/%s/%s/json" % (SENSOR_API, device_uri, current_time, PRESSURE))
    return response.json()['value']

def getDeviceCurrentHumidity(device_uri):
    current_time = _getCurrentTimestamp()
    response = requests.get("%s/%s/%s/%s/json" % (SENSOR_API, device_uri, current_time, HUMIDITY))
    return response.json()['value']

def getDeviceCurrentMotion(device_uri):
    current_time = _getCurrentTimestamp()
    response = requests.get("%s/%s/%s/%s/json" % (SENSOR_API, device_uri, current_time, MOTION))
    return response.json()['value']
    

if __name__ == "__main__":
    # Get all available devices
    devices_response = requests.get("http://einstein.sv.cmu.edu/get_devices/json")
    devices = devices_response.json()
    
    # Loop through all devices and get sensor readings...
    for device in devices:
        device_uri = device.get('uri')
        device_location = device.get('device_location')
        temperature = getDeviceCurrentTemperature(device_uri)
        light = getDeviceCurrentLight(device_uri)
        pressure = getDeviceCurrentPressure(device_uri)
        humidity = getDeviceCurrentHumidity(device_uri)
        motion = getDeviceCurrentMotion(device_uri)
        
        # Print statement of sensor readings per device
        print("--------------------------------------")
        print("Device Id: %s  Room: %s" % (device_uri, device_location))
        print("Temperature: %s" % temperature)
        print("Light: %s" % light)
        print("Pressure: %s" % pressure)
        print("Humidity: %s" % humidity)
        print("Motion: %s" % motion)
        print("--------------------------------------")
        print("")
        
        
        
        