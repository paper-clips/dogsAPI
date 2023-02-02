import requests
#import json

# API GET request
response = requests.get("https://dog.ceo/api/breed/hound/images/random")
#print(json.dumps(response.json(), indent=4))       # Print request info

# Verify input
if response.json()["status"] != "success":
    # API request not successful
    print("Unsuccessful API request.")
    exit()
if not response.json()["message"].startswith("https://images.dog.ceo/breeds/"):
    # Invalid URL
    print("Not correct website.")
    exit()

# Retrieve and save image
web_image = requests.get(response.json()["message"]).content
with open('dogImage.jpg', 'wb') as img:
    img.write(web_image)

print("---------------------------------")