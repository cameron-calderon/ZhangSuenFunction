import numpy as np
from neighbors import get_neighbors

def find_minutiae(img, radius):  
    bif = []   
    term = []    
    for x in range(1, img.shape[0]-1, radius):        
        for y in range(1, img.shape[1]-1, radius): 
            a, b, neighbors = get_neighbors(x, y, img)
            if(b==1):
                term.append(img[x,y])
            elif(b==3):
                bif.append(img[x,y])
    return bif, term




            