import cv2
import numpy as np
import matplotlib.pyplot as plt
import core.utils as ut


img1 = cv2.imread("assets/walter.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("assets/black_white_image.jpg", cv2.IMREAD_GRAYSCALE)

def salt_pepper_noise(image, prob=0.02):
    noisy = np.copy(image)
    white = np.random.rand(*image.shape) < (prob / 2)
    noisy[white] = 255
    black = np.random.rand(*image.shape) < (prob / 2)
    noisy[black] = 0
    return noisy

img1_noisy = salt_pepper_noise(img1)
img2_noisy = salt_pepper_noise(img2)


def apply_filters(image):
    results = {}
    for k in [3,5,7]:

        # Média (Box)
        mean = cv2.blur(image, (k,k))

        # Mediana
        median = cv2.medianBlur(image, k)

        # Bartlett (Triangular) -> aproximação com filtro separável
        kernel = np.array([list(range(1, k//2+2)) + list(range(k//2, 0, -1))])
        kernel = kernel / kernel.sum()
        bartlett = cv2.sepFilter2D(image, -1, kernel, kernel)
        
        results[f"Mean {k}x{k}"] = mean
        results[f"Median {k}x{k}"] = median
        results[f"Bartlett {k}x{k}"] = bartlett
    return results

filters_img1 = apply_filters(img1_noisy)
filters_img2 = apply_filters(img2_noisy)

ut.show_images([img1, img1_noisy], ["Original", "Com Ruído"])
for name, result in filters_img1.items():
    ut.show_images([img1_noisy, result], ["Ruído", name])

# Aplicar Sobel  # https://docs.opencv.org/3.4/d2/d2c/tutorial_sobel_derivatives.html
def sobel_filters(image):
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = cv2.magnitude(sobel_x, sobel_y)
    return (np.uint8(np.abs(sobel_x)), np.uint8(np.abs(sobel_y)), np.uint8(magnitude)) 

sx, sy, mag = sobel_filters(img1)
ut.show_images([sx, sy, mag], ["Sobel X (Original)", "Sobel Y (Original)", "Magnitude (Original)"])

sx_n, sy_n, mag_n = sobel_filters(img1_noisy)
ut.show_images([sx_n, sy_n, mag_n], ["Sobel X (Ruído)", "Sobel Y (Ruído)", "Magnitude (Ruído)"])

for name, f_img in filters_img1.items():
    sx_f, sy_f, mag_f = sobel_filters(f_img)
    ut.show_images([sx_f, sy_f, mag_f], [f"Sobel X ({name})", f"Sobel Y ({name})", f"Magnitude ({name})"])
