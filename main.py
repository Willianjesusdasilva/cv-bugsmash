import numpy as np
import pyautogui
import imutils
import cv2


def get_bugs(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(image_gray, 120, 255, cv2.THRESH_BINARY_INV)
    dilated = cv2.dilate(thresh, np.ones((20, 20)))

    contour = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour = imutils.grab_contours(contour)

    centers = []
    for c in contour:
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        centers.append([cX, cY])

    return(centers)


while True:
    image = pyautogui.screenshot(region=(2, 120, 1280, 590))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    for cordinate in get_bugs(image):
        pyautogui.click(x=cordinate[0]+2, y=cordinate[1]+120)
