import cv2
import numpy as np

def preprocess(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    return cv2.resize(img, (640,640))
