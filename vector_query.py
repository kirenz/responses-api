"""
vector_query.py
----------------
This script demonstrates how to use the OpenAI API to query a vector store for information using a natural language prompt.

- Loads environment variables (such as the OpenAI API key) from a .env file.
- Initializes the OpenAI client.
- Sends a query to a specific vector store using the 'file_search' tool.
- Prints the response from the model.

Requirements:
- openai
- python-dotenv
- A valid OpenAI API key in your .env file
- A vector store already created and populated with files
"""
from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client (uses OPENAI_API_KEY from environment)
client = OpenAI()

# Query the vector store with a natural language question
response = client.responses.create(
    model="gpt-4o-mini",
    input="What is the customer name in the file?",
    tools=[{
        "type": "file_search",
        "vector_store_ids": ["vs_67f62d2aac208191bc923243a54ed553"]
    }]
)

# Print the model's answer
print(response.output_text)