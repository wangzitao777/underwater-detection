import os
import numpy as np
import cv2
import operator
import scipy.signal
from artifactRemoval import get_contour, get_top_arc_point, get_down_arc_point, compute_theta, compute_radius, \
    cart2polar, is_existing_artifacts, remove_artifacts, calc_row_mean_pixel, generate_artifacts
from wienerFilter import wiener_filter
from contrastEnhancement import contrast_enhance

data_percent = 0.3
input_path = '../data/images'  #


def main():
    total_imgs = os.listdir(input_path)
    if not os.path.exists('../data/preprocessed/2/images'):  #
        os.makedirs('../data/preprocessed/2/images')  #

    for img in total_imgs:
        print(img)
        img_in = cv2.imread(input_path + '/' + img)

        cnt = get_contour(img_in)
        x, y, w, h = cv2.boundingRect(cnt)
        l, r = get_top_arc_point(cnt)
        theta = compute_theta(cnt)
        r = compute_radius(theta, w)
        ld, rd = get_down_arc_point(cnt)
        delta_r = ((l[1] - ld[1]) ** 2 + (l[0] - ld[0]) ** 2) ** 0.5

        img_in_gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
        img_polar = cart2polar(img_in_gray,
                               theta_range=((np.pi - theta) / 2.0, (np.pi + theta) / 2.0),
                               r_range=(r - delta_r, r),
                               center=(x + w / 2, y + r))

        if is_existing_artifacts(img_polar, 3):
            print(f"{img} exists artifacts")
            img_out = remove_artifacts(img_polar, 3, img_in_gray, theta_range=((np.pi - theta) / 2.0, (np.pi + theta) / 2.0),
                                       r_range=(r - delta_r, r),
                                       center=(x + w / 2, y + r))
            img_out = contrast_enhance(img_out)
            img_out = wiener_filter(img_out)
        else:
            img_out = contrast_enhance(img_in_gray)
            img_out = wiener_filter(img_out)
        cv2.imwrite('../data/preprocessed/2/images/' + img, img_out)  #


def debug():
    img = "../data/0.1/images/marine-debris-aris3k-1236.jpg"
    img_in = cv2.imread(img)

    cnt = get_contour(img_in)
    x, y, w, h = cv2.boundingRect(cnt)
    print(x, y, w, h)
    l, r = get_top_arc_point(cnt)
    print(l, r)
    theta = compute_theta(cnt)
    r = compute_radius(theta, w)
    print(theta, r)
    ld, rd = get_down_arc_point(cnt)
    print(ld, rd)

    delta_r = ((l[1] - ld[1]) ** 2 + (l[0] - ld[0]) ** 2) ** 0.5
    print(delta_r)

    img_in_gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    print(((np.pi - theta) / 2.0, (np.pi + theta) / 2.0))
    print((r - delta_r, r))
    img_polar = cart2polar(img_in_gray,
                           theta_range=((np.pi - theta) / 2.0, (np.pi + theta) / 2.0),
                           r_range=(r - delta_r, r),
                           center=(x + w / 2, y + r))

    if is_existing_artifacts(img_polar, 3):
        print(f"{img} exists artifacts")
        img_out = remove_artifacts(img_polar, 3, img_in_gray,
                                   theta_range=((np.pi - theta) / 2.0, (np.pi + theta) / 2.0),
                                   r_range=(r - delta_r, r),
                                   center=(x + w / 2, y + r))
        img_out = wiener_filter(img_out)
        img_out2 = contrast_enhance(img_out)
    else:
        img_out1 = contrast_enhance(img_in_gray)
        img_out = wiener_filter(img_in_gray)
        img_out2 = wiener_filter(img_out1)
        # img_out2 = contrast_enhance(img_out)
    cv2.imshow('in', img_in)
    cv2.imshow('out', img_out)
    cv2.imshow('out1', img_out1)
    cv2.imshow('out2', img_out2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite('../data/preprocessed/' + str(data_percent) + '/images/' + img, img_out)


if __name__ == '__main__':
    # debug()
    # cv2.destroyAllWindows()
    main()
