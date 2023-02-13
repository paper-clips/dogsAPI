import requests
from rich.console import Console
import csv
import json

class DogFunctions:
    # Constructor
    def __init__(self):
        self.console = Console()

    # Retrieve data from API using GET request
    def getRequest(self, breed):
        if breed == "random":
            return requests.get("https://dog.ceo/api/breeds/image/random")  # Random dog breed
        else:
            return requests.get("https://dog.ceo/api/breed/" + breed + "/images/random")    # Specific dog breed

    # Verify API request, exit app if error
    def verifyAPIRequest(self, response, breed):
        if response.status_code != 200:
            # API request not successful
            self.console.print("Unsuccessful API request.", style="bold red")
            exit()
        # Check whether the user specified a valid dog breed (also whether the GET request returned a dog picture)
        if breed != "random" and breed != "list":
            if 'message' not in response.json():
                # Invalid breed (or other issues), ask for input again
                self.console.print("Invalid input type.", style="bold red")
                return False
        if not response.json()["message"].startswith("https://images.dog.ceo/breeds/"):
            # Invalid URL
            # May remove, verifies that the return isn't from another source
            self.console.print("Invalid return address. (On the API's end)", style="bold red")
            exit()
        return True

    # Print JSON Objects that are returned from GET request to debug
    def printJSONObjects(self, response):
        print(json.dumps(response.json(), indent=4))   

    # Retrieve image and save it to the computer
    def saveImage(self, response):
        web_image = requests.get(response.json()["message"]).content
        with open('dogImage.jpg', 'wb') as img:
            img.write(web_image)

    # Get user input (Also change - to / (ex: terrier-fox --> terrier/fox) since the breed will be passed as URL)
    def getInput(self):
        breed = input("Name a dog breed (or type \"random\" or \"list\" or \"end\"): ")
        breed = breed.replace("-", "/")
        return breed

    # List all the dog breeds to choose from
    def listDogBreeds(self):
        print("Breeds list:")
        # Open CSV file
        with open('dogBreedsCSV.csv', 'r') as dogBreedsCSV:
            dogBreeds = csv.reader(dogBreedsCSV)
            # Print each dog breed to console
            for dogBreed in dogBreeds:
                for d in range(len(dogBreed)):
                    self.console.print(dogBreed[d], style="blue")

    # Prints that the image was found (also changes / to - in the breed name)
    def printImageFound(self, breed):
        breed = breed.replace("/", "-")
        if breed == "random":
            self.console.print("Image found!", style="bold green")
        else:
            self.console.print(breed.capitalize() + " image found!", style="bold green")
        return breed

# --------------------------------------------------------------------------------------- #

def main():
    dogs = DogFunctions()

    # Get dog breed from user
    breed = dogs.getInput()

    # Loops until user types "end"
    while breed != "end":
        # Random dog picture
        if breed == "random":
            response = dogs.getRequest(breed)
            #printJSONObjects(response)     # To debug

            dogs.verifyAPIRequest(response, breed)

            dogs.saveImage(response)

            breed = dogs.printImageFound(breed)
        # List breed types
        elif breed == "list":
            dogs.listDogBreeds()
        # Specific dog breed picture
        else:
            response = dogs.getRequest(breed)
            #printJSONObjects(response)     # To debug

            # Verify input and API request, exit app if errors
            isValid = dogs.verifyAPIRequest(response, breed)
            if isValid == False:
                breed = dogs.getInput()
                continue

            dogs.saveImage(response)

            breed = dogs.printImageFound(breed)

        # Get input again
        breed = dogs.getInput()

if __name__=="__main__":
    main()