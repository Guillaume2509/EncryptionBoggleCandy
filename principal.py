# -*- coding: utf-8 -*-
"""Voici le point d'entrée principal du programme. Nous utilisons les fonctions que vous devez programmer,
il est donc normal que ce code ne fonctionne pas tant que vous n'avez pas complété ces fonctions.
Exécutez d'abord les tests unitaires du module rsa fournis pour tester la programmation de vos fonctions 
au fur et à mesure.

Auteur: (à compléter)
"""

from rsa import generer_paire_de_cles
from chiffrement_fichiers import chiffrer_fichier, dechiffrer_fichier

# Nous ajoutons ce code pour vous donner un exemple supplémentaire d'utilisation finale des fonctions du TP.
print("Génération des clés...")
cle_privee, cle_publique = generer_paire_de_cles()
print("Clé publique: ", cle_publique)
print("Clé privée: ", cle_privee)
print()

print("Chiffrement en cours...\n")
chiffrer_fichier('fichier_a_chiffrer.txt', 'fichier_version_chiffree.txt', cle_publique)

print("Déchiffrement en cours...\n")
message = dechiffrer_fichier('fichier_version_chiffree.txt', cle_privee)

print("Message déchiffré:")
print("---------------------------------------------------------------------")
print(message)
print("---------------------------------------------------------------------")

# TODO: Une fois le code ci-haut fonctionnel et que vous êtes en mesure de chiffrer et déchiffrer le message
# TODO: clair fourni avec l'énoncé (fichier_a_chiffrer.txt), supprimez le code ci-haut et écrivez le code
# TODO: nécessaire pour déchiffrer et afficher le contenu du fichier secret.txt fourni avec l'énoncé.
# TODO: Utilisez la clé publique de l'enseignant, donnée dans l'énoncé du TP.

