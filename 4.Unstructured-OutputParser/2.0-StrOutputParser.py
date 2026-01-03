from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

parser=StrOutputParser()

chain= template1 | model | parser | template2 | model | parser

result=chain.invoke({'topic':'black-hole'})

print(result)