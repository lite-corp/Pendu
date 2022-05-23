from tkinter import *
from xml.etree.ElementTree import C14NWriterTarget
from PIL import *
from random import choice
from larousse_api import larousse
# INSTALL LAROUSSE_API WITH:
# pip install larousse-api-sunbro

#FONCTIONS UTILES
#Fonction qui permet de générer un mot aléatoirement
def mot_a_trouver(): 
    fichier=open("liste.txt","r")
    contenu=fichier.readlines()
    mot_secret = choice(contenu) 
    return mot_secret[:-1]

#Fonction qui permet de générer un mot difficile et aléatoirement
def mot_difficile():
    fichier2=open("motsdifficiles.txt","r")
    contenu=fichier2.readlines()
    mot_hard=choice(contenu)
    return mot_hard[:-1]

#Fonction pour choisir un mot facile ou difficile aléatoirement
def hasard():
    mot1=mot_a_trouver()
    mot2=mot_difficile()
    contenu=[mot1,mot2]
    return choice(contenu)

def mot_surprise():
    fichier2=open("prenoms.txt","r")
    contenu=fichier2.readlines()
    mot_surp=choice(contenu)
    return mot_surp[:-1]

#Fonction qui permet de générer une suite d'underscore de la taille d'un mot mis en argument
def mot_underscore(mot):
    mot_cache = ""
    for i in range(len(mot)):
        mot_cache += "_"
    return mot_cache

#Fonction qui remplace les underscore par la lettre valide
def remplace(lettre,msecret,cache):
    for i in range(len(msecret)):
        if msecret[i] == lettre:
            t = list(cache) 
            t[2*i] = lettre #pour eviter que ça remplace les espaces 
            cache = "".join(t)
    return cache

#Fonction qui vérifie si un caractère entré est une lettre ou non
def est_valide(mot):
    for c in mot:
        if not c.isalpha():
            return True
        else:
            return False

