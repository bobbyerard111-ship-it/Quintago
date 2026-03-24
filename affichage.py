from parametres import *

def afficher_grille(grille):
    '''
    Affiche une grille de quintago avec des jetons blancs et gris

    Paramètre : grille (list) : grille quintago 4D

    Sortie : None
    '''
    print("  ┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓")

    for i in range(6):
        print(str(i+1) + " ┃", end="")

        for j in range(6):
            sg_l = i // 3
            sg_c = j // 3
            l = i % 3
            c = j % 3

            valeur = grille[sg_l][sg_c][l][c]
            print(f" {VALEURS_A_AFFICHER[valeur]} ", end="")

            if j == 2:
                print("┃", end="")
            elif j < 5:
                print("│", end="")

        print("┃")

        if i == 2:
            print("  ┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫")
        elif i < 5:
            print("  ┠───┼───┼───╂───┼───┼───┨")

    print("  ┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛")
    print("    1   2   3   4   5   6  ")