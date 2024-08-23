# pixel_manager
A Package To Manage Pixels On Screen in Python

**Team of people to finish this project, out goal is that with this package,
You can do anything pixel related in python. So please, if you can. Contribute. Every pull request will be tested and if they work, 
added to the main branch**

So far, we have **two** functions.

***MakeImgFromPixelRGB***

Example Code:
```
pixelmanager.MakeImgFromPixelRGB.createIMG(RGB_PIXEL_ARRAY, IMG_HEIGHT, IMG_WIDTH,  "name_of_saved_file.jpg", True)
```
***getPixelsFromIMG***

Example Code:
```
pixels = pixelmanager.getPixelsFromIMG(JpegPath="name_of_jpeg.jpg")
print(pixels.output)
```
