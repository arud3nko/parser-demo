import base64
import pytesseract
from PIL import Image
import os


def decode(imaga):
    encoded = str(imaga.img['src']).replace('data:image/png;base64,', '')
    img_data = encoded.encode()
    with open("tempo.png", "wb") as fh:
        fh.write(base64.decodebytes(img_data))
    filename = "tempo.png"
    phone = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    return phone