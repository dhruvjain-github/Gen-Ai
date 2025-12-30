from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding= OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)

document = [
    "New Delhi is the capital of India",
    "Washington, D.C. is the capital of the United States",
    "London is the capital of the United Kingdom",
    "Paris is the capital of France",
    "Tokyo is the capital of Japan"
]

result=embedding.embed_documents(document)

print(str(result))