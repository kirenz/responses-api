"""
get_vector_store_id.py
---------------------
This script demonstrates how to list all vector stores available in your OpenAI account.

- Loads environment variables (such as the OpenAI API key) from a .env file.
- Initializes the OpenAI client.
- Lists all vector stores and prints their details.

Requirements:
- openai
- python-dotenv
- A valid OpenAI API key in your .env file
"""
from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client (uses OPENAI_API_KEY from environment)
client = OpenAI()

# List all vector stores in your account
vector_stores = client.vector_stores.list()
print(vector_stores)