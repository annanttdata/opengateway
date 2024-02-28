import time
import http.client
import json

def open_program():
    """
    Function to display a welcome message.
    """
    print("Welcome to the Dog-H 1.0.")
    #time.sleep(3);

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
    #time.sleep(3);

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
    #print(f"Scheduled pause of {seconds} seconds.")
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
    #result = "Using the profile: " + dataToPrint["qosProfile"] + "on the device number " + dataToPrint["device"]["phoneNumber"]
    #return result


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
    print("Demo ended.")

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

location = get_wrong_location()
lost_location(location)
scheduled_pause(2)
send_improve_signal_message()
scheduled_pause(5)
print("Location obtained successfully.")
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
