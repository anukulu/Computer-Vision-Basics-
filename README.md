# Computer-Vision-Basics-
Implementing a few basic computer vision algorithms using python 

1. Canny Edge Detector
  This algorithms has been implemented using PIL library and numpy. 
  The images were firstly converted to greyscale.
  Gaussian filter of size 5 by 5 was applied to the greyscale image to blur the image and reduce noise.
  Sobel Operators were then applied to find vertical and horizontal edges, then total edge gradient and edge direction were also calculated.
  Non maximum supression algorithm was implemented to remove the less relevant pixels.
  Double thresholding and hysteresis was done to find pixels that seemed non relevant but were part of the main edges as well as to
    reduce non-relevent pixels.
   
