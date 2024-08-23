from PIL import Image
import numpy as np

class MakeImgFromPixelRGB:
    def createIMG(PixelArray: list, Height: int, Width: int, ImgName: str, SaveImgAsFile: bool):
        # Convert the pixels into an array using numpy
        array = np.array(PixelArray, dtype=np.uint8).reshape(Height, Width, 3)
        if SaveImgAsFile == True:
            new_image = Image.fromarray(array)
            new_image.save(ImgName)
class getPixelsFromIMG:
    def __init__(self, JpegPath):
        im = Image.open(JpegPath, 'r')
        width, height = im.size
        im = Image.open(JpegPath)
        px = list(im.getdata())
        self.output = px