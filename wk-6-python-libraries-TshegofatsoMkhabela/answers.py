import os
import requests
from urllib.parse import urlparse
from datetime import datetime

def fetch_image():
    # Prompt the user for a URL
    url = input("Enter the URL of the image you want to fetch: ").strip()
    
    if not url:
        print("No URL entered. Exiting...")
        return
    
    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the image: {e}")
        return
    
    # Get the directory where this Python file resides
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create "Fetched_Images" folder inside the script directory
    images_dir = os.path.join(script_dir, "Fetched_Images")
    os.makedirs(images_dir, exist_ok=True)
    
    # Extract filename or generate one
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    if not filename or '.' not in filename:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"image_{timestamp}.jpg"
    
    file_path = os.path.join(images_dir, filename)
    
    # Save image in binary mode
    try:
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Image saved successfully as: {file_path}")
    except IOError as e:
        print(f"Error saving the image: {e}")

if __name__ == "__main__":
    fetch_image()
