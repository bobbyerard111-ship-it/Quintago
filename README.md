# README — Quintago
 
## Auteurs
 
- [Prénom1 NOM1]
- [Prénom2 NOM2]
 
---
 
## Nom du projet
 
**Quintago** — adaptation du jeu de société Pentago©
 
---
 
## Date et version
 
- Date : 2025–2026
- Version : 1.0
 
---
 
## Langage utilisé
 
Python 3.6 et versions ultérieures
 
---
 
## Fichier principal à exécuter
 
```
python quintago.py
```
 
---
 
## Description du menu d'accueil
 
Au lancement du programme :
 
1. Si un fichier de sauvegarde `partie_en_cours.txt` est détecté, le programme propose de reprendre la partie en cours (saisir `o` pour oui, `n` pour non).
2. Si aucune sauvegarde n'existe (ou si le joueur refuse de reprendre), une nouvelle partie est lancée.
3. Les deux joueurs saisissent leur prénom.
4. La partie commence : les joueurs jouent chacun leur tour jusqu'à la victoire de l'un d'eux, une double victoire simultanée, ou un match nul (grille pleine).
 
---
 
## Arborescence du projet
 
```
quintago/
│
├── quintago.py          # Fichier principal — lancement du jeu
├── parametres.py        # Constantes et paramètres du jeu
├── initialisation.py    # Création de la grille initiale
├── affichage.py         # Affichage de la grille dans le terminal
├── saisie.py            # Fonctions de saisie sécurisée au clavier
├── tests_alignements.py # Détection des alignements et victoires
├── tour_de_jeu.py       # Déroulement d'un tour (case + rotation)
├── sauvegarde.py        # Sauvegarde et chargement d'une partie
└── README.md            # Ce fichier
```
 
---
 
## Liste et rôles des paramètres (`parametres.py`)
 
| Paramètre            | Valeur       | Rôle                                                   |
|----------------------|--------------|--------------------------------------------------------|
| `NOM_FICHIER`        | `'partie_en_cours.txt'` | Nom du fichier de sauvegarde              |
| `ALIGNEMENT`         | `5`          | Nombre de pions alignés pour gagner                    |
| `NB_SG`              | `2`          | Nombre de sous-grilles par côté (2×2 sous-grilles)     |
| `TAILLE_SG`          | `3`          | Taille d'une sous-grille (3×3)                         |
| `TAILLE`             | `6`          | Taille totale de la grille (`NB_SG × TAILLE_SG`)       |
| `JETON_BLANC`        | `'●'` (blanc)| Symbole du joueur 1 (affiché en blanc dans le terminal)|
| `JETON_NOIR`         | `'●'` (gris) | Symbole du joueur 2 (affiché en gris dans le terminal) |
| `VALEURS_A_AFFICHER` | dictionnaire | Association valeur → symbole affiché (`0`, `1`, `2`)   |
 
---
 
## Liste des fichiers / modules implantés
 
| Fichier                | Contenu principal                                                              |
|------------------------|--------------------------------------------------------------------------------|
| `quintago.py`          | Fonction `jouer()` — boucle principale de jeu ; point d'entrée du programme   |
| `parametres.py`        | Toutes les constantes du jeu                                                   |
| `initialisation.py`    | Fonction `initialisation_grille()` — création d'une grille vide 4D            |
| `affichage.py`         | Procédure `afficher_grille()` — affichage formaté dans le terminal             |
| `saisie.py`            | Fonctions de saisie protégée (entiers, coordonnées, sens de rotation)          |
| `tests_alignements.py` | `grille_plate()`, `cinq_alignes()`, `alignement_horizontal()`, `alignement_vertical()`, `alignement_diagonal()`, `test_victoire()` |
| `tour_de_jeu.py`       | `jouer_case()`, `rotation_droite()`, `rotation_gauche()`, `jouer_tour()`      |
| `sauvegarde.py`        | `sauvegarder_grille()`, `charger_grille()`, `supprimer_sauvegarde()`          |
 
---
 
## Modules Python utilisés
 
Aucun module externe n'est nécessaire. Le projet utilise uniquement la bibliothèque standard Python :
 
- `os` (dans `sauvegarde.py` pour la gestion de fichiers)
 
---
 
## Règles du jeu
 
La grille est un tableau 6×6 divisé en quatre sous-grilles 3×3. À chaque tour, le joueur :
 
1. **Place un pion** sur une case libre de son choix.
2. **Effectue une rotation** d'un quart de tour (gauche ou droite) sur l'une des quatre sous-grilles.
 
Le premier joueur à aligner **5 pions** horizontalement, verticalement ou en diagonale remporte la partie. En cas d'alignement simultané des deux joueurs, ou de grille pleine sans alignement, la partie est déclarée nulle.