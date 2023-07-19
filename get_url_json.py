"""
Step 1 : choose the url from where you need the informations
Step 2 : adapt file_path to the folder location where you want the new json and his name
"""

import requests
import json
import os

url = "https://api.realt.community/v1/token"

# Send a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()

    # Define the file path for the new JSON file
    file_path = "C:/Users/Asa/PycharmProjects/pythonProject3/Test.json"

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write the formatted JSON data to the new file
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print("JSON data imported and saved successfully.")
else:
    print("Failed to retrieve data from the API.")
