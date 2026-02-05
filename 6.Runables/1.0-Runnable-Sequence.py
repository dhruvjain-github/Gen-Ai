from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

load_dotenv()

model=ChatOpenAI()

prompt=PromptTemplate(
    template='wirte a small para about the {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

chain=RunnableSequence(prompt,model,parser)

result=chain.invoke({'topic':'college'})

print(result)

