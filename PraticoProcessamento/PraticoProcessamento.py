import cv2
import numpy as np
import copy
import array

def limiarizacao(img1,lim):
    img2 = copy.copy(img1)
    for i in range(0, img1.shape[0]-1):
        for j in range(0, img1.shape[1]-1):
            if img1.item(i,j,0) >= lim:
                img2[i,j] = 0
    cv2.imwrite('ativ1.png',img2) 
    return img2;
    
def gamma(img1,gamma):
    img2 = adjust_gamma(original, gamma)
    cv2.imwrite('ativ2.png',img2)
    return img2;

def gamma(image, gammma):
   invGamma = 1.0 / gammma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")
   return cv2.LUT(image, table)

def negativo(img1):
    img2 = copy.copy(img1)
    for i in range(0, img1.shape[0]-1):
        for j in range(0, img1.shape[1]-1):
            nega = 255 - img1[i, j]
            img2[i,j] = nega
    cv2.imwrite('ativ3.png',img2)
    return img2;

def fatiamento(img1,inthini,inthfim,intvini,intvfim):
    img2 = img1[inthini:inthfim,intvini:intvfim]
    cv2.imwrite('ativ4.png',img2)
    return img2;

def media(img1,mask):
    img2 = copy.copy(img1)
    masc = []
    mascara = np.ones((mask,mask),np.float32)/(mask*mask)
    for i in range(mask, img1.shape[0]-1):
        for j in range(mask, img1.shape[1]-1):
            for y in range(i-mask/2,i+mask/2):
                for x in range(j-mask/2,j+mask/2):
                   masc.extend(img1[y,x])
            img2[i,j] = np.mean(masc)
            masc = []
    cv2.imwrite('ativ5.png',img2)
    return img2;

def mediana(img1,mask):
    img2 = copy.copy(img1)
    masc = []
    mascara = np.ones((mask,mask),np.float32)/(mask*mask)
    for i in range(mask, img1.shape[0]-1):
        for j in range(mask, img1.shape[1]-1):
            for y in range(i-mask/2,i+mask/2):
                for x in range(j-mask/2,j+mask/2):
                   masc.extend(img1[y,x])
            masc.sort()
            img2[i,j] = masc[mask*mask/2]
            masc = []
    cv2.imwrite('ativ6.png',img2)
    return img2;

def min(img1,mask):
    img2 = copy.copy(img1)
    masc = []
    mascara = np.ones((mask,mask),np.float32)/(mask*mask)
    for i in range(mask, img1.shape[0]-1):
        for j in range(mask, img1.shape[1]-1):
            for y in range(i-mask/2,i+mask/2):
                for x in range(j-mask/2,j+mask/2):
                   masc.extend(img1[y,x])
            masc.sort()
            img2[i,j] = masc[0]
            masc = []
    cv2.imwrite('ativ7.png',img2)
    return img2;

def max(img1,mask):
    img2 = copy.copy(img1)
    masc = []
    mascara = np.ones((mask,mask),np.float32)/(mask*mask)
    for i in range(mask, img1.shape[0]-1):
        for j in range(mask, img1.shape[1]-1):
            for y in range(i-mask/2,i+mask/2):
                for x in range(j-mask/2,j+mask/2):
                   masc.extend(img1[y,x])
            masc.sort()
            masc.reverse()
            img2[i,j] = masc[0]
            masc = []
    cv2.imwrite('ativ8.png',img2)
    return img2;

def show(img1,img2):
    cv2.imshow('original',img)
    cv2.imshow('modificado',img2)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    return

img = cv2.imread('img02-a.jpg',cv2.IMREAD_COLOR)
lim = 50
gamma = 0.5
inthini = 60
inthfim = 200
intvfim = 200
intvini = 60
mask = 4
show(img,limiarizacao(img,lim))
show(img,gamma)
show(img,negativo(img))
show(img,fatiamento(img,inthini,inthfim,intvini,intvfim))
show(img,media(img,mask))
show(img,mediana(img,mask))
show(img,max(img,mask))
show(img,min(img,mask))