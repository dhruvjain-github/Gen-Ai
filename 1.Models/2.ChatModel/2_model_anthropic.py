from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

# we have not purchased the antropic credits
model= ChatAnthropic(model="")

result=model.invoke("What is the capital of India")

print(result.content)