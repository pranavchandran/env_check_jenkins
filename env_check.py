import os
import subprocess

# Get AWS credentials from environment variables
some_key = os.getenv('some_key')
original_key = some_key.split(':')[1]

# Write the key to a text file

with open('key.txt', 'w') as file:
    file.write(original_key)
