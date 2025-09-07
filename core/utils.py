import cv2 as cv

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
