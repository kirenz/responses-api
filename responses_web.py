"""
responses_web.py
----------------
This script demonstrates how to use the OpenAI API with the web search tool to retrieve up-to-date information from the web.

- Loads environment variables (such as the OpenAI API key) from a .env file.
- Initializes the OpenAI client.
- Uses the 'web_search_preview' tool to ask for a positive news story from today in Germany.
- Prints the model's response.

Requirements:
- openai
- python-dotenv
- A valid OpenAI API key in your .env file
"""
from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Now you can access your API key
# OpenAI client will automatically use OPENAI_API_KEY environment variable

client = OpenAI()

# Use the web_search_preview tool to get current news
response = client.responses.create(
    model="gpt-4o-mini",
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today in Germany?"
)

# Print the model's answer
print(response.output_text)
