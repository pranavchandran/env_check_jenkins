import os

# Get AWS credentials from environment variables
some_key = os.getenv('some_key')

# Check if AWS credentials are not None
if some_key is None:
    print("some key not found")
    exit(1)

# Write the key to a text file
with open('key.txt', 'w') as file:
    file.write(some_key)