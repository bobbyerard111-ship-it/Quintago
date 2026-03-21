def configuration():
   L1 = [[0, 1, 2],   # liste qui constitue un des quatres cadrans, elle-meme constituée de listes représentant les demi-lignes (coupure verticale) de la grille de jeu
         [0, 1, 2], 
         [0, 1, 2]]
      
   L2 = [[0, 1, 2], 
         [0, 1, 2], 
         [0, 1, 2]]
    
   L3 = [[0, 1, 2], 
         [0, 1, 2], 
         [0, 1, 2]]
    
   L4 = [[0, 1, 2], 
         [0, 1, 2], 
         [0, 1, 2]]
    
   XL1 = [L1, L2]     # liste correspondant à la moitié de grille de jeu (coupure horizontale)
   XL2 = [L3, L4]     
   XXL = [XL1, XL2]   # liste correspondant à la grille de jeu
