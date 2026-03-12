def afficher_grille(grille):
    '''
    Entrée : grille (liste 4D) représentant les 4 sous-grilles 3x3
    Sortie : aucune
    But : afficher la grille complète 6x6 avec séparations des sous-grilles
    '''
    print("┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓")

    for i in range(6):
        print("┃", end="")

        for j in range(6):

            sg_l = i // 3
            sg_c = j // 3
            l = i % 3
            c = j % 3

            valeur = grille[sg_l][sg_c][l][c]

            print(f" {valeur} ", end="")

            if j == 2:
                print("┃", end="")
            elif j < 5:
                print("│", end="")

        print("┃")

        if i == 2:
            print("┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫")
        elif i < 5:
            print("┠───┼───┼───╂───┼───┼───┨")

    print("┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛")

grille = [
    [
        [["1", " ", " "], [" ", " ", " "], [" ", " ", "1"]],
        [[" ", " ", "1"], [" ", " ", " "], [" ", " ", "1"]]
    ],
    [
        [["1", " ", " "], [" ", " ", " "], [" ", " ", " "]],
        [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    ]
]

afficher_grille(grille)