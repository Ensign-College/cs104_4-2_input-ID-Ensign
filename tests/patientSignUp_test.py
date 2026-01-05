import subprocess
import sys
import os
from difflib import SequenceMatcher

# TEST SETUP
script_path = os.path.join(os.path.dirname(__file__), '..', 'patientSignUp.py')
script_path = os.path.abspath(script_path)

simulated_input = 'Test Name\n104\n' # Simulate user input for name and age

result = subprocess.run(
	[sys.executable, script_path],
	input=simulated_input,
	capture_output=True,
	text=True
)

output = result.stdout.strip()

with open(script_path, 'r') as file:
		code = file.read()


# TESTS
def test_patientSignUp_message():
    assert output, "❌ patientSignUp.py does not print anything. Hint: make sure to use the print() function!"

    expected = """
Welcome to VitalLink! Let's get you signed up for our healthcare services.

Please enter your full name: Test Name
Please enter your age: 104

Thank you for signing up! We have created a new record for Test Name, age 104.
""".strip()

    # Calculate similarity ratio
    similarity = SequenceMatcher(None, output, expected).ratio()

    assert similarity >= 0.8, (
        f"❌ patientSignUp.py does not print out the correct sign-up message.\n"
        f"Hint: make sure running `py patientSignUp.py` prints text like this:\n"
        f"\n{expected}\n"
    )
    print("✅ patientSignUp.py prints the correct sign-up message.")

    
def test_patientSignUp_input_usage():
	assert 'input(' in code, "❌ patientSignUp.py does not use the input() function. Hint: use input() to ask for the user's name and age."
	print("✅ patientSignUp.py uses the input() function.")

def test_patientSignUp_variable_usage():
	assert '=' in code, "❌ patientSignUp.py does not use variables. Hint: create variables like 'name' and 'age'."
	print("✅ patientSignUp.py uses variables.")

def test_patientSignUp_print_variables():
	assert 'Test Name' in output, "❌ patientSignUp.py does not print the user's name. Hint: use the variables in the final print statement."
	print("✅ patientSignUp.py prints the user's name correctly.")
	assert '104' in output, "❌ patientSignUp.py does not print the user's age. Hint: use the variables in the final print statement."
	print("✅ patientSignUp.py prints the user's age correctly.")