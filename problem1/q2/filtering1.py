import cv2
import numpy as np
from skimage.util import random_noise

# Consts
FONT = cv2.FONT_HERSHEY_SIMPLEX
ORG = (25, 25)
SCALE = 0.5
COLOR = (0, 0, 0)
THICKNESS = 1

def insertCap(src:np.matrix, text:str):
    return cv2.putText(src, text, ORG, FONT, 
                       SCALE, COLOR, THICKNESS, cv2.LINE_AA)    

def addSPNoise(src:np.matrix, proportion:float):
    noiseImg = random_noise(src, mode='s&p', amount=proportion)
    # The function returns a floating-point image
    # in range [0, 1]. Need to converted it to 'uint8'
    # and in range [0,255]
    return np.array(255*noiseImg, dtype = 'uint8')

def addGaussianNoise(src:np.matrix, sigma:float):
    noiseImg = random_noise(src, mode='gaussian', var=sigma)
    return np.array(255*noiseImg, dtype = 'uint8')    

def meanFilter3by3(src:np.matrix):
    avgKernel = np.ones((3, 3), np.float32)/9
    return cv2.filter2D(src=src, ddepth=-1, kernel=avgKernel)

def medianFilter3by3(src:np.matrix):
    return cv2.medianBlur(src, 3)

def gaussianFilter(src:np.matrix):
    gaussianKernel = cv2.getGaussianKernel(3,1)
    return cv2.filter2D(src=src, ddepth=-1, kernel=gaussianKernel)   

if __name__ == "__main__":
    image = cv2.imread('peppers-scaled.jpg', cv2.IMREAD_COLOR);
    src = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    spNoiseImage = addSPNoise(src, 0.05)
    gaussianNoiseImage = addGaussianNoise(src, 1/256)

    medianFilteredSP = medianFilter3by3(spNoiseImage)
    medianFilteredGauss = medianFilter3by3(gaussianNoiseImage)

    meanFilteredSP = meanFilter3by3(spNoiseImage)
    meanFilteredGauss = meanFilter3by3(gaussianNoiseImage)

    gaussianFilteredSP = gaussianFilter(spNoiseImage)
    gaussianFilteredGauss = gaussianFilter(gaussianNoiseImage)

    spStack = np.concatenate((insertCap(src, "Source"), 
                              insertCap(spNoiseImage, "spNoise"),
                              insertCap(meanFilteredSP, "meanFilter"),
                              insertCap(medianFilteredSP, "medianFilter"),
                              insertCap(gaussianFilteredSP, "gaussianFilter")), axis=1) 

    gaussianStack = np.concatenate((insertCap(src, "Source"), 
                                 insertCap(gaussianNoiseImage, "gaussianNoise"),
                                 insertCap(meanFilteredGauss, "meanFilter"),
                                 insertCap(medianFilteredGauss, "medianFilter"),
                                 insertCap(gaussianFilteredGauss, "gaussianFilter")), axis=1) 
    
    cv2.imwrite("output-saltAndPepper.jpg", spStack)
    cv2.imwrite("output-gaussian.jpg", gaussianStack)

    cv2.imshow("salt&pepper", spStack)
    cv2.imshow("gaussian", gaussianStack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()