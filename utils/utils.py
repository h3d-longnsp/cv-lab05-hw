import cv2
import numpy as np

def resizing(img:np.matrix, scl:float):
    """Downscale both images so the collage can fit on the monitor

    Args:
        img (np.matrix): Input image
        scl (float): Scale
    Returns:
        resized_img (np.matrix): Down/Up-scaled image based on scale ratio
    """
    scale_percent = scl # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
  
    # resize image
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
