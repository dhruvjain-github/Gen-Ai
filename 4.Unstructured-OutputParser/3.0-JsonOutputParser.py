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
    # partial variable get filled before run time
    partial_variables={'format':parser.get_format_instructions()}
)

prompt=template1.invoke({'topic':topic})

result=model.invoke(prompt)

# print(result)

final_result=parser.parse(result.content)

print(final_result)

print(type(result))
print(type(final_result))