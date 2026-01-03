from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatOpenAI()

template1=PromptTemplate(
    template='give me a detailed report on {topic}',
    input_variables='topic'
)

template2=PromptTemplate(
    template='give me a brief summry of 5 lines on {topic}',
    input_variables='topic'
)

prompt1=template1.invoke({'topic':'black hole'})

result=model.invoke(prompt1)

# print(result)

prompt2=template2.invoke({'topic':result.content})

final_result=model.invoke(prompt2)

print(final_result)