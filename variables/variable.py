# Les types de données et les variables en Python 
# Il existe plusieurs types de données en python : 

"""
  Les types de données et les variables en Python.
  Il existe plusieurs types de données en python : 
  1. Integer (int) : Nombres entiers positifs ou négatifs.
  2. Float (float) : Nombres décimaux.
  3. String (str) : Chaînes de caractères.
  4. Boolean (bool) : Vrai ou faux.
  5. List (list) : Une collection ordonnée de données.
  6. Tuple (tuple) : Une collection ordonnée de données immuable.
  7. Dictionary (dict) : Un ensemble de paires clé-valeur.
  8. Set (set) : Une collection non ordonnée sans doublon.
  9. Fonction (function) : Un ensemble d'instructions (n'est pas un type de donnée en soi).
  10. Module (module) : Fichier contenant du code Python réutilisable (n'est pas un type de donnée en soi).
  11. Classe (class) : Modèle pour créer des objets avec des propriétés et des méthodes (n'est pas un type de donnée en soi).

"""
import copy
from itertools import product
# Déclaration et affectation de variables
# en python les variables sont automatiquement typées c'est à dire que vous n'avez plus besoin de préciser les types de variables.

nom =  "John"  
age = 30
citation = " Tout le monde devrait apprendre à programmer un ordinateur, car cela vous apprend à penser " # cette sitation vient de steve Jobs
moyenne_scolaire = 16.5 
est_en_promotion = True  # Cette variable est de type booléen
noms_des_etudiants = [ "Jean", "Paul", "Pierre", "Caroline", "Diane"]
informations_des_etudiants = {    }

print(noms_des_etudiants[2:])