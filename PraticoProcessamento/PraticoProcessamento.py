#!/usr/bin/python


# Importacao de bibliotecas
import cv2
import numpy as np

# Abre a imagem
# - cv2.IMREAD_COLOR
# - cv2.IMREAD_GRAYSCALE
# - cv2.IMREAD_UNCHANGED

#img = cv2.imread('a.jpg', cv2.IMREAD_COLOR)
img = cv2.imread('img01-a.jpg', cv2.IMREAD_GRAYSCALE)

# Acesso a um pixel
# Modo1: ineficiente
#pixel = img[100, 100]
#print(pixel)

# Modo2: eficiente
print('Dimensao da imagem')
print(img.shape)

print('Tamanho da imagem')
print(img.size)

linhas, colunas = img.shape
print('linhas:  ' + str(linhas))
print('colunas: ' + str(colunas))

for i in range(0, int(linhas / 2)):
	for j in range(0, colunas):
		negativo = 255 - img.item(i, j)
		img.itemset((i, j), negativo)





# Exibe a imagem na tela
cv2.imshow('imagem', img)
cv2.imwrite('negativo.png', img)

# Espera alguma tecla
tecla = cv2.waitKey(0)

# tecla 27 = ESC
cv2.destroyAllWindows()
