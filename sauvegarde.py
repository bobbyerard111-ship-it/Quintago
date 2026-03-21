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

    with open(NOM_FICHIER, "w") as fichier:
        fichier.write("joueur:" + str(nb_joueur) + "\n")
        for i in range(NB_SG):
            for j in range(NB_SG):
                #Identification de la sous-grille (sg:I:J)
                fichier.write("sg:" + str(i) + ":" + str(j) + "\n")
                #Valeurs case par case en sautant des lignes
                for l in range(TAILLE_SG):
                    for c in range(TAILLE_SG):
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
            lignes = []
            for ligne in fichier: # car chaque élément est une ligne avec le "\n" à la fin
                lignes.append(ligne)
            
            # Pour restituer les informations correctement, il faut retier le "\n" à la fin de chaque ligne avec un slice[:-1]
            # (la dernière ligne peut ne pas en avoir d'où la vérification)
            for i in range(len(lignes)):
                if len(lignes[i]) > 0 and lignes[i][-1] == "\n":
                    lignes[i]  = lignes[i][:-1]
            
            nb_joueur = int(lignes[0][7]) # Format attendu "joueur:X"  ; Le chiffre est donc toujours à l'indice 7

            #Initialisation d'une grille vide

            grille = [[[[0] * TAILLE_SG for _ in range(TAILLE_SG)] for _ in range(NB_SG)] for _ in range(NB_SG)]

            # Remplissage de la grille
            # On parcourt les lignes à partir de la ligne 1 (on saute "joueur:X")
            # lignes[0:2] == "sg" pour détecter en-tête
            # ligne[3] == I (indice de ligne de la sous-grille)
            # ligne[5] == J (indice de colonne de la sous-grille)
            num_ligne = 1
            while num_ligne < len(lignes):
                ligne = lignes[num_ligne]
                
                if ligne[0:2] == "sg":
                    #lecture des indices directement par position
                    i = int(ligne[3])
                    j = int(ligne[5])
                    num_ligne += 1

                    for l in range(TAILLE_SG):
                        for c in range(TAILLE_SG):
                            grille[i][j][l][c] = int(lignes[num_ligne])
                            num_ligne +=1
                else:
                    #ligne inattendue : on l'ignore
                    num_ligne += 1
        
        print("Partie chargée depuis '" + NOM_FICHIER + "'. C'est au joueur " + str(nb_joueur) + " de jouer.")

        return grille, nb_joueur

    except FileNotFoundError:
        print("Aucune partie sauvegardée trouvée (fichier '" + NOM_FICHIER + "' est introuvable")
        return None
    
    except (ValueError, IndexError) as erreur:
        print("Erreur lors du chargement : fichier invalide. (" + str(erreur) + ")")
        return None
