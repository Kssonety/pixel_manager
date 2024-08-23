import pixelmanager

pixels = pixelmanager.getPixelsFromIMG(JpegPath="download.jpg")

pixelmanager.MakeImgFromPixelRGB.createIMG(pixels.output, 640, 480,  "output.jpg", True)

with open("output.txt", "w") as f:
    for s in pixels.output:
        f.write(str(s) + "," + "\n")