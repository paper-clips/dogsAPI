# Dog Picture Using an API

The program takes user input from the console and saves a picture of a dog to the user's computer. The user can retrieve a dog picture of a specific dog breed, a random dog breed, or they have the option to list all the dog breeds to the console to select from.

## Prerequisites
Install these modules:
```
pip install requests
```
```
pip install rich
```

## Getting Started

To run the code:
```
python dogs.py
```

<br>Once everything is set up, you will be prompted in the console: 
> Name a dog breed (or type "random" or "list" or "end"): 
<br>

``` random ``` - Will save a picture of a random dog breed

``` list ``` - Will list all of the available dog breeds to select from

``` pitbull ```, ``` shiba ```, ``` pug ```, etc. - Will save a picture of the specified dog breed

``` end ``` - Will end the program 

## Other

Dog API sources:
- [Dog API](https://dog.ceo/dog-api/documentation/breed) <br>
- [Random Dog API](https://dog.ceo/dog-api/documentation/random)
