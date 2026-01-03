from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated

load_dotenv()

model=ChatOpenAI()

text = "The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this."


# simple
class Review(TypedDict):
    summary:str
    sentiment:str

simple_structured_model= model.with_structured_output(Review)

result=simple_structured_model.invoke(text)

# print(result)
# print(result["summary"])
# print(result["sentiment"])


# anotated
# sometime our name of vairable ('summary') is not explainarty so what happens is we neet to pass the description to the model there we use annotated .
# it is not compulsary that all variable must be of same type
class Review2(TypedDict):
    summary:Annotated[str,"A brief summary of the review"]
    sentiment:str

anotated_structured_model= model.with_structured_output(Review2)

result2=anotated_structured_model.invoke(text)

# print(result2)
print(result2["summary"])
print(result2["sentiment"])
