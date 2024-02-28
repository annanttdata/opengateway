from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
import network_as_code as nac
from network_as_code.models.location import CivicAddress, Location
from network_as_code.models.device import Device, DeviceIpv4Addr

import time
import http.client
import json


def open_program():
    """
    Function to display a welcome message.
    """
    print("Welcome to the Dog-H 1.0.")

def initialize_robot():
    """
    Function to initialize the robot.
    """
    conn = http.client.HTTPSConnection("device-status.p-eu.rapidapi.com")

    payload = "{\r\n    \"subscriptionDetail\": {\r\n    \"device\": {\r\n     \"phoneNumber\": \"21431000020\"\r\n        },\r\n        \"eventType\": \"CONNECTIVITY\"\r\n    },\r\n    \"subscriptionExpireTime\": \"2024-02-29T18:21:29\",\r\n    \"maxNumberOfReports\": 5,\r\n    \"webhook\": {\r\n        \"notificationUrl\": \"https://example.com/notifications\",\r\n        \"notificationAuthToken\": \"cb7fd045f8mshf68438ee8eedb74p143d09jsncf547d5a063b\"\r\n    }\r\n}"

    headers = {
        'content-type': "application/json",
        'X-RapidAPI-Key': "cb7fd045f8mshf68438ee8eedb74p143d09jsncf547d5a063b",
        'X-RapidAPI-Host': "device-status.nokia.rapidapi.com"
    }

    conn.request("POST", "/event-subscriptions", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print("Robot initialized.")
    # Load the JSON string into a dictionary
    dataToPrint = json.loads(data)
    # Accessing specific elements
    print("Device Phone Number:", dataToPrint["subscriptionDetail"]["device"]["phoneNumber"])

def get_location():
    """
    Function to obtain the location.
    """
    # Here, we simulate obtaining the location.
    conn = http.client.HTTPSConnection("location-retrieval.p-eu.rapidapi.com")

    payload = "{\r\n    \"device\": {\r\n        \"phoneNumber\": \"21431000020\"\r\n    },\r\n    \"maxAge\": 60\r\n}"

    headers = {
        'content-type': "application/json",
        'X-RapidAPI-Key': "cb7fd045f8mshf68438ee8eedb74p143d09jsncf547d5a063b",
        'X-RapidAPI-Host': "location-retrieval.nokia.rapidapi.com"
    }

    conn.request("POST", "/retrieve", payload, headers)

    res = conn.getresponse()
    data = res.read()
    # Load the JSON string into a dictionary
    dataToPrint = json.loads(data)
    # Accessing specific elements
    result = "Address: " + dataToPrint["civicAddress"]["A1"] + "," + dataToPrint["civicAddress"]["A2"]
    return result

def confirm_location(location):
    """
    Function to confirm the location.
    """
    print("Location confirmed:", location)

def get_wrong_location():
    """
    Function to obtain the location with errors.
    """
    # Here, we simulate obtaining the location.
    conn = http.client.HTTPSConnection("location-verification.p-eu.rapidapi.com")

    payload = "{\r\n    \"device\": {\r\n        \"phoneNumber\": \"21431000020\" \r\n    },\r\n    \"area\": {\r\n        \"areaType\": \"Circle\",\r\n        \"center\": {\r\n            \"latitude\": 41.359624196788616,\r\n            \"longitude\": 2.1187637707026745\r\n        },\r\n        \"radius\": 10\r\n    },\r\n    \"maxAge\": 60\r\n}"

    headers = {
        'content-type': "application/json",
        'X-RapidAPI-Key': "cb7fd045f8mshf68438ee8eedb74p143d09jsncf547d5a063b",
        'X-RapidAPI-Host': "location-verification.nokia.rapidapi.com"
    }

    conn.request("POST", "/verify", payload, headers)

    res = conn.getresponse()
    data = res.read()
    # Load the JSON string into a dictionary
    dataToPrint = json.loads(data)
    # Accessing specific elements
    result = "Verification result: " + dataToPrint["verificationResult"]
    return result

def lost_location(location):
    """
    Function to confirm the location.
    """
    print("Location lost:", location)

def scheduled_pause(seconds):
    """
    Function to perform a scheduled pause.
    """
    time.sleep(seconds)

def send_improve_signal_message():
    """
    Function to send a message on screen to improve the signal.
    """
    print("Error: Location unreachable. Improving signal...")
    
    conn = http.client.HTTPSConnection("quality-of-service-on-demand.p-eu.rapidapi.com")

    payload = "{\r\n    \"qosProfile\": \"DOWNLINK_L_UPLINK_L\",\r\n    \"device\": {\r\n        \"phoneNumber\": \"21431000020\",\r\n        \"ipv4Address\": {\r\n            \"publicAddress\": \"1.1.1.1\"\r\n        }\r\n    },\r\n    \"applicationServer\": {\r\n        \"ipv4Address\": \"233.252.0.2\",\r\n        \"ipv6Address\": \"2001:db8:1234:5678:9abc:def0:fedc:ba98\"\r\n    },\r\n    \"duration\": \"60\",\r\n    \"notificationUrl\": \"https://example.com/notifications\",\r\n    \"notificationAuthToken\": \"cb7fd045f8mshf68438ee8eedb74p143d09jsncf547d5a063b\"\r\n}"

    headers = {
        'content-type': "application/json",
        'X-RapidAPI-Key': "cb7fd045f8mshf68438ee8eedb74p143d09jsncf547d5a063b",
        'X-RapidAPI-Host': "quality-of-service-on-demand.nokia.rapidapi.com"
    }

    conn.request("POST", "/sessions", payload, headers)

    res = conn.getresponse()
    data = res.read()

    # Load the JSON string into a dictionary
    dataToPrint = json.loads(data)

    # Accessing specific elements
    print("Using the Profile:", dataToPrint["qosProfile"])
    print("on the Device Phone Number:", dataToPrint["device"]["phoneNumber"])

def send_emergency_request():
    """
    Function to request emergency assistance for the owner's health.
    """
    print("Requesting emergency assistance for the owner's health.")

def alert_emergency_services():
    """
    Function to alert doctor, ambulance, and private emergency contact.
    """
    print("Alert sent to doctor, ambulance, and private emergency contact.")

def turn_off_emergency_signal():
    """
    Function to turn off the emergency signal.
    """
    print("Emergency signal turned off.")

def end_demo():
    """
    Function to end the demo.
    """
    print("Device is working.")

# Transferred steps in sequential order:

open_program()
scheduled_pause(2)
initialize_robot()
scheduled_pause(2)

location = get_location()
confirm_location(location)

scheduled_pause(5)

location = get_location()
confirm_location(location)

scheduled_pause(5)

location = get_location()
confirm_location(location)

scheduled_pause(5)

location = get_wrong_location()
lost_location(location)
scheduled_pause(2)

send_improve_signal_message()
scheduled_pause(5)
print("Location obtained successfully.")

location = get_location()
confirm_location(location)

scheduled_pause(5)

location = get_location()
confirm_location(location)

scheduled_pause(5)

location = get_location()
confirm_location(location)

scheduled_pause(5)

send_emergency_request()
scheduled_pause(3)
alert_emergency_services()
scheduled_pause(5)


location = get_location()
confirm_location(location)
scheduled_pause(5)

location = get_location()
confirm_location(location)
scheduled_pause(5)

location = get_location()
confirm_location(location)
scheduled_pause(5)


turn_off_emergency_signal()

end_demo()




app = Flask(__name__)
CORS(app)

phone_number = '21431000020'
phone_id = uuid.uuid4()
token_nac = '65c04ac140mshc4cf416ef811741p14e7eajsnbef39249379c'

@app.route('/localization', methods=['GET'])
def get_localization():
    # Here we will get from the dog-care device the geographic coordinates based from dog-care API directly
    longitude = 2.1187637707026745
    latitude = 41.359624196788616
    
    # Begin with the client object followed by the NetworkAsCodeClient() method and client's token:
    client = nac.NetworkAsCodeClient(
        token=token_nac
    )
    
    # This step will require the External Identifier, IP and ports input:
    device = client.devices.get(phone_number = phone_number,
                                ipv4_address = "1.1.1.1"
    )
    
    # print(jsonify({'gps': {'longitude': longitude, 'latitude': latitude}, 'network_as_code': {'longitude': location.longitude, 'latitude': location.latitude, 'civic_address': location.civic_address}}))
    # In case location is not the same from GPS and Network, we can return both.
    if device.verify_location(longitude=longitude, latitude=latitude, radius=10, max_age=60):
        return jsonify({'gps': {'longitude': longitude, 'latitude': latitude}})
    else:
        # Create a location object followed by a method that will enable it:
        location = device.location(max_age=60)
        return jsonify({'gps': {'longitude': longitude, 'latitude': latitude}, 
                        'network_as_code': {'longitude': location.longitude, 'latitude': location.latitude}})

@app.route('/notifications', methods=['POST'])
def post_notifications():
    data = request.get_json()
    # Realizar alguna acción si el valor es true
    if data.get('event', {}).get('eventDetail', {}).get('deviceStatus') == "REACHABLE":
        # Perform some action if the value is "REACHABLE"
        print("REACHABLE")
    else:
        # Perform some action if the value is not "REACHABLE"
        print("Not REACHABLE")
        session = device.create_qod_session(
            service_ipv4="233.252.0.2", # here is the IP of the service itself
            service_ipv6="2001:db8:1234:5678:9abc:def0:fedc:ba98",
            profile="QOS_E" #better latency
        )
    return jsonify({'status': 'ok'})       


if __name__ == '__main__':
    # Begin with the client object followed by the NetworkAsCodeClient() method and client's token:
    client = nac.NetworkAsCodeClient(
        token = token_nac
    )
    
    # This step will require the External Identifier, IP and ports input:
    device = client.devices.get(phone_number = phone_number,
                                ipv4_address = "1.1.1.1"
    )
    
    subscription = client.connectivity.subscribe(
        event_type = "CONNECTIVITY",
        device = device,
        max_num_of_reports = 50,
        notification_url = "https://example.com/notifications", # Use HTTPS to send notifications
        notification_auth_token = phone_id.hex
    )
    app.run()
    
    subscription.delete()


