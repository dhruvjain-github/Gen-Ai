from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

# doccument through which we have to search
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]
# what we have to search
query='tell me about bumrah'

embedding_model= OpenAIEmbeddings(model="text-embedding-3-small",dimensions=100)

doc_embedding= embedding_model.embed_documents(documents)
query_embedding= embedding_model.embed_query(query)

score=cosine_similarity([query_embedding],doc_embedding)[0]


index,score= sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(documents[index])
print("Similaritty score is ",score)

