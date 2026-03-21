"""
Module contenant les fonctions de sauvegarde et de chargement de la grille pour le jeu Quintago.

Format du fichier 'partie_en_cours.txt' :
    - Ligne 1 : "joueur:X" où X est le numéro du joueur dont c'est le tour (1 ou 2)
    - Ensuite, pour chaque sous-grille (sg), une ligne d'en-tête "sg:I:J" suive des valeurs de la sous-grille, une par ligne, de gauche à droite et de haut en bas.
    - Les valeurs seront : 0 (case vide), 1 (pion joueur 1), 2 (pion joueur 2)

Exemple pour une sous-grille:
    joueur:1
    sg:0:0
    0
    1
    0
    1
    0
    2
    2
    0
    1
    sg:0:1
    ....
"""
from parametres import *


def sauvegarder_grille(grille, nb_joueur):
    """
    Sauvegarde la grille de jeu et le joueur dont c'est le tour au porchain coup dans le fichier 'parti_en_cours.txt'

    Paramètres : grille (liste) : grille de jeu sous forme de liste 4D
                                  nb_joueur : numéro du joueur dont c'est le tour (1 ou 2)
                                  
    Retourne : None
    """
    nb_sg = len(grille)
    taille_sg = len(grille[0][0])

    with open(NOM_FICHIER, "w") as fichier:
        fichier.write("joueur:" + str(nb_joueur) + "\n")
        for i in range(nb_sg):
            for j in range(nb_sg):
                #Identification de la sous-grille (sg:I:J)
                fichier.write("sg:" + str(i) + ":" + str(j) + "\n")
                #Valeurs case par case en sautant des lignes
                for l in range(taille_sg):
                    for c in range(taille_sg):
                        fichier.write(str(grille[i][j][l][c] + "\n"))

    print("Partie sauvegardée dans '" + NOM_FICHIER + "'.")


def charger_grille():
    """
    Charge la grille de jeu et le joueur dont c'est le tour depuis le fichier 'partie_en_cours.txt'.
    Les entêtes "sg:I:J" montrent dans quelle sous-grille écrire les valeurs qui suivent.

    Paramètres : Aucun

    Retourne : (grille, nb_joueur) : tuple si le chargement a réussi :
                    grille (liste) : grille reconstruite en format 4D
                    nb_joueur (int) : numéro du joueur dont c'est le tour (1 ou 2)
                None si le fichier est supprimé ou modifié et que les informations sont par conséquent illisibles.
    """
    try:
        with open(NOM_FICHIER, "r") as fichier:
            pass
    except:
        pass