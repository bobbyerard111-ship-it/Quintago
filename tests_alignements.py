from parametres import *
from quintago import *


def grille_plate(grille):
    """
    Convertir une liste en 4D en une grille 2D de dimensions 6x6 sans tenir compte des sous-grille
    Paramètre : grille (liste) : grille de jeu en 4D
                                 grille[i][j] est la sous-grille de la ligne i, colonne j   
                                 grille[i][j][l][c] est la case à la ligne l, colonne c de la sous-grille de la ligne i, colonne j

    Retourne: plat (liste) : liste en 2D 6x6, une autre représentation de la grille complète, plus simple à traiter pour les test d'alignement
    """
    plat = [[0] * TAILLE for _ in range(TAILLE)]

    for sg_lig in range(NB_SG): #indice de ligne des sous-grilles (0 ou 1)
        for sg_col in range(NB_SG): # indice de colonne des sous-grilles (0 ou 1)
            for l in range(TAILLE_SG): #ligne dans la sous-grille
                for c in range(TAILLE_SG): # colonne dans la sous-grille
                    # Calcul des coordonnées dans la grille plate
                    lig = sg_lig * TAILLE_SG + l
                    col = sg_col * TAILLE_SG + c
                    plat[lig][col] = grille[sg_lig][sg_col][l][c]

    return plat


def cinq_alignes(sequence, joueur, alignement=ALIGNEMENT):
    """
    Vérifie si une séquence (ligne, colonne ou diagonale) contient au moins 5 occurences du pion du joueur.

    Paramètres: sequence (liste) : liste de valeurs de cases d'une séquence
                joueur (int) : numéro de joueur (1 ou 2)
                alignement_gagnant (int) : longueur de l'alignement gagnant (5 dans notre cas)

    Retourne : booléen : True si alignement trouvé, False sinon
    """
    cpt = 0
    for case in sequence:
        if case == joueur:
            cpt += 1
            if cpt >= alignement:
                return True
        else:
            cpt = 0
    return False

def alignement_horizontal(grille, joueur):
    """
    Teste s'il existe un alignement horizontal gagnant pour le joueur donné.

    Paramètres : grille (liste) : grille de jeu en 4D
                 joueur (int) : numéro du joueur (1 ou 2)

    Retourne : booléen : True si le joueur a 5 pions alignés horizontalement, False sinon
    """
    plat = grille_plate(grille)
    
    for lig in range(len(plat)):
        # Chaque ligne est une séquence à tester
        if cinq_alignes(plat[lig], joueur):
            return True
        
    return False

def alignement_vertical(grille, joueur):
    """
    Teste s'il existe un alignement vertical gagnant pour le joueur donné.

    Paramètres : grille (liste) : grille de jeu sous forme de liste 4D
                 joueur (int) : numéro du joueur (1 ou 2)

    Retourne: booléen : True si le joueur a 5 pions alignés verticalement, False sinon
    """
    plat = grille_plate(grille)

    for col in range(len(plat)):
        # On fait une liste qui représente une colonne
        colonne = [plat[lig][col] for lig in range(len(plat))]
        if cinq_alignes(colonne, joueur):
            return True
        
    return False

def alignement_diagonal(grille, joueur):
    """
    Teste s'il existe un alignement diagonal gagnant pour le joueur donnée.
    Vérifie les deux sens de diagonales (haut-gauche vers bas-droite et haut-droite vers bas-gauche).

    Paramètres : grille (liste) : grille de jeu sous forme de liste 4D
                 joueur (int) : numéro du joueur (1 ou 2)

    Retourne : bool : True si le joueur a 5 pions alignés en diagonale, False sinon
    """

    plat = grille_plate(grille)
    taille = len(plat)

    # Diagonales descendantes (haut-gauche vers bas-droite)
    # On parcourt toutes les diagonales possibles en faisant varier le point de départ
    for depart in range(-(taille -1), taille):
        #depart représente l'écart entre l'indice de ligne et de colonne (lig - col = constate)

        diag = []
        for lig in range(taille):
            col = lig - depart
            if 0 <= col < taille:
                diag.append(plat[lig][col])

        if cinq_alignes(diag, joueur):
            return True
    
    # Diagonales montantes (bas-gauche vers haut-droite)
    # La somme lig + col est constante sur chaque diagonales inversées

    for total in range((2 * taille) -1):
        diag_inv = []
        for lig in range(taille):
            col = total - lig
            if 0 <= col < taille:
                diag_inv.append(plat[lig][col])
        if cinq_alignes(diag_inv, joueur):
            return True

    return False

def test_victoire(grille):
    if alignement_horizontal(grille, 1) or alignement_vertical(grille, 1) or alignement_diagonal(grille, 1):
        if alignement_horizontal(grille, 2) or alignement_vertical(grille, 2) or alignement_diagonal(grille, 2):
            return -1
        else:
            return 1
    elif alignement_horizontal(grille, 2) or alignement_vertical(grille, 2) or alignement_diagonal(grille, 2):
        return 2        # en effet, il ne peut y avoir qu'une valeur retournée pas fonction donc si les deux joueurs sont victorieux 2 ne sera pas retourné 
    else:
        return 0