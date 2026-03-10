def afficher_grille(grille):
    '''
    Entrée : Liste de liste grille qui recense les pionts des deux joueurs
    Sortié : Pas de sortie
    But : Afficher la grille avec des traits plutôt que des affichages de listes bruts
    '''
    print("┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓")

    for i in range(6):
        print("┃", end="")

        for j in range(6):
            print(f" {grille[i][j]} ", end="")

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
    ["X", " ", "O", " ", "X", " "],
    [" ", "X", " ", " ", " ", "O"],
    ["O", " ", " ", "X", " ", " "],
    [" ", " ", "X", " ", "O", " "],
    [" ", "O", " ", " ", " ", "X"],
    ["X", " ", " ", "O", " ", " "]
]
afficher_grille(grille)