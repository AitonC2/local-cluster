# This class is intended to run powershell commands and capture it's outputs
# In order to get the desired information from the command line
import subprocess
import os
import sys

# gets the current user account directory
userprofile = os.getenv('UserProfile')

# sets the location for the events dump file
dump_file = str(userprofile + "\\AppData\\Local\\Temp")

# runs a powershell command given an argument
def powershell_command(arg):
    subprocess.run(["powershell", "-Command", arg], capture_output=True)
