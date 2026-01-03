from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatOpenAI()

topic=input('Enter the topic: ')
parser=JsonOutputParser()

template1=PromptTemplate(
    template="generate a course guide on topic {topic} \n {format}",
    input_variables='topic',
    partial_variables={'format':parser.get_format_instructions()}
)

chain = template1 | model | parser

result=chain.invoke({'topic':topic})

print(result)