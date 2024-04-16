import os
import openai

openai.api_key = "place API"
user_prompt = "bmw in blue"

response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="512x512"
)

image_url = response["data"][0]["url"]
print(image_url)
