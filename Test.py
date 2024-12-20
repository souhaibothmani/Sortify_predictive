import requests
from PIL import Image
import time

# Define server details and image paths
url = "http://10.134.178.161/uploadImage"  # Replace with your server's endpoint
original_image_path = "test-images/cardboard.jpeg"  # Path to the original image
optimized_image_path = "test-images/optimized_cardboard.jpeg"  # Path for optimized image

# Static MAC address
mac_address = "00:1A:2B:3C:4D:5S"


# Function to resize and compress the image
def optimize_image(input_path, output_path, size=(500, 500), quality=80):
    with Image.open(input_path) as img:
        img = img.resize(size)  # Resize the image
        img.save(output_path, format="JPEG", quality=quality)  # Compress the image


# Optimize the image before sending
print("Optimizing image...")
optimize_image(original_image_path, optimized_image_path)
print(f"Image optimized and saved to {optimized_image_path}")

# Start measuring time
start_time = time.time()

# Send the optimized image
with open(optimized_image_path, "rb") as file:
    headers = {
        "Content-Type": "image/jpeg",  # Image content type
        "X-MAC-Address": mac_address,  # Custom header for MAC address
        "Connection": "keep-alive"  # Reuse the TCP connection
    }
    try:
        print("Sending image to server...")
        response = requests.post(url, data=file, headers=headers, timeout=10)  # 10-second timeout
        elapsed_time = time.time() - start_time  # Calculate elapsed time

        # Print server response
        if response.status_code == 200:
            print(f"Response: {response.json()}")  # Parse JSON if possible
        else:
            print(f"Failed with status code: {response.status_code}")
            print(f"Response: {response.text}")

        print(f"Time taken for the request: {elapsed_time:.2f} seconds")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
