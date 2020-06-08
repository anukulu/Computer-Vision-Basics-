from PIL import Image
import numpy as np
from Kmeans import KMeansPlusPlus
import time
from ImageCreator import ImageCreate as imCreate

class ColorQuantize:

    @staticmethod
    def ImageData(image):

        tempImage = Image.open(image)
        img = None
        lst = image.split(".")
        if(lst[1] == 'jpg' or lst[1] == 'jpeg'):
            img = tempImage
        elif(lst[1] == 'png'):
            img = tempImage.convert('RGB')
        imageArray = np.array(img) / 255.0
        
        flattened = np.resize(imageArray, (imageArray.shape[0] * imageArray.shape[1], 3))

        return (flattened, imageArray.shape)
    
    @staticmethod
    def Cluster(image, k):

        mainData, imageShape = ColorQuantize.ImageData(image)
        centroids = KMeansPlusPlus.Kmeans(mainData, k)  #this takes a lot of time

        for x in range(mainData.shape[0]):

            dataPoint = mainData[x]
            distance = []
            for y in centroids:
                d = KMeansPlusPlus.distance(y, dataPoint)
                distance.append(d)
            indexOfNearestCentroid = np.argmin(distance)
            mainData[x] = centroids[indexOfNearestCentroid]
        
        finalImage = np.resize(mainData, imageShape)
        print(finalImage)
        newName = 'QuantizedImageWith_K=' + str(k)
        imCreate.RecreateImage(finalImage, newName)

        return finalImage
    

    

