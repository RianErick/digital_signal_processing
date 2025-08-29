
import cv2 as cv
import numpy as np

def ler_imagem(caminho_imagem):
    imagem = cv.imread(caminho_imagem, cv.IMREAD_COLOR)

    if imagem is None:
        print(f"Não foi possível ler a imagem: {caminho_imagem}")
    return imagem

def showImage(imagem):
    cv.imshow("Imagem", imagem)
    cv.waitKey(0)
    cv.destroyAllWindows()

def blur(image):
    blur = cv.GaussianBlur(image, (7,7), 0)
    return blur

def median(image):
    median = cv.medianBlur(image, 5)
    return median

def saveImage(image, path):
    cv.imwrite(path, image)

image = ler_imagem("assets/saltandpepperruid.jpg")


# image_blur = blur(image)
# showImage(image_blur)

image_median = median(image)
showImage(image_median)

saveImage(image_median, "result/saltandpepperruid_median.jpg")