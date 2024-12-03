from openai import AzureOpenAI
client = AzureOpenAI(
    api_key="b3853712358b4605add15ce36dd37925",
    
    api_version="2023-09-15-preview",
    azure_endpoint="https://revupdemo.openai.azure.com/"
)

# def get_completion_from_message2(system_message2,
#                                  model='DemoMigrate', temperature=1.2,max_tokens=2500) -> str:
def get_completion_from_message2(system_message2) -> str:
    messages = [
        {"role": "system", "content": system_message2},
        # {"role": "user", "content": user_message1}, # user_message1}
       
        # {'role': 'system', 'content': erp_master_message},
        

    ]
    print(messages)
    response = client.chat.completions.create(
        model='DemoMigrate',  
        messages=messages,
        temperature=1.2,
        max_tokens=2500,
        top_p=0.95,
        n=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    # response = client.completions.create()
    return response.choices[0].message.content
def main():
  system_message2="create a unique article on dog"
  # response1="1"
  # erp_master_message="2"
  print(get_completion_from_message2(system_message2 ))
if __name__ == "__main__":
  main()