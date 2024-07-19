import subprocess

command = "pymon src/main.py"

process = subprocess.Popen(command, shell=True)

process.wait()
