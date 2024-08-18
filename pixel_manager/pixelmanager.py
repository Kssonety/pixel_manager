from PIL import Image
import numpy as np

def MakeImageFromPixelRGB(PixelArray: list, ImgName: str, SaveImgAsFile: bool):
    # Convert the pixels into an array using numpy
    array = np.array(PixelArray, dtype=np.uint8)

    if SaveImgAsFile == True:
        new_image = Image.fromarray(array)
        new_image.save(ImgName)