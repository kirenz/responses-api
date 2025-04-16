# Responses API

This repository provides educational examples for working with the OpenAI API, focusing on vector stores and web search tools. The code is designed to help you understand how to create, manage, and query vector stores, as well as how to use web search capabilities with OpenAI models.

## Project Structure

- `responses_vector.py`: Demonstrates how to create a vector store and upload a file for semantic search.

- `get_vector_store_id.py`: Shows how to list all vector stores in your OpenAI account.

- `vector_query.py`: Explains how to query a vector store using a natural language prompt.

- `responses_web.py`: Demonstrates how to use the web search tool to retrieve current information from the web.

- `example.txt`: Example file used for uploading to the vector store.

- `pyproject.toml`, `uv.lock`: Project dependencies and environment management files.

## Setup Instructions

1. **Install dependencies**
   
```bash
uv sync
```
   

2. **Set up your environment**

- Create a `.env` file in the project root with your OpenAI 


3. **Run the examples**

- To create a vector store and upload a file:

```bash
python responses_vector.py
```

- To list your vector stores:

```bash
python get_vector_store_id.py
```

To query a vector store:
```bash
python vector_query.py
```

- To use the web search tool:

```bash
python responses_web.py
```

## Educational Notes

- **Vector Stores**: These are databases optimized for storing and searching high-dimensional vectors, such as document embeddings. You can upload files and then query them semantically using natural language.

- **Web Search Tool**: Allows the model to access up-to-date information from the web, which is useful for questions about current events.

- **Environment Variables**: The `.env` file is used to securely store your API key and other sensitive information.



