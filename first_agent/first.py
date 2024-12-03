###using llama index
#pip install llama-index
#pip install llama-index-llms-azure-openai
from dotenv import load_dotenv
load_dotenv(override=True)
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.llms.azure_openai import AzureOpenAI
import os

#defining the functions 
def multi(a:float,b:float)->float:
    return a*b
def add(a:float,b:float)->float:
    return a+b
def sub(a:float,b:float)->float:
    return a-b
def div(a:float,b:float)->float:
    return a/b

#defining tools for agent
multi_tool=FunctionTool.from_defaults(fn=multi)
add_tool=FunctionTool.from_defaults(fn=add)
sub_tool=FunctionTool.from_defaults(fn=sub)
div_tool=FunctionTool.from_defaults(fn=div)

#initilazing th llm
llm = AzureOpenAI(
    model="gpt-3.5-turbo",
    engine=os.getenv("Engine"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("API_VERSION_TO_USE"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")

)
#initilizing the agent
agent=ReActAgent.from_tools([multi_tool,add_tool,sub_tool,div_tool],llm=llm,verbose=True)
#testing the agent
response = agent.chat("What is 20+(2*4)? Use a tool to calculate every step.")
print(response)
