
import cv2 as cv
import core.utils as ut


def median(image):
    median = cv.medianBlur(image, 5)
    return median

image = ut.ler_imagem("assets/saltandpepperruid.jpg")

image = median(image)

ut.showImage(image)
