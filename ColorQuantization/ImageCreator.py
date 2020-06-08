from PIL import Image
import numpy as np

class ImageCreate:

    @staticmethod
    def RecreateImage(arr, newName):
        # rescaling the image to 0-255 and converting to uint8
        rescaledNewImg = (255.0 / arr.max() * (arr - arr.min())).astype(np.uint8)    
        
        newImg = Image.fromarray(rescaledNewImg)
        newImg.save('images/' + newName + ".png")
        return newImg
        