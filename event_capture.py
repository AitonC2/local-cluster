# This class is intended to run powershell commands and capture it's outputs
# In order to get the desired information from the command line
import subprocess
import os

# gets the current user account temp directory
file_path = os.getenv('Temp')


# runs a powershell command given an argument
def powershell_command(arg):
    subprocess.run(["powershell", "-Command", arg], capture_output=True)
