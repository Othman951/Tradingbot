from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_market(pairs):
    messages = [
        {"role": "system", "content": "Tu es un assistant d'analyse crypto."},
        {"role": "user", "content": f"Analyse les données suivantes : {pairs}"}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content
