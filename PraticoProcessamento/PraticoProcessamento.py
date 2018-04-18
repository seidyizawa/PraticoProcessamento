import cv2
import numpy as np
import copy
import array

def limiarizacao(img1,lim):
    img2 = copy.copy(img1)
    linhas, colunas = img1.shape
    for i in range(0, int(linhas)):
	    for j in range(0, colunas):
		    if img.item(i,j) <= lim:
                    img.itemset((i,j),0)
    cv2.imwrite('ativ1.png',img2) 
    return img2;
    
def gamma(img1,gamma):
    img2 = copy.copy(img1)
    img2 = ajuste_gamma(img1, gamma=gamma)
    cv2.imwrite('ativ2.png',img2)
    return img2;

def ajuste_gamma(image, gamma):
   iGamma = 1.0 / gamma
   tabela = np.array([((i / 255.0) ** iGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")
   return cv2.LUT(image, tabela);

def negativo(img1):
    img2 = copy.copy(img1)
    linhas, colunas = img1.shape
    for i in range(0, int(linhas)):
	    for j in range(0, colunas):
		    nega = 255 - img.item(i, j)
            img2.itemset((i, j), nega)
    cv2.imwrite('ativ3.png',img2)
    return img2;

def fatiamento(img1,inthini,inthfim,intvini,intvfim):
    img2 = img1[inthini:inthfim,intvini:intvfim]
    cv2.imwrite('ativ4.png',img2)
    return img2;

def media(img1,mask):
    img2 = copy.copy(img1)
    mascara = np.ones((mask,mask),np.float32)/(mask*mask)
    linhas, colunas = img1.shape
        for i in range(0, int(linhas)):
	        for j in range(0, colunas):
              img2[i,j] = (media/(mask*mask))
    cv2.imwrite('ativ5.png',img2)
    return img2;

def mediana(img1,mask):
    img2 = copy.copy(img1)
    members=[source[0,0]]*(mask*mask)
    for y in range(1,source.shape[0]-1):
        for x in range(1,source.shape[1]-1):
            members[0] = source[y-1,x-1]
            members[1] = source[y,x-1]
            members[2] = source[y+1,x-1]
            members[3] = source[y-1,x]
            members[4] = source[y,x]
            members[5] = source[y+1,x]
            members[6] = source[y-1,x+1]
            members[7] = source[y,x+1]
            members[8] = source[y+1,x+1]
            members.sort()
            img2[y,x]=members[mask*mask/2]
    cv2.imwrite('ativ6.png',img2)
    return img2;

def min(img1,mask):
    img2 = copy.copy(img1)
    members=[source[0,0]]*(mask*mask)
    for y in range(1,source.shape[0]-1):
        for x in range(1,source.shape[1]-1):
            members[0] = source[y-1,x-1]
            members[1] = source[y,x-1]
            members[2] = source[y+1,x-1]
            members[3] = source[y-1,x]
            members[4] = source[y,x]
            members[5] = source[y+1,x]
            members[6] = source[y-1,x+1]
            members[7] = source[y,x+1]
            members[8] = source[y+1,x+1]
            members.sort()
            img2[y,x]=members.index
    cv2.imwrite('ativ7.png',img2)
    return img2;

#def max(img1,mask):
#    img2 = copy.copy(img1)
    members=[source[0,0]]*(mask*mask)
    for y in range(1,source.shape[0]-1):
        for x in range(1,source.shape[1]-1):
            members[0] = source[y-1,x-1]
            members[1] = source[y,x-1]
            members[2] = source[y+1,x-1]
            members[3] = source[y-1,x]
            members[4] = source[y,x]
            members[5] = source[y+1,x]
            members[6] = source[y-1,x+1]
            members[7] = source[y,x+1]
            members[8] = source[y+1,x+1]

            members.sort()
            members.reverse()
            img2[y,x]=members.index
#    cv2.imwrite('ativ8.png',img2)
#    return img2;

def show(img1,img2):
    cv2.imshow('original',img)
    cv2.imshow('modificado',img2)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    return

img = cv2.imread('img01-a.png',cv2.IMREAD_COLOR)
lim = 50
gamma = 0.5
inthini = 60
inthfim = 200
intvfim = 200
infvini = 60
mask = 3
show(img,limiarizacao(img,lim))
show(img,gamma(img,gamma))
show(img,negativo(img))
show(img,fatiamento(img,inthini,inthfim,intvini,intvfim))
show(img,media(img,mask)
show(img,mediana(img,mask))
show(img,max(img,mask))
show(img,min(img,mask))