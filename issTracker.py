import requests
import time
import sys
import json

r = requests.get('http://api.open-notify.org/iss-now.json')
if not r.status_code in (200, 202):
    sys.exit(-1)

# Only if the status code was 200 or 202, will this code be executed.
resp = r.json()
iss_latitude = resp['latitude']
iss_longitude = resp['longitude']
iss_altitude = resp['altitude']
iss_velocity = resp['velocity']

# Data for the ISS position
def get_iss_data():
    iss_api = 'http://www.isstracker.com/home.json'
    request = requests.get(iss_api).json()

    # Print the position and velocity (KM/H, MPH)
    print(f'''
        ---------------------------
        Real-time ISS Location:
        ---------------------------
        Altitude: {request['altitude']}
        Latitude: {request['latitude']}
        Longitude: {request['longitude']}
        Velocity (KM/H): {request['velocity']}
        Velocity (MPH): {request['velocity'] / 1.60934}
        ---------------------------
        ''')

# Return the position 3 times, wait 5 seconds
def iss_current_data():
    for i in range(3):
        get_iss_data()
        time.sleep(5)


iss_current_data()
