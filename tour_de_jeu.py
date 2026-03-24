from saisie import *
from initialisation import *

def rotation_droite(num_sous_grille_rotation):
   if num_sous_grille_rotation == 1:
      sous_grille = L1
   elif num_sous_grille_rotation == 2:
      sous_grille = L2
   elif num_sous_grille_rotation == 3:
      sous_grille = L3
   else:
      sous_grille = L4
   
   sous_grille[0][0], sous_grille[0][2], sous_grille[2][2], sous_grille[2][0] = sous_grille[0][2], sous_grille[2][2], sous_grille[2][0], sous_grille[0][0] # on s'occupe des permutations des jetons situés sur les coins
   sous_grille[0][1], sous_grille[1][2], sous_grille[2][1], sous_grille[1][0] = sous_grille[1][2], sous_grille[2][1], sous_grille[1][0], sous_grille[0][1] # on s'occupe des permutations des jetons en excluant les coins
      
def rotation_gauche(num_sous_grille_rotation):
   if num_sous_grille_rotation == 1:
      sous_grille = L1
   elif num_sous_grille_rotation == 2:
      sous_grille = L2
   elif num_sous_grille_rotation == 3:
      sous_grille = L3
   else:
      sous_grille = L4
   
   sous_grille[0][0], sous_grille[2][0], sous_grille[2][2], sous_grille[0][2] = sous_grille[2][0], sous_grille[2][2], sous_grille[0][2], sous_grille[0][0]
   sous_grille[0][1], sous_grille[1][0], sous_grille[2][1], sous_grille[1][2] = sous_grille[1][0], sous_grille[2][1], sous_grille[1][2], sous_grille[0][1]


def jouer_tour(nb_joueur):
   jouer_case(nb_joueur)
   test = 0
   while test == 0:  # on force la saisie 
         try:       # permet de tester le type de la saisie : dans ce cas précis si ce n'est pas un entier on passe directement aux lignes 31 et 32 qui indiquent que la saisie est invalide 
            num_sous_grille_rotation = int(input("Veuillez saisir le numéro de sous-grille sachant que 1, 2, 3, 4 désigne les sous-grilles en haut à gauche, en haut à droite, en bas à gauche, en bas à droite"))
            if 1 <= num_sous_grille_rotation <= 4: 
               test = 1  # sortie si saisie valide  
         except ValueError:        # cas de saisie invalide (pas un entier) 
            print("Entrée invalide.")        # forcer saisie
   
   sens_rotation = int(input("Veuillez saisir un sens de rotation de la sous-grille D pour droite et G pour gauche"))
   
   while sens_rotation !="D" and sens_rotation !="d" and sens_rotation !="G" and sens_rotation !="g": # forcer saisie
      sens_rotation = int(input("Veuillez saisir un sens de rotation valide de la sous-grille D pour droite et G pour gauche"))
   
   if sens_rotation == "D" or "d":
      rotation_droite(num_sous_grille_rotation)
   else: 
      rotation_gauche(num_sous_grille_rotation)