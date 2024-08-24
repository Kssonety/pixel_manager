from PIL import Image
import numpy as np

class MakeImgFromPixelRGB:
    def __init__(self, PixelArray: list, Height: int, Width: int, ImgName: str, SaveImgAsFile: bool):
        array = np.array(PixelArray, dtype=np.uint8).reshape(Width, Height, 3)
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

class setPixelOnIMG:
    def __init__(self, Pixel_X_Position, Pixel_Y_Position, ImgPath, ImgNAME: str, newRGBAtupleValue: tuple):
        im = Image.open(ImgPath)
        pix = im.load()
        pix[Pixel_X_Position, Pixel_Y_Position] = newRGBAtupleValue
        im.save(ImgNAME)