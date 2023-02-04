import requests
import json

# Get dog breed from user
breed = input("Name a dog breed: ")

# API GET request
response = requests.get("https://dog.ceo/api/breed/" + breed + "/images/random")
print(json.dumps(response.json(), indent=4))       # Print request info to debug

# Verify input and API request, exit app if errors
if response.json()["status"] != "success":
    # API request not successful
    print("Unsuccessful API request.")
    exit()
isMessageFound = False
# for key,value in response.content.items():
#     if value == "message":
#         isMessageFound = True
#         break
#     print(value)
# if isMessageFound == False:
#     # Invalid dog breed
#     print("Breed not correct.")
#     exit()
if not response.json()["message"].startswith("https://images.dog.ceo/breeds/"):
    # Invalid URL
    print("Not correct website.")
    exit()

# Retrieve and save image
web_image = requests.get(response.json()["message"]).content
with open('dogImage.jpg', 'wb') as img:
    img.write(web_image)

print("---------------------------------")