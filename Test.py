import requests
import time

# Use a static MAC address
mac_address = "00:1A:2B:3C:4D:5E"

# Define the endpoint and image file path
url = "http://10.134.178.161/uploadImage"
file_path = "test-images/glass.jpeg"  # Ensure this is a valid JPEG file path

# Start measuring time
start_time = time.time()

# Send the POST request with the image file as raw JPEG data
with open(file_path, "rb") as file:
    headers = {
        "Content-Type": "image/jpeg",      # Set the Content-Type header to image/jpeg
        "X-MAC-Address": mac_address      # Add the MAC address as a custom header
    }
    response = requests.post(url, data=file, headers=headers)

# Calculate the elapsed time
elapsed_time = time.time() - start_time

# Print the response as JSON
try:
    print(response.json())  # Try to parse JSON response
except ValueError:
    print("Response is not JSON:", response.text)  # Fallback if response is not JSON

# Print the time taken for the request
print(f"Time taken for the request: {elapsed_time:.2f} seconds")
