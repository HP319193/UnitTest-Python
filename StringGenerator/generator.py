import random
import string

class RandomStringGenerator:
    def __init__(self, length=8):
        """
        Initialize the RandomStringGenerator with a default length.
        
        :param length: The length of the random string to generate. Default is 8.
        """
        self.length = length

    def generate(self):
        """
        Generate a random string of the specified length.
        
        :return: A random string containing letters and digits.
        """
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(self.length))
        return random_string
