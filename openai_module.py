import openai
from openai import AzureOpenAI,OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the Azure OpenAI instance
# openai.api_type = "azure"
# openai.api_key = os.getenv("AZURE_OPENAI_KEY")
# openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # e.g., "https://<your-resource-name>.openai.azure.com"
# openai.api_version = os.getenv("API_VERSION_TO_USE")  # Example version, may vary by Azure deployment

client=AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("API_VERSION_TO_USE"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)
def generate_text_basic(prompt: str, system_prompt: str = "You are a helpful AI assistant"):
    response = client.chat.completions.create(
       #engine=deployment_name,  # Use the deployment name here instead of model
        model='DemoMigrate',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def generate_text_with_conversation(messages):
    response = client.chat.completions.create(
        #engine=deployment_name,  # Use the deployment name here instead of model
        model='DemoMigrate',
        messages=messages
    )
    return response.choices[0].message.content