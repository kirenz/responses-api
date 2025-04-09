from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

client = OpenAI()


response = client.responses.create(
    model="gpt-4o-mini",
    input="What is the customer name in the file?",
    tools=[{
        "type": "file_search",
        "vector_store_ids": ["vs_67f62d2aac208191bc923243a54ed553"]
    }]
)

print(response.output_text)