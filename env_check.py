import os

# Get AWS credentials from environment variables
some_key = os.getenv('some_key')
print(some_key)

# Check if AWS credentials are not None
if some_key is None:
    print("some key not found")
    exit(1)


