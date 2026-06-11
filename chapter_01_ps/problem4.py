# Import the os module
import os

# Get the list of files and folders in the current directory
contents = os.listdir()

# Print a heading
print("Contents of the current directory:")

# Print each file/folder name
for item in contents:
    print(item)