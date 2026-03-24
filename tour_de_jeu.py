from saisie import *
from initialisation import *

def rotation_gauche(grille, num_sous_grille_rotation):
   """
    But :
        Effectuer une rotation vers la gauche (sens anti-horaire) d’une sous-grille 3x3.

    Entrée :
        - grille : grille principale
        - num_sous_grille_rotation : numéro de la sous-grille (1 à 4)

    Sortie :
        Aucune (modifie directement la grille)
   """
   if num_sous_grille_rotation == 1:   # création de variable sous_grille égale aux positions de la sous_grille dans la grille
      sous_grille = grille[0][0]
   elif num_sous_grille_rotation == 2:
      sous_grille = grille[0][1]
   elif num_sous_grille_rotation == 3:
      sous_grille = grille[1][0]
   else:
      sous_grille = grille[1][1]
   
   sous_grille[0][0], sous_grille[0][2], sous_grille[2][2], sous_grille[2][0] = sous_grille[0][2], sous_grille[2][2], sous_grille[2][0], sous_grille[0][0] # on s'occupe des permutations des jetons situés sur les coins
   sous_grille[0][1], sous_grille[1][2], sous_grille[2][1], sous_grille[1][0] = sous_grille[1][2], sous_grille[2][1], sous_grille[1][0], sous_grille[0][1] # on s'occupe des permutations des jetons en excluant les coins
      
def rotation_droite(grille, num_sous_grille_rotation):
   """
    But :
        Effectuer une rotation vers la droite (sens horaire) d’une sous-grille 3x3.

    Entrée :
        - grille : grille principale
        - num_sous_grille_rotation : numéro de la sous-grille (1 à 4)

    Sortie :
        Aucune (modifie directement la grille)
   """

   if num_sous_grille_rotation == 1:
      sous_grille = grille[0][0]
   elif num_sous_grille_rotation == 2:
      sous_grille = grille[0][1]
   elif num_sous_grille_rotation == 3:
      sous_grille = grille[1][0]
   else:
      sous_grille = grille[1][1]
   
   sous_grille[0][0], sous_grille[2][0], sous_grille[2][2], sous_grille[0][2] = sous_grille[2][0], sous_grille[2][2], sous_grille[0][2], sous_grille[0][0]
   sous_grille[0][1], sous_grille[1][0], sous_grille[2][1], sous_grille[1][2] = sous_grille[1][0], sous_grille[2][1], sous_grille[1][2], sous_grille[0][1]


def jouer_tour(grille, nb_joueur):
   """
    But :
        Faire jouer un tour complet à un joueur (placement + rotation).

    Entrée :
        - grille : grille de jeu
        - nb_joueur : numéro du joueur (1 ou 2)

    Sortie :
        Aucune (modifie la grille)
   """
   jouer_case(grille, nb_joueur)
   test = 0
   while test == 0:  # on force la saisie 
         try:       # permet de tester le type de la saisie : dans ce cas précis si ce n'est pas un entier on passe directement aux lignes 31 et 32 qui indiquent que la saisie est invalide 
            num_sous_grille_rotation = int(input("Choisissez une sous-grille : 1 (haut gauche), 2 (haut droite), 3 (bas gauche), 4 (bas droite) : "))
            if 1 <= num_sous_grille_rotation <= 4: 
               test = 1  # sortie si saisie valide  
         except ValueError:        # cas de saisie invalide (pas un entier) 
            print("Entrée invalide.")        # forcer saisie
   
   sens_rotation = input("Veuillez saisir un sens de rotation : D (droite), G (gauche) : ")
   
   while sens_rotation !="D" and sens_rotation !="d" and sens_rotation !="G" and sens_rotation !="g": # forcer saisie
      sens_rotation = input("Veuillez saisir un sens de rotation valide de la sous-grille D pour droite et G pour gauche : ")
   
   if sens_rotation == "D" or "d":
      rotation_droite(grille, num_sous_grille_rotation)      # application du sens de rotation en fonction de la saisie de l'utilisateur
   else: 
      rotation_gauche(grille, num_sous_grille_rotation)