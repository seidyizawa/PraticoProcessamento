import cv2
import numpy as np
import copy

def ativ1(img1,lim):
    img2 = copy.copy(img1)
    linhas, colunas = img1.shape
    for i in range(0, int(linhas)):
	for j in range(0, colunas):
		if img.item(i,j) > lim:
                    img.itemset((i,j),0)
    cv2.imwrite('ativ1.png',img2) 
    return img2;
    
def ativ2(img1,gam):
    img2 = copy.copy(img1)
    cv2.imwrite('ativ2.png',img2)
    return img2;

def ativ3(img1):
    img2 = copy.copy(img1)
    linhas, colunas = img1.shape
    for i in range(0, int(linhas)):
	for j in range(0, colunas):
		negativo = 255 - img.item(i, j)
                img2.itemset((i, j), negativo)
    cv2.imwrite('ativ3.png',img2)
    return img2;

def ativ4(img1,inthini,inthfim,intvini,intvfim):
    img2 = img1[inthini:inthfim,intvini:intvfim]
    cv2.imwrite('ativ4.png',img2)
    return img2;

def ativ5(img1,mask):
    img2 = copy.copy(img1)
    cv2.imwrite('ativ5.png',img2)
    return img2;

def ativ6(img1,mask):
    img2 = copy.copy(img1)
    cv2.imwrite('ativ6.png',img2)
    return img2;

def ativ7(img1,mask):
    img2 = copy.copy(img1)
    cv2.imwrite('ativ7.png',img2)
    return img2;

def ativ8(img1,mask):
    img2 = copy.copy(img1)
    cv2.imwrite('ativ8.png',img2)
    return img2;

def show(img1,img2):
    cv2.imshow('image',img)
    cv2.imshow('image2'img2)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    return

img = cv2.imread('img01-a.png',cv2.IMREAD_COLOR)
lim = 50
gam = 200
inthini = 60
inthfim = 200
intvfim = 200
infvini = 60
mask = 3
show(img,ativ1(img,lim))
show(img,ativ2(img,gam))
show(img,ativ3(img))
show(img,ativ4(img,inthini,inthfim,intvini,intvfim))
show(img,ativ5(img,mask))
show(img,ativ6(img,mask))
show(img,ativ7(img,mask))
show(img,ativ8(img,mask))
