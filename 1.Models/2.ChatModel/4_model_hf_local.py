from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

# this command helps to install the model locally and run it
llm=HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model=ChatHuggingFace(llm=llm)

result=model.invoke("What is the capital of india")

print(result)