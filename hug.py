from langchain_huggingface import HuggingFaceEndpoint
import os
from dotenv import load_dotenv
load_dotenv()

#os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HF_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="huggingfaceh4/zephyr-7b-alpha", 
    temperature=0.7,       
    max_new_tokens=512 
)

query = "What is capital of India and UAE?"

prompt = f"""
 <|system|>
You are an AI assistant that follows instruction extremely well.
Please be truthful and give direct answers
</s>
 <|user|>
 {query}
 </s>
 <|assistant|>
"""

response = llm.predict(prompt)
print(response)