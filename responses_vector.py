"""
responses_vector.py
------------------
This script demonstrates how to create a new vector store using the OpenAI API and upload a file to it for semantic search purposes.

- Loads environment variables (such as the OpenAI API key) from a .env file.
- Initializes the OpenAI client.
- Creates a new vector store named 'Support FAQ'.
- Uploads a file (example.txt) to the vector store and waits for the upload to complete.
- Prints the ID of the created vector store.

Requirements:
- openai
- python-dotenv
- A valid OpenAI API key in your .env file
- A file named 'example.txt' in the project directory
"""
from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client (uses OPENAI_API_KEY from environment)
client = OpenAI()

# Create a new vector store for storing and searching documents
vector_store = client.vector_stores.create( 
    name="Support FAQ",
)

# Upload a file to the vector store and wait for completion
client.vector_stores.files.upload_and_poll(
    vector_store_id=vector_store.id,
    file=open("example.txt", "rb")
)

# Store and print the vector store ID for later use
vector_store_id=vector_store.id
print("Vector store ID:", vector_store_id)