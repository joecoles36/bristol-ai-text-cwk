from google import genai
from PIL import Image

client = genai.Client()

img = Image.open("num_7.png")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        "Describe the number, its colour, its size, and the background colour in one sentence.",
        img
    ]
)

print(response.text)
