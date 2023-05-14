import os
import cv2

path = "~/data/GitProjects/ultralytics/UATD_Training/images"
for image in os.listdir(path):
    if os.path.splitext(image)[1] == '.bmp':
        print(image)
        # print(path + '/' + image)
        img = cv2.imread(path + '/' + image)
        new_image = image.replace(".bmp", ".jpg")
        cv2.imwrite(path + '/' + new_image, img)
