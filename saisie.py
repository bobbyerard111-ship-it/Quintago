from quintago import *
from tour_de_jeu import *

# instruction 3 (i)
def jouer_case():
    test = 0      # remplace le role d'un break
    while test == 0:  # on force la saisie
        try:       # permet de tester le type de la saisie : dans ce cas précis si ce n'est pas un entier on passe directement aux lignes 31 et 32 qui indiquent que la saisie est invalide
            jouer_ligne = int(input("Veuillez indiquer la ligne de la case à jouer: par exemple 1 pour la première ligne en partant du haut"))
            if 1 <= jouer_ligne <= 6:
                test = 1  # sortie si saisie valide 
      
        except ValueError:        # cas de saisie invalide (pas un entier)
            print("Entrée invalide.")      
   
    test = 0
    while True:
        try:
            jouer_colonne = int(input("Veuillez indiquer la colonne de la case à jouer: par exemple 1 pour la première colonne en partant de la gauche"))
            if 1 <= jouer_colonne <= 6:
                test = 1  # sortie si saisie valide 

        except ValueError:
            print("Entrée invalide.")    

    if jouer_colonne <= 3:    # on sépare les 4 sous-listes pour faciliter la lisibilité et la compréhension du code
        if jouer_ligne <= 3:
            L1[jouer_ligne-1][jouer_colonne-1] = "X"   # on soustrait 1 car dans la saisie de l'utilisateur les lignes et les colonnes commençaient à 1 
        else:
            L3[jouer_ligne-1-3][jouer_colonne-1] = "X" # on enlève 1 pour la raison précédente et encore 3 car la ligne 4 du joueur(saisie) correspond à l'indice 0 de L3 et ainsi de suite (décalge de 3)
    else:
        if jouer_ligne <= 3:
            L2[jouer_ligne-1][jouer_colonne-1-3] = "X"  # on enlève à jouer_colonne 3 car la colonne 4 du joueur(saisie) correspond à l'indice 0 de L2 et ainsi de suite (décalge de 3)
        else:
            L4[jouer_ligne-1-3][jouer_colonne-1-3] = "X"


