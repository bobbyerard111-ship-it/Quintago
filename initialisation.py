def initialisation_grille():
      L1 = [[0, 0, 0],   # liste qui constitue un des quatres cadrans, elle-meme constituée de listes représentant les demi-lignes (coupure verticale) de la grille de jeu 
            [0, 0, 0],   # les 0 représente les cases vides
            [0, 0, 0]] 

      L2 = [[0, 0, 0],  
            [0, 0, 0],  
            [0, 0, 0]] 

      L3 = [[0, 0, 0],  
            [0, 0, 0],  
            [0, 0, 0]] 

      L4 = [[0, 0, 0],  
            [0, 0, 0],  
            [0, 0, 0]]
      
      XL1 = [L1, L2]     # liste correspondant à la moitié de grille de jeu (coupure horizontale)
      XL2 = [L3, L4]     
      return [XL1, XL2]   # liste correspondant à la grille de jeu

