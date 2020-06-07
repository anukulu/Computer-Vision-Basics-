from CannyEdgeDetection import Edgedetector as ED
import time

start = time.time()
a = ED()
a.CannyEdgeDetector("test.png") # the name of image whose edge needs to be detected is written here
end = time.time()
print(end - start)