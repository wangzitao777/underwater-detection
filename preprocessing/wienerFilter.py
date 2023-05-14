import scipy.signal
import cv2
import numpy as np


def wiener_filter(gray):
    _gray = gray.astype('float64')
    out = scipy.signal.wiener(_gray, [3, 3])
    output = np.uint8(out / out.max() * 255)
    return output
