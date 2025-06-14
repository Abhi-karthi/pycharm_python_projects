from chat import query
from openai import OpenAI

client = OpenAI(api_key="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")

question = input("Enter prompt: ")
print(query(question))
