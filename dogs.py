import requests
import json

# Get dog breed from user
breed = input("Name a dog breed (or type random): ")

# Random dog picture
if breed == "random":
    # API GET request
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    #print(json.dumps(response.json(), indent=4))       # Print request info to debug

    # Verify API request, exit app if error
    if response.status_code != 200:
        # API request not successful
        print("Unsuccessful API request.")
        exit()

    # Retrieve and save image
    web_image = requests.get(response.json()["message"]).content
    with open('dogImage.jpg', 'wb') as img:
        img.write(web_image)

    print("Image found!")
# Specific dog breed picture
else:
    # API GET request
    response = requests.get("https://dog.ceo/api/breed/" + breed + "/images/random")
    #print(json.dumps(response.json(), indent=4))       # Print request info to debug

    # Verify input and API request, exit app if errors
    if response.status_code != 200:
        # API request not successful
        print("Unsuccessful API request.")
        exit()
    if 'message' not in response.json():
        # Invalid breed
        print("Invalid breed type.")
        exit()
    if not response.json()["message"].startswith("https://images.dog.ceo/breeds/"):
        # Invalid URL
        print("Invalid return address. (On the API's end)")
        exit()

    # Retrieve and save image
    web_image = requests.get(response.json()["message"]).content
    with open('dogImage.jpg', 'wb') as img:
        img.write(web_image)

    print(breed.capitalize() + " image found!")

print("---------------------------------")