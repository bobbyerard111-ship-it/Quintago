# instruction 3

def jouer_case():
   L1 = [[0, 1, 2], 
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
    
   XL1 = [L1, L2]
   XL2 = [L3, L4]
   XXL = [XL1, XL2]

   jouer_ligne = int(input("Veuillez indiquer la ligne de la case à jouer: par exemple 1 pour la première ligne en partant du haut"))
   while jouer_ligne        # voir comment redemander de saisr si pas int 
   jouer_colonne = int(input("Veuillez indiquer la colonne de la case à jouer: par exemple 1 pour la première colonne en partant de la gauche"))
   while jouer_ligne
   if jouer_colonne <= 3:
      if jouer_ligne <= 3:
         L1[jouer_ligne] = 
      else:
         L3[jouer_ligne]
   else:
      if jouer_ligne <= 3:
         L2[jouer_ligne] = 
      else:
         L4[jouer_ligne]


def rotation_droite():
  if numero_sous_grille_rotation == 1:
      sous_grille = L1
   elif numero_sous_grille_rotation == 2:
      sous_grille = L2
   elif numero_sous_grille_rotation == 3:
      sous_grille = L3
   else:
      sous_grille = L4
   
   sous_grille[0][0], sous_grille[0][2], sous_grille[2][2], sous_grille[2][0] = sous_grille[0][2], sous_grille[2][2], sous_grille[2][0], sous_grille[0][0] # on s'occupe des permutations des jetons situés sur les coins
   sous_grille[0][1], sous_grille[1][2], sous_grille[2][1], sous_grille[1][0] = sous_grille[1][2], sous_grille[2][1], sous_grille[1][0], sous_grille[0][1] # on s'occupe des permutations des jetons en excluant les coins
      
def rotation_gauche():
   if numero_sous_grille_rotation == 1:
      sous_grille = L1
   elif numero_sous_grille_rotation == 2:
      sous_grille = L2
   elif numero_sous_grille_rotation == 3:
      sous_grille = L3
   else:
      sous_grille = L4
   
   sous_grille[0][0], sous_grille[2][0], sous_grille[2][2], sous_grille[0][2] = sous_grille[2][0], sous_grille[2][2], sous_grille[0][2], sous_grille[0][0]
   sous_grille[0][1], sous_grille[1][0], sous_grille[2][1], sous_grille[1][2] = sous_grille[1][0], sous_grille[2][1], sous_grille[1][2], sous_grille[0][1]


def jouer_tour():
   jouer_case()
   num_sous_grille_rotation = int(input("Veuillez saisir le numéro de sous-grille sachant que 1, 2, 3, 4 désigne les sous-grilles en haut à gauche, en haut à droite, en bas à gauche, en bas à droite"))
   while   # forcer saisie
   
   sens_rotation = int(input("Veuillez saisir un sens de rotation de la sous-grille D pour droite et G pour gauche"))
   while sens_rotation =!"D" or sens_rotation =!"d" sens_rotation =!"G" or sens_rotation =!"g" # forcer saisie
      sens_rotation = int(input("Veuillez saisir un sens de rotation valide de la sous-grille D pour droite et G pour gauche"))
   if sens_rotation == "D" or "d":
      rotation_droite()
   else: 
      rotation_gauche()
