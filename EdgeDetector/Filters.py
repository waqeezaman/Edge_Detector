import numpy as np
import PIL.ImageOps as ImageOps
from scipy.signal import convolve2d


class Filters:
    SobelVertical=np.array([ [1,0,-1],
                             [2,0,-2],
                             [1,0,-1]])

    SobelHorizontal=np.array([[1,2,1],
                             [0,0,0],
                             [-1,-2,-1]])

    edge=np.array([[1,  0, -1],
                [2 , 0, -2 ],
                [1  ,0 ,-1]])

    PrewittVertical=np.array([[1,0,-1],
                         [1,0,-1],
                         [1,0,-1]])

    

    staticmethod
    def ApplyFilter(imgfilter,image):
         
         ## if we want edge detection we must first make the image greyscale
         image=ImageOps.grayscale(image)
              


         
         ## applies a filter to the image  // by iterating the filter over each value 
         ## in the array
         image=np.array(image)
         image=convolve2d(image,imgfilter)
        
         return image

 