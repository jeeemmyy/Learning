import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

# Prints the name of the OS
print("OS name = ", os.name, "\n")

# Check for item existence & type
print("Item exists: " + str(path.exists("text.txt")))
print("Item is a file: " + str(path.isfile("text.txt")))
print("Item is a directory: " + str(path.isdir("text.txt")))

# Working with PATHS
print("Real PATH = " + str(path.realpath("text.txt")))
print("Real PATH = " + str(path.split(path.realpath("text.txt"))) + "\n")


# Get the file modification time
print("File modification time: " + str(time.ctime(path.getmtime("text.txt"))))
