import cv2
import numpy as np

# Consts
FONT = cv2.FONT_HERSHEY_SIMPLEX
ORG = (175, 25)
SCALE = 0.7
THICKNESS = 2
COLOR = (255, 255, 255)

def insertCap(src:np.matrix, text:str):
    return cv2.putText(src, text, ORG, FONT, 
                       SCALE, COLOR, THICKNESS, cv2.LINE_AA) 

def edgeSobel(src:np.matrix):
    sobelX = cv2.Sobel(src=src, ddepth=cv2.CV_8U, dx=1, dy=0, ksize=5)
    sobelY = cv2.Sobel(src=src, ddepth=cv2.CV_8U, dx=0, dy=1, ksize=5)
    return sobelX + sobelY

def edgePrewitt(src:np.matrix):
    kernelX = np.array([[ 1, 1, 1],
                        [ 0, 0, 0],
                        [-1,-1,-1]]) 
    kernelY = np.array([[-1,0,1],
                        [-1,0,1],
                        [-1,0,1]]) 

    prewittX = cv2.filter2D(src, -1, kernelX) 
    prewittY = cv2.filter2D(src, -1, kernelY)    
    return prewittX + prewittY

def edgeRoberts(src:np.matrix):
    kernelCrossV = np.array([[1, 0],
                             [0,-1]])
    kernelCrossH = np.array([[0, 1],
                            [-1, 0]])
    
    robertsVertical = cv2.filter2D(src=src, ddepth=-1, kernel=kernelCrossV)
    robertsHorizontal = cv2.filter2D(src=src, ddepth=-1, kernel=kernelCrossH)
    edgeImg = np.sqrt(np.square(robertsHorizontal) + np.square(robertsVertical))
    # The function returns a floating-point image
    # on the range [0, 1]. Need to converted it to 'uint8'
    # and on range [0,255]
    return np.array(255*edgeImg, dtype = 'uint8')

def edgeCanny(src:np.matrix):
    # use `trackbar.py` to quickly try threshold values
    return cv2.Canny(src, 12, 60)

def edgeLaplacian(src:np.matrix):
    laplacian = cv2.Laplacian(src, ddepth=cv2.CV_64F, ksize=3) # CV_64F | CV_16S
    return cv2.convertScaleAbs(laplacian)

if __name__ == "__main__":
    image = cv2.imread('iss-scaled.jpg', cv2.IMREAD_COLOR);
    src = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)     

    # Preprocessing: reduce noise for better edges detection
    srcBlurred = cv2.GaussianBlur(src, (3, 3), 0)

    detectEdgeSobel     =  edgeSobel(srcBlurred)
    detectEdgePrewitt   =  edgePrewitt(srcBlurred)
    detectEdgeCanny     =  edgeCanny(srcBlurred)
    detectEdgeRoberts   =  edgeRoberts(srcBlurred)
    detectEdgeLaplacian =  edgeLaplacian(srcBlurred)

    stack1 = np.concatenate((insertCap(src, "Source"), 
                            insertCap(detectEdgeSobel, "Sobel"),
                            insertCap(detectEdgePrewitt, "Prewitt"),), axis=0) 

    stack2 = np.concatenate((insertCap(detectEdgeRoberts, "Roberts"),
                             insertCap(detectEdgeCanny, "Canny"),
                             insertCap(detectEdgeLaplacian, "Laplacian")), axis=0) 

    cv2.imwrite("output-1.jpg", stack1)
    cv2.imwrite("output-2.jpg", stack2)

    cv2.imshow("Edge detection", stack1)
    cv2.imshow("Edge detection2", stack2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()