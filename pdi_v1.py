
import cv2 as cv
import numpy as np
import core.utils as ut
import matplotlib.pyplot as plt

image = ut.ler_imagem("assets/walter.jpg")
#image = ut.ler_imagem("assets/black_white_image.jpg")

def median(image):
    median = cv.medianBlur(image, 5)  
    return median

def medianBox(image, k=5):
    mean = cv.blur(image, (k,k)) 
    return mean


def salt_pepper_noise(image, prob=0.02):
    noisy = np.copy(image)
    white = np.random.rand(*image.shape) < (prob / 2) 

    noisy[white] = 255
    black = np.random.rand(*image.shape) < (prob / 2)   

    noisy[black] = 0

    return noisy

def sobel_filters(image):
    sobel_x = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=3)
    sobel_y = cv.Sobel(image, cv.CV_64F, 0, 1, ksize=3)
    magnitude = cv.magnitude(sobel_x, sobel_y)

    return (np.uint8(np.abs(sobel_x)), np.uint8(np.abs(sobel_y)), np.uint8(magnitude)) 

def concat_images(img_list):
    h, w = img_list[0].shape[:2]
    resized = [cv.resize(img, (w, h)) for img in img_list]
    return cv.vconcat(resized)  # horizontal (lado a lado)

original = cv.imread("assets/walter.jpg", cv.IMREAD_GRAYSCALE)
noisy = salt_pepper_noise(original)
median_img = median(noisy)
mean_img = medianBox(noisy)

combined = concat_images([original, noisy, median_img, mean_img])
ut.showImage(combined)

