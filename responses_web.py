from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Now you can access your API key
# OpenAI client will automatically use OPENAI_API_KEY environment variable

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today in Germany?"
)

print(response.output_text)
