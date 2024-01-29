import tkinter as tk
import json
import urllib.request
import requests

from io import BytesIO
from PIL import ImageTk

def display_image(image_url: str) -> None:
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read() # тук изтегляме снимката


    image_stream = BytesIO(image_data)    # взимаме тези данни със самото изображение и създаваме поток от данни (binary symbols) в паметта RAM

    image = ImageTk.PhotoImage(Image.open(image_stream))






#В тази функция е връзката ни с API, откъдето получаваме линк към изображението, което AI е генерирал.
def get_image_url() -> str:

    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjhiN2UyNzQtNjk1MC00ZTFmLWE1OWMtOGNiNTZhNGFjNDU1IiwidHlwZSI6ImFwaV90b2tlbiJ9.1Q48xkbkr9i6Zkqo8Odhl5E7oyBE7fYOPhas8Y_9pdg"}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input_field.get(),
        "resolution": "256x256",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    print(result['openai']['items'][0]["image_resource_url"])



def rened_image():
    image_url = get_image_url()


window = tk.Tk()
window.title("AI Image Creator")
window.geometry("500x350") # width x height

input_field = tk.Entry(window, width=15) # за да го видим трябва да му зададем позиция, което правим на следващия ред
input_field.place(x=200, y=20)

generate_button = tk.Button(window, text="Create", height=1, command=rened_image)
generate_button.place(x= 300, y =17)

window.mainloop()
""" window.mainloop() е един безкраен цикъл, който подържа
нашата програма жива и позволява да движим мишката си, 
както и различни събития да се случват докато програмата 
работи. Този код не спира до момента, в който ние не
затворим прозореца.
 """