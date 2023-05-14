import numpy as np
import cv2
import operator


def get_contour(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ret, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key=cv2.contourArea)
    return cnt


def get_top_arc_point(cnt):
    out = sorted(cnt[:, 0, :].tolist(), key=operator.itemgetter(0))
    left_arc_point = (out[0][0], out[0][1])
    right_arc_point = (out[-1][0], out[-1][1])
    return left_arc_point, right_arc_point


def get_down_arc_point(cnt):
    x, y, w, h = cv2.boundingRect(cnt)
    out = sorted(cnt[:, 0, :].tolist(), key=operator.itemgetter(1))
    right_arc_point = (out[-1][0], out[-1][1])
    left_arc_point = (out[-1][0], out[-1][1])
    for i in range(len(out) - 1, 0, -1):
        if out[i][1] == out[-1][1]:
            left_arc_point = (out[i][0], out[i][1])
        else:
            break
    # in case of acquiring the same side
    if right_arc_point[0] - left_arc_point[0] < 50:
        if right_arc_point[0] < x + w / 2:
            right_arc_point = (2 * x + w - left_arc_point[0], left_arc_point[1])
        else:
            left_arc_point = (2 * x + w - right_arc_point[0], right_arc_point[1])
    return left_arc_point, right_arc_point


def compute_theta(cnt):
    l, r = get_top_arc_point(cnt)
    x, y, w, h = cv2.boundingRect(cnt)
    chord_top2side = ((l[1] - y) ** 2 + (w / 2) ** 2) ** 0.5
    chrod_left2right = w
    theta = 4 * np.arccos(0.5 * chrod_left2right / chord_top2side)
    return theta


def compute_radius(theta, w):
    return 0.5 * w / np.sin(theta / 2)


def cart2polar(input_img, theta_range, r_range, center, theta_step=np.pi / (8 * 180.0), r_step=1):
    minr, maxr = r_range
    mintheta, maxtheta = theta_range
    h = int((maxr - minr) / r_step + 1)
    w = int((maxtheta - mintheta) / theta_step + 1)
    output_img = np.zeros((h, w), np.uint8)
    j = 0
    for theta in np.arange(mintheta, maxtheta, theta_step):
        i = 0
        for r in np.arange(minr, maxr, r_step):
            x = int(round(center[0] + r * np.cos(theta)))
            y = int(round(center[1] - r * np.sin(theta)))
            output_img[i][j] = input_img[y][x]
            i += 1
        j += 1
    return output_img


def is_existing_artifacts(img, k):
    distribution = calc_row_mean_pixel(img)
    mean = sum(distribution) / len(distribution)
    max_index, max_row = max(enumerate(distribution), key=operator.itemgetter(1))
    if max_row > k * mean:
        return True
    else:
        return False


def remove_artifacts(img, k, origin_img, theta_range, r_range, center, theta_step=np.pi / (8 * 180.0)):
    minr, maxr = r_range
    mintheta, maxtheta = theta_range
    distribution = calc_row_mean_pixel(img)
    mean = sum(distribution) / len(distribution)
    for row in range(img.shape[0]):
        if distribution[row] > k * mean:
            r = minr + row
            col = 0
            for theta in np.arange(mintheta, maxtheta, theta_step):
                x = int(center[0] + r * np.cos(theta))
                y = int(center[1] - r * np.sin(theta))
                img[row][col] = img[row - 1][col]
                origin_img[y][x] = img[row][col]  # nearest neighbor approximation  img[row - 1][col]
                col += 1
    return origin_img


def calc_row_mean_pixel(img):
    distribution = np.zeros(img.shape[0], dtype=float)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            distribution[row] += img[row][col]
        distribution[row] /= img.shape[1]
    return distribution


def generate_artifacts(polar_img, origin_img, theta_range, r_range, center, theta_step=np.pi / (8 * 180.0), r_step=1):
    minr, maxr = r_range
    mintheta, maxtheta = theta_range
    p = np.random.randint(0, polar_img.shape[0] - 2)
    for i in range(p - 1, p + 1):
        polar_img[i, :] = 255
    for theta in np.arange(mintheta, maxtheta, theta_step):
        for r in np.arange(minr + p - 1, minr + p + 1, r_step):
            x = int(center[0] + r * np.cos(theta))
            y = int(center[1] - r * np.sin(theta))
            origin_img[y, x] = 255
    return polar_img, origin_img
