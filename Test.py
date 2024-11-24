import requests

# Define the endpoint and image file path
url = "http://10.134.178.161/uploadImage"
file_path = "test-images/glass.png"

# Send the POST request with the image
with open(file_path, "rb") as file:
    response = requests.post(url, files={"file": file})

# Print the response as JSON
print(response.json())


