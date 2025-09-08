import cv2 as cv
import matplotlib.pyplot as plt
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

def saveImage(image, path):
    cv.imwrite(path, image)
    
def show_images(images, titles, cmap='gray'):
    plt.figure(figsize=(15,5))
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(1, len(images), i+1)
        plt.imshow(img, cmap=cmap)
        plt.title(title)
        plt.axis("off")
    plt.show()