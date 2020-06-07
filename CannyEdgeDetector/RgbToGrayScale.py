from PIL import Image
import numpy as np
import time

class RgbToGrayScale:
    
    @staticmethod
    def ConvertToGrayScale(image):
        lst = image.split(".")
        img = Image.open(image)
        rgbImg = None
        if(lst[1] == 'png'):
            rgbImg = img.convert('RGB')
        elif(lst[1] == 'jpg' or lst[1] == 'jpeg'):
            rgbImg = img
        normalizedImg = np.array(rgbImg) / 255.0

        newImage = np.zeros(normalizedImg.shape)
        coefficients = [0.2126, 0.7152, 0.0722]
        # multiplying each RGB channel with its corresponding luminosity weights according to that which humans perceive
        # Similar to:
        # i = 0
        # for x in coefficients:
        #   newImage += self.image[:,:,i] * coefficient
        #   i += 1 
        newImage = np.dot(normalizedImg, coefficients)
        return newImage
        





