# pixel_manager
A Package To Manage Pixels On Screen in Python

**We require a team of people to finish this project. Our main goal is that with this package,
You can do anything pixel related in python. So please, if you can. Contribute. Every pull request will be tested and if they work, 
added to the main branch**

So far, we have **three** functions.

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

***setPixelOnIMG***

Example Code:
```
this_rgb_tuple = (0, 1, 0)
pixelmanager.setPixelOnIMG(2, 9, "img.png", "output.png", this_tuple)
```
