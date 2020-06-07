from RgbToGrayScale import RgbToGrayScale as rgb2gs
import numpy as np
import time
from PIL import Image
from scipy import ndimage
from ImageCreator import ImageCreate as imCreate

class Edgedetector:

    def Convolution2D(self, fltr, image):
        # outputHeight = int((image.shape[0] - fltr.shape[0]) + 1)
        # outputWidth = int(image.shape[1] - fltr.shape[1] + 1)

        # convolvedImage = np.zeros((outputHeight, outputWidth))

        # for i in range(0, outputHeight):
        #     for j in range(0, outputWidth):
        #         convolvedImage[i,j] = np.sum(fltr * image[i: (i + fltr.shape[0]), j: (j + fltr.shape[1])] )

        # implementation using scipy is way faster as it runs on C language
        convolvedImage = ndimage.filters.convolve(image, fltr)
        return convolvedImage
        

    def GaussianKernel(self, sigma, size):
        gFilter = np.zeros((size, size))
        size1 = int(size / 2)
        fraction = 1 / (2.0 * np.pi * sigma**2)
        for x in range(1, size+1):
            for y in range(1, size+1):
                gFilter[x-1][y-1] = np.exp(-1 * ((x - (size1+1))**2 + (y - (size1+1))**2) / (2 * sigma**2) )
                # print(y- size1-1)
        gFilter = fraction * gFilter
        return gFilter
    
    def BlurImage(self):
        tempBlurredImg = self.Convolution2D(self.GaussianKernel(1,5), self.gsImage)
        imCreate.RecreateImage(tempBlurredImg, 'gaussianBlurred')  #just to see the result
        return tempBlurredImg
    
    def SobelEdgeDetection(self):
        fltrX = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  #Sobel operators horizaontal and vertical
        fltrY = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

        
        blurImage = self.BlurImage()
        
        derivativeOfImageX = self.Convolution2D(fltrX, blurImage)
        derivativeOfImageY = self.Convolution2D(fltrY, blurImage)

        self.totalDerivative = np.hypot(derivativeOfImageX, derivativeOfImageY)
        self.edgeDirection = np.arctan2(derivativeOfImageY, derivativeOfImageX)

        imCreate.RecreateImage(self.totalDerivative, 'sobelEdgeDetected')   #just to see the result

        return(self.totalDerivative, self.edgeDirection)
    
    def nonMaximumSuppression(self):
        # convert the edge directions to degrees by multiplying the values in direction matrix by 180 / pi and add 180 to 
        # values less than 0 to flip the direction to make it positive
        gradient = self.totalDerivative
        # gradient = (gradient/ gradient.max()) * 255.0
        direction = self.edgeDirection * 180 * (1/ np.pi)
        direction[direction < 0] += 180
        
        newImage = np.zeros(gradient.shape)

        for i in range(1, gradient.shape[0]-1):
            for j in range(1, gradient.shape[1]-1):

                a = 0
                b = 0

                # for horizontal direction ie. 0 to 22.5 and 157.5 to 180
                if((0 <= direction[i,j] < 22.5) or (157.5 <= direction[i,j] <= 180)):
                    a = gradient[i, j+1]
                    b = gradient[i, j-1]
                # for 45 degree neighbours
                elif(22.5 <= direction[i,j] < 67.5):
                    a = gradient[i-1, j+1]
                    b = gradient[i+1, j-1]
                # for 90 degree or vertical neighbors
                elif(67.5 <= direction[i, j] < 112.5):
                    a = gradient[i-1, j]
                    b = gradient[i+1, j]
                # for 135 degree neighbours
                elif(112.5 <= direction[i,j] < 157.5):
                    a = gradient[i-1, j-1]
                    b = gradient[i+1, j+1]
                
                if(gradient[i,j] > a) and (gradient[i,j] > b):
                    newImage[i,j] = gradient[i,j]
                    # print(gradient[i,j])
                else:
                    newImage[i,j] = 0

        
        imCreate.RecreateImage(newImage, 'nonMaximumSupressed') #just to see the result
        
        self.supressedImage = newImage
        return newImage
    
    def DoubleThreshold(self):
        highThresholdRatio = 0.085
        lowThresholdRatio = 0.2
        supressedImage = self.supressedImage

        highThreshold = highThresholdRatio * supressedImage.max()
        lowThreshold = highThreshold * lowThresholdRatio

        newImage = np.zeros(supressedImage.shape)

        maximumI, maximumJ = np.where(supressedImage >= highThreshold)
        middleI, middleJ = np.where((supressedImage >= lowThreshold) & (supressedImage < highThreshold))

        newImage[maximumI, maximumJ] = 1
        newImage[middleI, middleJ] = 0.1

        self.thresholdedImage = newImage

        imCreate.RecreateImage(newImage, 'doubleThresholded')   #just to see the result
        return newImage
    
    def Hysteresis(self):

        low = 0.1
        high = 1
        thresholdImage = self.thresholdedImage
        for i in range(1, thresholdImage.shape[0]-1):
            for j in range(1, thresholdImage.shape[1]-1):

                if(thresholdImage[i,j] == low):
                    if((thresholdImage[i-1, j-1] == high) or (thresholdImage[i-1, j] == high) or (thresholdImage[i-1, j+1] == high) or (thresholdImage[i, j-1] == high) or (thresholdImage[i, j+1] == high) or (thresholdImage[i+1, j-1] == high) or (thresholdImage[i+1, j] == high) or (thresholdImage[i+1, j+1] == high)):
                        thresholdImage[i, j] = high
                    else:
                        thresholdImage[i, j] = 0
        
        self.hysteresisImage = thresholdImage

        imCreate.RecreateImage(thresholdImage, 'cannyEdgeDetected') #just to see the result
        return thresholdImage

    def CannyEdgeDetector(self, colorImage):

        self.gsImage = rgb2gs.ConvertToGrayScale(colorImage)
        self.SobelEdgeDetection()
        self.nonMaximumSuppression()
        self.DoubleThreshold()
        self.Hysteresis()



