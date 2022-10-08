from utils import resizing
import cv2

image = cv2.imread('iss.jpg', cv2.IMREAD_COLOR)

scaled = resizing(image, 55)

cv2.imshow("scaled", scaled)
cv2.imwrite("iss-scaled.jpg", scaled)
cv2.waitKey(0)
cv2.destroyAllWindows
