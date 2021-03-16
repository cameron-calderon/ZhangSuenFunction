#My observations from the score distribution plots is the less the search area the closer the 
#genuine and imposter scores are together. The d prime score varies from plot to plot. 
#But from my understanding the bigger the search area the more accurate data can be recovered
from skimage import io
import matplotlib.pyplot as plt
from zhang_suen_function import zhang_suen
from minutiae import find_minutiae
import os
from skimage.filters import threshold_otsu
import performance

# Function to compute the Jaccard similarity
def jaccard(list1, list2):
    try:
        intersection = len(list(set(list1).intersection(list2)))
        union = (len(list1) + len(list2)) - intersection
        return float(intersection) / union   
    except:
        return 0     

# search area for minutiae points
search_area = [5, 10, 15, 20]

for to_search in search_area:

    X = []
    y = []
    
    database = "hw_data/"
    files = os.listdir(database)
    
    for file in files:
           
        # -------------------------------------------
        # Load the image
        image_file = database + file
        img = io.imread(image_file, as_gray=True)
        
        # -------------------------------------------
        # Plot the untouched image
        fig, axes = plt.subplots(1, 3)
        axes[0].imshow(img, cmap='gray')
        
        # -------------------------------------------
        # Apply a filter to create binary version of the image
        Otsu_Threshold = threshold_otsu(img)   
        binary_img = img < Otsu_Threshold
        binary_img = binary_img * 1
                      
        # -------------------------------------------
        # Plot the binary image
        axes[1].imshow(binary_img, cmap='gray')
        
        # -------------------------------------------
        # Call the zhang-suen thinning function, 
        # apply it to the binary image, 
        
        thinned_img = zhang_suen(binary_img)
        axes[2].imshow(thinned_img, cmap='gray')
        plt.savefig(file.replace(".BMP",".png"))
        plt.close()
        
        # Get minutiae points
        bif, term = find_minutiae(thinned_img, to_search)
        
        X.append((bif, term))
        y.append(file.split("_")[0])
        
    # --------------------------------------------------------------------
        
    gen_scores = []
    imp_scores = []
    for i in range(len(y)):
        bifT = X[i][0]
        termT = X[i][1]
        for j in range(len(y)):             
            bifQ = X[j][0]
            termQ = X[j][1]      
            score1 = jaccard(bifT, bifQ)  
            score2 = jaccard(termT, termQ)
            score = (score1 + score2) / 2.
            if y[i] == y[j]:
                gen_scores.append(score)
            else:
                imp_scores.append(score)
                           
    far, frr, tpr = performance.compute_rates(gen_scores, imp_scores, 100)
    performance.plot_scoreDist(gen_scores, imp_scores, "Score Distribution Plot, Search Area %d" % to_search)
    
    
    
    
    
    
