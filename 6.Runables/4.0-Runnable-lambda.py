from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableSequence

load_dotenv()

model=ChatOpenAI()

prompt=PromptTemplate(
    template='write a joke on {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

def word_counter(text):
    return len(text.split())


joke_chain=RunnableSequence(prompt,model,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'count':RunnableLambda(word_counter)
})

final_chain=RunnableSequence(joke_chain,parallel_chain)

result=final_chain.invoke('Gym')

print(result)
print(result['joke'])
print(result['count'])