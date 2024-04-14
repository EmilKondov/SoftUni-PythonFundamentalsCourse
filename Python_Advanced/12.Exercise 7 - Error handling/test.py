import tkinter as tk
import json
import requests


def render_image():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjhiN2UyNzQtNjk1MC00ZTFmLWE1OWMtOGNiNTZhNGFjNDU1IiwidHlwZSI6ImFwaV90b2tlbiJ9.1Q48xkbkr9i6Zkqo8Odhl5E7oyBE7fYOPhas8Y_9pdg"}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": 'openai',
        "text": input_field.get(),
        "resolution": "512x512",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)

    try:
        result = json.loads(response.text)
        print(result)  # Print the entire response for debugging

        # Check if 'openai' key exists
        if 'openai' in result:
            # Assuming 'items' exist within 'openai'
            print(result['openai']['items'])
        else:
            print("Error: 'openai' key not found in the response.")

    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)

    except Exception as e:
        print("An error occurred:", e)


window = tk.Tk()
window.title("First Window")
window.geometry("750x600")

input_field = tk.Entry(window, width=25)
input_field.place(x=150, y=20)

image_label = tk.Label(window)
image_label.place(x=125, y=70)

generate_button = tk.Button(window, text="Create", height=1, command=render_image)
generate_button.place(x=325, y=18)

window.mainloop()
