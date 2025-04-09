from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

client = OpenAI()

vector_store = client.vector_stores.create(        # Create vector store
    name="Support FAQ",
)

client.vector_stores.files.upload_and_poll(        # Upload file
    vector_store_id=vector_store.id,
    file=open("customer_policies.txt", "rb")
)


vector_store_id=vector_store.id

print("Vector store ID:", vector_store_id)