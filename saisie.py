from tour_de_jeu import *
from initialisation import *

# instruction 3 (i) 
def jouer_case(grille, nb_joueur): 
   """
    But :
        Permettre à un joueur de choisir une case valide et y placer son pion.

    Entrée :
        - grille : grille de jeu
        - nb_joueur : numéro du joueur (1 ou 2)

    Sortie :
        Aucune (la grille est modifiée)
    """

   test_coordonnées = 0 
   while test_coordonnées == 0: 
      test = 0      # remplace le role d'un break 
      
      while test == 0:  # on force la saisie 
         try:       # permet de tester le type de la saisie : dans ce cas précis si ce n'est pas un entier on passe directement aux lignes 31 et 32 qui indiquent que la saisie est invalide 
            jouer_ligne = int(input("Rentrez la ligne : ")) 
            if 1 <= jouer_ligne <= 6: 
               test = 1  # sortie si saisie valide  
         except ValueError:        # cas de saisie invalide (pas un entier) 
            print("Entrée invalide.")       
     
      test = 0 
      while test == 0: 
         try: 
            jouer_colonne = int(input("Rentez la colonne : ")) 
            if 1 <= jouer_colonne <= 6: 
               test = 1  # sortie si saisie valide  
         except ValueError: 
            print("Entrée invalide.")    

      # on créer une variable gagnant qui permettra de vérifier facilement si la case a déjà été jouée  
      if jouer_colonne <= 3:    # on sépare les 4 sous-listes pour faciliter la lisibilité et la compréhension du code 
         if jouer_ligne <= 3:    
            case = grille[0][0][jouer_ligne-1][jouer_colonne-1]   # on soustrait 1 car dans la saisie de l'utilisateur les lignes et les colonnes commençaient à 1    
         else: 
            case = grille[1][0][jouer_ligne-1-3][jouer_colonne-1]  # on enlève 1 pour la raison précédente et encore 3 car la ligne 4 du joueur(saisie) correspond à l'indice 0 de L3 et ainsi de suite (décalge de 3) 
      else: 
         if jouer_ligne <= 3: 
            case = grille[0][1][jouer_ligne-1][jouer_colonne-1-3]  # on enlève à jouer_colonne 3 car la colonne 4 du joueur(saisie) correspond à l'indice 0 de L2 et ainsi de suite (décalge de 3) 
         else: 
            case = grille[1][1][jouer_ligne-1-3][jouer_colonne-1-3]

      if case != 1 and case != 2: # on vérifie que la case saisie n'a pas déjà été jouée
         test_coordonnées = 1      # cela nous permettra de sortir de la boucle while 

   # modification réelle de la grille (corrigé)
   if jouer_colonne <= 3:
      if jouer_ligne <= 3:
         grille[0][0][jouer_ligne-1][jouer_colonne-1] = nb_joueur
      else:
         grille[1][0][jouer_ligne-1-3][jouer_colonne-1] = nb_joueur
   else:
      if jouer_ligne <= 3:
         grille[0][1][jouer_ligne-1][jouer_colonne-1-3] = nb_joueur
      else:
         grille[1][1][jouer_ligne-1-3][jouer_colonne-1-3] = nb_joueur