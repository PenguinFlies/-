import cv2
import numpy as np


def vis_convert(img, mask):
    """
    vis_convert : use IMPAINT_TELEA from Alexandru Telea to clean white line

    Parameters
    ----------
    img : vis jpg file
    mask : gray,same size as img

    return
    ----------
    img : jpg file

    """
    img = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

    return img


def create_mask(img):
    """
    create_mask : create mask form img

    """
    mask = img.copy()
    i = 0
    j = 0
    while i < 800:
        j = 0
        while j < 800:
            if (int(mask[i, j, 0]) + int(mask[i, j, 1]) + int(mask[i, j, 2])) < 700:
                mask[i, j, 0] = 0
                mask[i, j, 1] = 0
                mask[i, j, 2] = 0
            j += 1
        i += 1
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    return mask


"""
how to use ?
1. read image
img = cv2.imread('test.jpg')

2. create mask
mask = create_mask(img)

3. clean white line
img = vis_convert(img,mask)

4. done!!
"""

img = cv2.imread('test5.jpg')
mask = create_mask(img)
img = vis_convert(img, mask)

cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey(0)