import tkinter as tk
import json
import urllib.request
import requests

from io import BytesIO
from PIL import ImageTk, Image


def display_image(image_url: str) -> None:
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read() # тук изтегляме снимката

    image_stream = BytesIO(image_data)    # взимаме тези данни със самото изображение и създаваме поток от данни (binary symbols) в паметта RAM
    image = ImageTk.PhotoImage(Image.open(image_stream))

    image_label.config(image=image)
    image_label.image = image # keeps reference to the image


#В тази функция е връзката ни с API, откъдето получаваме линк към изображението, което AI е генерирал.
def get_image_url() -> str:
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjhiN2UyNzQtNjk1MC00ZTFmLWE1OWMtOGNiNTZhNGFjNDU1IiwidHlwZSI6ImFwaV90b2tlbiJ9.1Q48xkbkr9i6Zkqo8Odhl5E7oyBE7fYOPhas8Y_9pdg"}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": "this is a test of Eden AI",
        "resolution": "512x512",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    print(result['openai']['items'][0]["image_resource_url"])


def render_image():
    print("clicked")
    try:
        error_label.place_forget()
        image_url = get_image_url()
    except KeyError:
        error_label.place(x=175, y=50)
    else:
        display_image(image_url)


window = tk.Tk()
window.title("AI Image Creator")
window.geometry("500x350") # width x height

error_label = tk.Label(window, text="Prompt cannot be empty!", fg="red")

input_field = tk.Entry(window, width=15, bg="orange") # за да го видим трябва да му зададем позиция, което правим на следващия ред
input_field.place(x=200, y=20)


image_label = tk.Label(window)
image_label.place(x=125, y=70)

generate_button = tk.Button(window, text="Create", height=1, command=render_image)
generate_button.place(x=300, y=17)

window.mainloop()
""" window.mainloop() е един безкраен цикъл, който подържа
нашата програма жива и позволява да движим мишката си, 
както и различни събития да се случват докато програмата 
работи. Този код не спира до момента, в който ние не
затворим прозореца.
 """