import requests

API_URL = "http://127.0.0.1:8000/add-app/"

device_info = {
    "app_name": "VirtualDeviceApp",
    "version": "2.1",
    "description": "Data sent from virtual Android system"
}

response = requests.post(API_URL, json=device_info)

if response.status_code == 201:
    print("Data sent successfully:", response.json())
else:
    print("Failed to send data:", response.text)
