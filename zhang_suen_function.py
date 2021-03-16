from neighbors import get_neighbors

def zhang_suen(image):
    
    thinned_img = image.copy()
    step1 = step2 = 1
    while step1 or step2:
        step1 = []
        

        #to_change = []
        # step 1
        for x in range(1, thinned_img.shape[0]-1):
            for y in range(1, thinned_img.shape[1]-1):
                a_p1, b_p1, neighbors = get_neighbors(x, y, thinned_img)
                if thinned_img[x,y] == 1:
                    if 2<= b_p1 <= 6:
                        if a_p1 == 1:
                            if neighbors[0] * neighbors[2] * neighbors[4] == 0:
                                if neighbors[2] * neighbors[4] * neighbors[6] == 0:
                                    step1.append((x, y))
        for x,y in step1:
            thinned_img[x][y] = 0
            
        step2 = []
        for x in range(1, thinned_img.shape[0]-1):
            for y in range(1, thinned_img.shape[1]-1):
                a_p1, b_p1, neighbors = get_neighbors(x, y, thinned_img)
                if thinned_img[x,y] == 1:
                    if 2<= b_p1 <= 6:
                        if a_p1 == 1:
                            if neighbors[0] * neighbors[2] * neighbors[6] == 0:
                                if neighbors[0] * neighbors[4] * neighbors[6] == 0:
                                    step2.append((x, y))
                                    

        for x,y in step2:
            thinned_img[x][y] = 0

    return thinned_img
    
