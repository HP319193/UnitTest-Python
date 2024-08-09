import unittest
from StringGenerator.generator import RandomStringGenerator  # Replace with your actual module and class names

class TestYourClass(unittest.TestCase):

    def test_function_contains_key(self):
        instance = RandomStringGenerator()
        result = instance.generate()  # Replace with the actual function you want to test

        # Check if the result is a dictionary
        self.assertIsInstance(result, str, "The result should be a dictionary")

        # Check if the specific key is in the result
        # self.assertIn('your_key', result, "The result should contain the key 'your_key'")

if __name__ == '__main__':
    unittest.main()