import numpy as np
import sys

class KMeansPlusPlus:

    @staticmethod
    def distance(a, b):
        return np.sum((a-b)**2)
    

    @staticmethod
    def Kmeans(data, k):    #only accepts 2D vector
        
        centroids = []
        centroids.append(data[np.random.randint(data.shape[0])])

        for x in range(k-1):

            distances = []

            for y in range(data.shape[0]):

                dataPoint = data[y]
                minDistance = sys.maxsize

                for z in range(len(centroids)):

                    tempDistance = KMeansPlusPlus.distance(centroids[z], dataPoint)
                    minDistance = min(tempDistance, minDistance)
                
                distances.append(minDistance)
            
            distances = np.array(distances)
            maximumDistanceIndex = np.argmax(distances)
            newCentroid = data[maximumDistanceIndex]
            centroids.append(newCentroid)
        
        return centroids



    
    


