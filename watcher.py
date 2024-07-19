import subprocess

# Command to run
command = "pymon src/main.py"

# Use subprocess to run the command
process = subprocess.Popen(command, shell=True)

# Wait for the command to complete
process.wait()