#DEFINITION DE LA CLASS JEU 
class Jeu():
    def __init__(self,mot=mot_a_trouver(),c0="clara1.gif",c1="clara1.gif",c2="clara2.gif",c3="clara3.gif",c4="clara4.gif",c5="clara5.gif",c6="clara6.gif",c7="clara7.gif",c8="clara8.gif",w1=300,h1=350,xa=152,ya=152,conditionindice="oui"):

        
        #CREATION DE LA FENETRE
        self.fenetre = Tk()
        self.fenetre.update()
        self.fenetre.title("Jeu du pendu")
        self.fenetre.configure(bg="black")
        self.fenetre.geometry("1000x1000")
        #CREATION DES WIDGETS
        #CREATION DU MOT MYSTERE
        self.mot=mot
        self.mot_cache=" ".join(mot_underscore(self.mot))
        self.mot_cache = remplace(self.mot[0], self.mot, self.mot_cache)


        #LABEL POUR AFFICHER LE MOT EN UNDERSCORE
        self.var=StringVar()
        self.var.set(self.mot_cache)
        self.affiche_mots = Label (self.fenetre,textvariable = self.var,font="Times 30",bg="black",fg="white")
        self.affiche_mots.place(x=520,y=200)

        #LABEL POUR AFFICHER DES PHRASES (pour commenter le jeu)
        self.var4=StringVar()
        self.var4.set("")
        self.affiche_phrase = Label (self.fenetre,textvariable = self.var4,font="Times 14",bg="black",fg="white")
        self.affiche_phrase.place(x=500,y=400)

        #LABEL AFFICHE COUPS (affiche le nombre de coups restants)
        self.coups=8
        self.var2=IntVar()
        self.affiche_coups = Label (self.fenetre, textvariable = self.var2, font="Times 180",bg="black",fg="white")
        self.var2.set(self.coups)
        self.affiche_coups.place(x=900,y=200)

        #LABEL INDICE 
        if conditionindice=="oui":
            self.var6=StringVar()
            self.affiche_indice = Label (self.fenetre, textvariable = self.var6, font="Times 12",bg="black",fg="white")
            self.ind=(larousse.get_definitions(self.mot))[0]
            if self.mot in self.ind:
                self.ind=self.ind.replace(self.mot,"**********")
            self.var6.set(self.ind)
            self.affiche_indice.place(x=100,y=480)
            self.affiche_indice.place_forget()

            #BOUTON INDICE
            self.bouton_indice= Button (self.fenetre, text="Indice",command=self.indice)
            self.bouton_indice.place(x=700,y=300)

        #BOUTON VALIDER
        self.bouton_valider= Button (self.fenetre, text="Valider",command=self.game)
        self.bouton_valider.place(x=550,y=350)

        #BOUTON REJOUER
        self.bouton_rejouer=Button(self.fenetre,text="Rejouer",command=self.init_welcome,padx=50,pady=10)
        self.bouton_rejouer.place(x=550,y=400)

        #CREATION DE L'ENTRY (permet à l'utilisateur d'entrer des caractères)
        self.entree1 = Entry (self.fenetre)
        self.entree1.place(x=500,y=300)
        self.entree1.bind("<Return>",self.game)
        
        #CREATION D'UN CANVAS
        self.canvas = Canvas(self.fenetre,width=w1,height=h1,bg="black")
        self.canvas.place(x=100,y=150)
        self.photo=PhotoImage(file=c0)
        self.photo1 = PhotoImage(file=c1)
        self.photo2 = PhotoImage(file=c2)
        self.photo3 = PhotoImage(file=c3)
        self.photo4 = PhotoImage(file=c4)
        self.photo5 = PhotoImage(file=c5)
        self.photo6 = PhotoImage(file=c6)
        self.photo7 = PhotoImage(file=c7)
        self.photo8 = PhotoImage(file=c8)
        self.i=0
        self.liste_ph=[self.photo,self.photo1,self.photo2,self.photo3,self.photo4,self.photo5,self.photo6,self.photo7,self.photo8]
        self.pic=self.canvas.create_image(xa, ya, image=self.liste_ph[0])

        #CREATION D'UNE LISTE (permet de contenir les lettres déjà utilisées)
        self.lettres_utilisees=[]

        self.init_welcome()
        self.fenetre.mainloop()
    

    def init_widgets(self,mot,c0="clara0.gif",c1="clara1.gif",c2="clara2.gif",c3="clara3.gif",c4="clara4.gif",c5="clara5.gif",c6="clara6.gif",c7="clara7.gif",c8="clara8.gif",w1=300,h1=350,xa=152,ya=152,conditionindice="oui"):
        #CACHER LES WIDGETS DE LA PAGE WELCOME:
        self.bouton_difficile.place_forget()
        self.bouton_facile.place_forget()
        self.welcome.place_forget()
        self.bouton_aleatoire.place_forget()
        self.bouton_surprise.place_forget()

        #CREATION DU MOT
        self.mot=mot
        self.mot_cache=" ".join(mot_underscore(self.mot))
        self.mot_cache = remplace(self.mot[0], self.mot, self.mot_cache)

        #LABEL POUR AFFICHER LE MOT EN UNDERSCORE
        self.var=StringVar()
        self.var.set(self.mot_cache)
        self.affiche_mots = Label (self.fenetre,textvariable = self.var,font="Times 30",bg="black",fg="white")
        self.affiche_mots.place(x=520,y=200)

        #LABEL AFFICHE PHRASE (pour commenter le jeu)
        self.var4=StringVar()
        self.var4.set("")
        self.affiche_phrase = Label (self.fenetre,textvariable = self.var4,font="Times 14",bg="black",fg="white")
        self.affiche_phrase.place(x=550,y=400)

        #LABEL AFFICHE COUPS (affiche le nombre de coups restants)
        self.coups=8
        self.var2=IntVar()
        self.affiche_coups = Label (self.fenetre, textvariable = self.var2, font="Times 180",bg="black",fg="white")
        self.var2.set(self.coups)
        self.affiche_coups.place(x=1000,y=200)

        #LABEL INDICE
        if conditionindice=="oui":
            self.var6=StringVar()
            self.affiche_indice = Label (self.fenetre, textvariable = self.var6, font="Times 12",bg="black",fg="white")
            self.ind=(larousse.get_definitions(self.mot))[0]
            if self.mot in self.ind:
                self.ind=self.ind.replace(self.mot,"**********")
            self.var6.set(self.ind)
            self.affiche_indice.place(x=100,y=480)
            self.affiche_indice.place_forget()

            #BOUTON INDICE
            self.bouton_indice= Button (self.fenetre, text="Indice",command=self.indice)
            self.bouton_indice.place(x=700,y=300)

        #BOUTON VALIDER
        self.bouton_valider= Button (self.fenetre, text="Valider",command=self.game)#probleme, il marche plus 
        self.bouton_valider.place(x=550,y=350)

        #CREATION DE L'ENTRY (permet à l'utilisateur d'entrer des caractères)
        self.entree1 = Entry (self.fenetre)
        self.entree1.place(x=550,y=300)
        self.entree1.bind("<Return>",self.game)

        #CREATION D'UN CANVAS
        self.canvas = Canvas(self.fenetre,width=w1,height=h1,bg="black")
        self.canvas.place(x=100,y=150)
        self.photo=PhotoImage(file=c0)
        self.photo1 = PhotoImage(file=c1)
        self.photo2 = PhotoImage(file=c2)
        self.photo3 = PhotoImage(file=c3)
        self.photo4 = PhotoImage(file=c4)
        self.photo5 = PhotoImage(file=c5)
        self.photo6 = PhotoImage(file=c6)
        self.photo7 = PhotoImage(file=c7)
        self.photo8 = PhotoImage(file=c8)
        self.i=0
        self.liste_ph=[self.photo,self.photo1,self.photo2,self.photo3,self.photo4,self.photo5,self.photo6,self.photo7,self.photo8]
        self.pic=self.canvas.create_image(xa, ya, image=self.liste_ph[0])

        #CREATION D'UNE LISTE (permet de contenir les lettres déjà utilisées)
        self.lettres_utilisees=[]

    #Fonction qui reliée au bouton indice, permet d'afficher le label indice
    def indice(self):
        self.affiche_indice.place(x=50,y=540)

    #Fonction pour générer une page de bienvenue
    def init_welcome(self):
        
        #CACHER LES WIDGETS
        self.bouton_rejouer.place_forget()
        self.affiche_coups.place_forget()
        self.affiche_mots.place_forget()
        self.affiche_phrase.place_forget()
        self.bouton_valider.place_forget()
        self.entree1.place_forget()
        self.canvas.place_forget()
        self.bouton_indice.place_forget()
        self.affiche_indice.place_forget()
        self.fenetre.configure(bg="black")
        

        #LABEL DE BIENVENUE
        self.var0=StringVar()
        self.welcome = Label (self.fenetre,textvariable = self.var0,font="Times 30",bg="black",fg="white")
        self.var0.set("Bienvenue dans le jeu du pendu !\nVeuillez choisir votre mode de jeu.")
        self.welcome.place(x=380,y=150)

        #BOUTON FACILE
        self.bouton_facile= Button (self.fenetre, text="Facile",font="Times",command=lambda:self.init_widgets(mot_a_trouver()),padx=20,pady=20,bg="lightgreen")
        self.bouton_facile.place(x=420,y=400)

        #BOUTON DIFFICILE
        self.bouton_difficile= Button (self.fenetre, text="Difficile",font="Times",command=lambda:self.init_widgets(mot_difficile()),padx=20,pady=20,bg="lightpink")
        self.bouton_difficile.place(x=620,y=400)

        #BOUTON ALEATOIRE
        self.bouton_aleatoire= Button (self.fenetre, text="Aléatoire",font="Times",command=lambda:self.init_widgets(hasard()),padx=20,pady=20,bg="lightblue")
        self.bouton_aleatoire.place(x=820,y=400)

        #BOUTON SURPRISE
        self.bouton_surprise=Button(self.fenetre,text="❕",font="Times",command=lambda:self.init_widgets(mot_surprise(),"nsi0.gif","nsi1.gif","nsi2.gif","nsi3.gif","nsi4.gif","nsi5.gif","nsi6.gif","nsi7.gif","nsi8.gif",350,240,300,100,"non"),padx=10,pady=10,bg="black") #300 s'applique qu'a une seule pht
        self.bouton_surprise.place(x=1000,y=40)
    
    #Fonction principale du jeu
    def game(self,event=None):#event pour pouvoir executer "self.entree1.bind("<Return>",self.game)" sans problème

        #PHRASES POUR LES COMMENTAIRES
        phrase0="Raté! Il vous reste "+str(self.coups-1)+" coup(s)"
        phrase1="Dommage...Le mot était "+str(self.mot)
        phrase2="Bravo! Le mot était bien "+str(self.mot)
        phrase3="Lettre déjà utilisée.⚠️"
        phrase4="Le caractère entré n'est pas valide.⚠️"
        phrase5="Bien vu!"
        phrase6="BRAVO!!!"

        lettre=self.entree1.get()
        self.entree1.delete(0, END)
        # if self.mot in self.var6:
        #   self.var6.set(self.var6-self.mot)

        if len(lettre)>1 or est_valide(lettre):
            self.var4.set(phrase4)
            if lettre==self.mot:
                self.var.set(" ".join(self.mot))
                self.bouton_rejouer.place(x=500,y=450)
                self.var4.set(phrase6)
        elif "_" in self.mot_cache:
            if self.coups>0:
                    if lettre in self.mot:
                        if lettre in self.lettres_utilisees:
                            self.var4.set(phrase3)
                        else:
                            self.mot_cache=remplace(lettre,self.mot,self.mot_cache)
                            self.var.set(self.mot_cache)
                            self.var4.set(phrase5)
                            self.lettres_utilisees.append(lettre)#utiliser time
                        if "_" not in self.mot_cache:
                            self.var4.set(phrase2)
                            self.bouton_rejouer.place(x=500,y=450)
                    else :
                        if lettre in self.lettres_utilisees:
                            self.var4.set(phrase3)
                        else:   
                            self.coups -= 1
                            if self.coups==0:
                                self.pic=self.canvas.create_image(175, 140, image=self.liste_ph[8])
                                self.var2.set(self.coups)
                                self.var4.set(phrase1)
                                self.bouton_rejouer.place(x=500,y=450)
                            else:
                                self.var2.set(self.coups)
                                self.i+=1
                                self.pic=self.canvas.create_image(152, 152, image=self.liste_ph[self.i])
                                self.canvas.place(x=100,y=150)
                                self.var4.set(phrase0)
                                self.lettres_utilisees.append(lettre)  
        

Jeu()



