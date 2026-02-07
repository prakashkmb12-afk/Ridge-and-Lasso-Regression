import ssl
import certifi

ssl._create_default_https_context = ssl._create_unverified_context

import google.generativeai as genai

# configure API
genai.configure(api_key="AIzaSyD3dL4xQ5SjGzCs2vzNvK25ADR8flu31YA")

model = genai.GenerativeModel("gemini-3-flash-preview")


def think(user_input, memory):

    # system instruction
    prompt = prompt = """
You are an AI assistant created by Prakash.
You help users with learning, calculations, and general tasks.
Do not say you are Google's model unless explicitly asked.
Be concise and helpful.
"""


    # add memory
    for msg in memory:
        prompt += msg + "\n"

    # add current input
    prompt += f"You: {user_input}\nAgent:"

    response = model.generate_content(prompt)

    return response.text
