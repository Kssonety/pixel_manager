from PIL import Image
import numpy as np

class MakeImgFromPixelRGB:
    def createIMG(PixelArray: list, ImgName: str, SaveImgAsFile: bool):
        # Convert the pixels into an array using numpy
        array = np.array(PixelArray, dtype=np.uint8)
        if SaveImgAsFile == True:
            new_image = Image.fromarray(array)
            new_image.save(ImgName)
    def getPixelsFromIMG(ImageFile):
        pass


MakeImgFromPixelRGB.createIMG([
   [(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],
   [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],
   [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],
   [(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]
], "test.png", True)
