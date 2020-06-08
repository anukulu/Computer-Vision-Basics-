# Computer-Vision-Basics-
Implementing a few basic computer vision algorithms using python. These are meant for learning purposes and anyone who wishes to learn
these algorithms can go through the code and understand it without much effort.

1. Canny Edge Detector
  This algorithms has been implemented using PIL library and numpy. 
  The images were firstly converted to greyscale.
  Gaussian filter of size 5 by 5 was applied to the greyscale image to blur the image and reduce noise.
  Sobel Operators were then applied to find vertical and horizontal edges, then total edge gradient and edge direction were also calculated.
  Non maximum supression algorithm was implemented to remove the less relevant pixels.
  Double thresholding and hysteresis were done to find pixels that seemed non relevant but were part of the main edges as well as to
    reduce non-relevent pixels.
2. Color Quantization using K++ algorithm
  This is a very simple implementation of K-means clustering algorithm. It has been used to quantize colors in the image with the specified value of k. The algorithm implemented in python is very bad in terms of time complexity and needs to be optimized but the results are not very bad.
    
    
Run main.py to see results with any image you want.
   
