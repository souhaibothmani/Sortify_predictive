import requests
import time
import random
import os

# Use a static MAC address
mac_address = "00:1A:2B:3C:4D:5E"

# Generate 5 random digits
random_digits = random.randint(10000, 99999)

# Create the new file name
new_file_name = f"{mac_address}_{random_digits}.png"

# Define the endpoint and image file path
url = "http://10.134.178.161/uploadImage"
file_path = "test-images/glass.png"

# Start measuring time
start_time = time.time()

# Rename the file by copying it with the new name
new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
os.rename(file_path, new_file_path)

# Send the POST request with the renamed image
with open(new_file_path, "rb") as file:
    response = requests.post(url, files={"file": file})

# Calculate the elapsed time
elapsed_time = time.time() - start_time

# Print the response as JSON
print(response.json())

# Print the time taken for the request
print(f"Time taken for the request: {elapsed_time:.2f} seconds")

# Optionally, rename the file back to its original name or remove it after use
# os.rename(new_file_path, file_path)  # Uncomment this line if you want to rename it back to the original name
# or delete the temporary file if not needed
# os.remove(new_file_path)  # Uncomment this if you want to delete the renamed file




