import cv2


def contrast_enhance(gray):
    clahe = cv2.createCLAHE(clipLimit=0.5, tileGridSize=(3, 3))
    clahe_img = clahe.apply(gray)
    return clahe_img
