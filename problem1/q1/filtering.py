import cv2
import numpy as np
from matplotlib import pyplot as plt

# Consts
FONT = cv2.FONT_HERSHEY_SIMPLEX
ORG = (25, 25)
SCALE = 0.7
COLOR = (255, 255, 255)
THICKNESS = 1

plt.rcParams["figure.figsize"] = [14, 8]

def insertCap(src:np.matrix, text:str):
    return cv2.putText(src, text, ORG, FONT, 
                       SCALE, COLOR, THICKNESS, cv2.LINE_AA)    

def brightenCv2(src:np.matrix, value:int):
    return cv2.convertScaleAbs(src, beta=value)

def contrastCv2(src:np.matrix, value:float):
    return cv2.convertScaleAbs(src, alpha=value)

def histeqCv2(src:np.matrix):
    return cv2.equalizeHist(src)

def histogramsPlotting(srcHistogram:np.matrix, brightenHistogram:np.matrix, 
                       contrastHistogram:np.matrix, histeqHistogram:np.matrix):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Histogram comparison')
    
    ax1.plot(srcHistogram, label = 'source')
    ax1.set(xlabel='Intensity')

    ax2.plot(brightenHistogram, label = 'brighten', color = 'orange')
    ax2.set(xlabel='Intensity')

    ax3.plot(contrastHistogram, label = 'contrast', color = 'yellow')
    ax3.set(xlabel='Intensity')

    ax4.plot(histeqHistogram, label = 'histEq', color = 'green')
    ax4.set(xlabel='Intensity')

    fig.legend(title = 'Histograms')
    for ax in fig.get_axes():
        ax.label_outer()
    plt.savefig('Histogram_comparison.png')
    plt.show()

if __name__ == "__main__":
    sourceImg = cv2.imread("./city.jpg", cv2.IMREAD_GRAYSCALE)

    brightenImage = brightenCv2(sourceImg, 55)
    contrastImage = contrastCv2(sourceImg, 1.7)
    histeqImage = histeqCv2(sourceImg)

    # Compute histograms
    srcHist = cv2.calcHist([sourceImg],[0],None,[256],[0,256])
    brightenHist= cv2.calcHist([brightenImage],[0],None,[256],[0,256])
    contrastHist = cv2.calcHist([contrastImage],[0],None,[256],[0,256])
    histeqHist = cv2.calcHist([histeqImage],[0],None,[256],[0,256])

    stack = np.concatenate((insertCap(sourceImg, "source"), 
                                       insertCap(brightenImage, "brighten"), 
                                       insertCap(contrastImage, "contrast"),
                                       insertCap(histeqImage, "histEq")), axis=1) 

    cv2.imshow("filtering", stack)
    cv2.imwrite('city-output.jpg', stack)

    histogramsPlotting(srcHist, brightenHist, contrastHist, histeqHist)

    cv2.waitKey(0)
    cv2.destroyAllWindows()