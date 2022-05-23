from random import *

#Fonction pour générer des mots aléatoirement
def mot_a_trouver(): 
    fichier=open("liste.txt","r")
    contenu=fichier.readlines()
    mot_secret = choice(contenu) 
    return mot_secret[:-1]

#Fonction pour générer le mot mystère et formé par des underscore
def mot_underscore(mot):
    mot_cache = ""
    for i in range(len(mot)):
        mot_cache += "_"
    return mot_cache

#Fonction pour remplacer les lettres du mot caché par les bonnes lettres 
def remplace(lettre,mot_secret,mot_cache):
    for i in range(len(mot_secret)):
        if mot_secret[i] == lettre:
            t = list(mot_cache) 
            t[2*i] = lettre 
            mot_cache = "".join(t)
    return mot_cache

#Fonction pour vérifier que le caractère entré par l'utilisateur est une lettre 
def est_valide(mot):
    for c in mot:
        if not c.isalpha():
            return True
        else:
            return False
  
#Fonction pour permettre à l'utilisateur de rentrer une lettre 
def lettre_a_saisir():
    lettre=input("Veuillez entrer une lettre: ").lower()
    if len(lettre)>1 or est_valide(lettre):
        print("Le caractère entré n'est pas valide. ")
        return lettre_a_saisir()
    else:

        return lettre

#Fonction qui programme le jeu
def play():
    nb_essais= 8
    mot_secret=mot_a_trouver()
    lettres_utilisees=[mot_secret[0]]
    mot_cache=" ".join(mot_underscore(mot_secret))
    mot_cache = remplace(mot_secret[0],mot_secret,mot_cache)
    while nb_essais>0:
        print(mot_cache)
        print("\n══════════════════════════════════════════════════════════════════════════════════════════════")
        lettre = lettre_a_saisir()
        if lettre in mot_secret:
            if lettre in lettres_utilisees:
                print("\nLettre déjà utilisée. ⚠️")
            else: 
                mot_cache = remplace(lettre, mot_secret, mot_cache)
                lettres_utilisees.append(lettre)
                if "_" not in mot_cache:
                    print(mot_cache)
                    print("\n\n- - - - - - - - - - - - - - - -\n")
                    print("\nBravo, vous avez gagné !\nLe mot secret était bien",mot_secret,"\n")
                    print("- - - - - - - - - - - - - - -\n")
                    print("\n                                                     ◄  FIN DE LA PARTIE  ►\n")
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    break
        else:
            if lettre in lettres_utilisees:
                print("\nLettre déjà utilisée. ⚠️")
            else:
                nb_essais -= 1
                print("\nPas de chance! Il vous reste",nb_essais,"essais.\n")
                lettres_utilisees.append(lettre)
    
    if nb_essais == 0:
        if "_" in mot_cache:
            print("\n\n- - - - - - - - - - - - - - - -\n")
            print("\nAïe....c'est perdu...! :(")
            print("Le mot secret était :",mot_secret,"\n")
            print("- - - - - - - - - - - - - - - -\n")
            print("\n                                                      ◄  FIN DE LA PARTIE  ►\n")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

#Fonction qui permet à l'utilisateur de choisir de rejouer ou non
def again():
    question=str(input("Voulez vous rejouer?\n").lower())
    if question=="non":
        print("\nOk, à la prochaine!")
    elif question=="oui":
        main()
    else:
        again()

#Fonction principale qui permet de lancer le jeu
def main():
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("\n                                        ☆ - ☆ - ☆  BIENVENUE DANS LE JEU DU PENDU  ☆ - ☆ - ☆ \n")
    print("                                  Tu disposes de 8 essais pour trouver le mot mystère, bon courage! :)\n")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("\n                                                         ◄  DEBUT DE LA PARTIE  ►\n")
    play()
    again()

main()
