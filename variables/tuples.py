# Un tuple est une liste qui ne peut être modifiée.

# Création d'un tuple
# syntaxe : nom_de_tuple = ()

niveau_de_jeux = ()

#Ajout d'une valeur à un tuple

niveau_de_jeux = ("facile" , "intermediare", "avancée", "Professionnel") # Vous pouvez mélanger les types lors de la création de votre tuple

niveau_de_jeux[0]= 2 # La modification d'un tuple entrainera une erreur : TypeError ; 'tuple' object doe s not support item assignment

# Notez bien : La création d'un tuple avec une valeur doit avoir une virgule à la fin sion cette variable sera considérée comme un string et non un tuple.


nom_de_tuple  = ("Jean")

print(type(nom_de_tuple)) # cette varible est de type string 

nom_de_tuple = ("Jean",)
print(type(nom_de_tuple)) # cette varible est de type tuple


