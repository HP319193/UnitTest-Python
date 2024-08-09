import subprocess

def run_unittest():
    # Define the command to run the unittest
    command = ['python', '-m', 'unittest', 'StringGenerator/test_generator.py']

    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the output and errors
    print("Output:\n", result.stdout)
    print("Errors:\n", result.stderr)

if __name__ == '__main__':
    run_unittest()