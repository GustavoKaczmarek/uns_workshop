# openai_client.py

import openai
import config

openai.api_key = config.OPENAI_API_KEY

def generate_response(question, data_context):
    prompt = (
        f"Based on the following data, answer the question:\n"
        f"Data: {data_context}\n"
        f"Question: {question}\n"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on provided data.  You are an operations assistant in a manufacturing environment and assist with analyzing data."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
    )

    return response.choices[0].message['content'].strip()
