import os
import subprocess

# Get AWS credentials from environment variables
some_key = os.getenv('some_key')

# Check if AWS credentials are not None
if some_key is None:
    print("some key not found")
    exit(1)

# Write the key to a text file
file_path = os.getcwd()
with open(file_path, 'w') as file:
    file.write(some_key)

# Commit and push the changes
subprocess.run(['git', 'add', file_path])
subprocess.run(['git', 'commit', '-m', 'Update key'])
subprocess.run(['git', 'push'])