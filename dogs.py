import requests
from rich.console import Console
#import json

console = Console()

# Get dog breed from user
breed = input("Name a dog breed (or type \"random\" or \"list\"): ")

# Random dog picture
if breed == "random":
    # API GET request
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    #print(json.dumps(response.json(), indent=4))       # Print request info to debug

    # Verify API request, exit app if error
    if response.status_code != 200:
        # API request not successful
        console.print("Unsuccessful API request.", style="bold red")
        exit()

    # Retrieve and save image
    web_image = requests.get(response.json()["message"]).content
    with open('dogImage.jpg', 'wb') as img:
        img.write(web_image)

    console.print("Image found!", style="bold green")
# List breed types
elif breed == "list":
    print("Breeds list:")
# Specific dog breed picture
else:
    # API GET request
    response = requests.get("https://dog.ceo/api/breed/" + breed + "/images/random")
    #print(json.dumps(response.json(), indent=4))       # Print request info to debug

    # Verify input and API request, exit app if errors
    if response.status_code != 200:
        # API request not successful
        console.print("Unsuccessful API request.", style="bold red")
        exit()
    if 'message' not in response.json():
        # Invalid breed
        console.print("Invalid breed type.", style="bold red")
        exit()
    if not response.json()["message"].startswith("https://images.dog.ceo/breeds/"):
        # Invalid URL
        console.print("Invalid return address. (On the API's end)", style="bold red")
        exit()

    # Retrieve and save image
    web_image = requests.get(response.json()["message"]).content
    with open('dogImage.jpg', 'wb') as img:
        img.write(web_image)

    console.print(breed.capitalize() + " image found!", style="bold green")
