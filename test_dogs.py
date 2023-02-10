import unittest
from dogs import DogFunctions

class TestDogs(unittest.TestCase):
    # Check if API request is successful
    def test_getRequest(self):
        dogs = DogFunctions()
        self.assertEqual(dogs.getRequest("random").status_code, 200, msg="Unsuccessful API Request (random breed)")
        self.assertEqual(dogs.getRequest("hound").status_code, 200, msg="Unsuccessful API Request (hound breed)")
        self.assertEqual(dogs.getRequest("dane/great").status_code, 200, msg="Unsuccessful API Request (dane-great breed)")

# python -m unittest