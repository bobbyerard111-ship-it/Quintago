from initialisation import *
from tour_de_jeu import *
from parametres import *
from affichage import *
from tests_alignements import *
from sauvegarde import *


def jouer(grille, joueur1='', joueur2=''):
   if joueur1 == '' and joueur2 == '':
      joueur1 = input("Veuillez saisir le nom du premier joueur : ") 
      joueur2 = input("Veuillez saisir le nom du second joueur : ") 
   print(joueur1, joueur2, "bienvenue au Quintago !")
   afficher_grille(grille)
   
   nombre_tours = 0 
   while test_victoire(grille) == 0 and nombre_tours < 36:  # tant qu'il n'y a pas de gagnant ou que la limite de tours n'est pas atteinte c'est à dire que toutes les cases de la grille ont été joués 
      print("A votre tour,", joueur1) 
      jouer_tour(grille, 1)         # séquence d'un tour de jeu 
      afficher_grille(grille) 
      nombre_tours += 1    
      sauvegarder_grille(grille, 2, joueur1, joueur2)

      print("A votre tour,", joueur2) 
      jouer_tour(grille, 2)
      afficher_grille(grille) 
      nombre_tours += 1 
      sauvegarder_grille(grille, 1, joueur1, joueur2)
   
   gagnant = test_victoire(grille) 
   if gagnant == 0:               # on dissocie les cas pour après exécuter un print en fonction du cas
      print("Egalité. Aucun joueur est victorieux.") 
   
   elif gagnant == -1: 
      print("Félicitations", joueur1, "et", joueur2, ", vous avez tous les deux gagné")   
    
   else: 
      if gagnant == 1:
         print("Bravo,", joueur1, "vous avez gagné(e)")       
      else:          
         print("Bravo,", joueur2, "vous avez gagné(e)")
   
   supprimer_sauvegarde()

if __name__ == "__main__":
   resultat = charger_grille()
   if resultat is not None:
      choix = input("Une partie sauvegardée existe. Voulez-vous la reprendre ? (o/n) : ")
      if choix == "o" or choix == "O":
         grille, nb_joueur, joueur1, joueur2 = resultat
         jouer(grille, joueur1, joueur2)
      else:
         grille = initialisation_grille()
         jouer(grille)
   else:
      grille = initialisation_grille()
      jouer(grille)