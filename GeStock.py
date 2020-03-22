from tkinter import *

class GeStock():

    def __init__(self):
        self.root=Tk()
        self.root.title("GeStock")
        self.root.minsize(640,480)
        self.root.geometry("800x600")

        self.FrameAccueil()

        self.root.mainloop()

    def FrameAccueil(self):     #Page d'accueil

        self.frame_acc = Frame(self.root, relief="groove", bd=2, height=600, width=500)
        self.frame_acc.pack()

        self.label_acc = Label(self.frame_acc, text="Bienvenue sur GeStock !")
        self.label_acc.pack()

        #Bouton qui envoie sur le frame Connex
        self.button_connex = Button(self.frame_acc, text="Connexion", command=self.FrameConnex)
        self.button_connex.pack()

        #Bouton qui envoie sur le frame Inscription
        self.button_inscri = Button(self.frame_acc, text="Inscription", command=self.FrameInscription)
        self.button_inscri.pack()

        self.button_quit = Button(self.frame_acc, text="Quitter", command=quit)
        self.button_quit.pack()
        

    def FrameConnex(self):      #Frame de connexion remplaçant celui de l'accueil
        self.frame_acc.pack_forget()    #Cache le frame d'accueil

        self.frame_connex = Frame(self.root)
        self.frame_connex.pack()

        self.label_user = Label(self.frame_connex, text="Nom d'utilisateur :")
        self.label_user.pack()

        self.entry_user = Entry(self.frame_connex)
        self.entry_user.pack()

        self.label_password = Label(self.frame_connex, text="Mot de passe :")
        self.label_password.pack()

        self.entry_password = Entry(self.frame_connex, show="*")
        self.entry_password.pack()

        self.button_connex = Button(self.frame_connex, text="Connexion", command=self.FrameMenu)
        self.button_connex.pack()

        self.button_annuler = Button(self.frame_connex, text="Annuler", command=self.AnnulerConnex)
        self.button_annuler.pack()

    def AnnulerConnex(self):      # Optimisation du bouton annuler
        self.frame_connex.pack_forget()     #Cache le frame de connexion
        self.FrameAccueil()     #Renvoie au frame d'accueil

    def FrameInscription(self):
        self.frame_acc.pack_forget()    #Cache le frame d'accueil

        self.frame_inscri = Frame(self.root)
        self.frame_inscri.pack()

        self.label_name=Label(self.frame_inscri, text="Nom : ")
        self.label_name.pack()

        self.entry_name=Entry(self.frame_inscri)
        self.entry_name.pack()

        self.label_username=Label(self.frame_inscri, text="Nom d'utilisateur : ")
        self.label_username.pack()

        self.entry_username=Entry(self.frame_inscri)
        self.entry_username.pack()

        self.label_newPW=Label(self.frame_inscri, text="Mot de passe : ")
        self.label_newPW.pack()

        self.entry_newPW=Entry(self.frame_inscri, show="*")
        self.entry_newPW.pack()

        self.label_confirmPW=Label(self.frame_inscri, text="Confirmez votre mot de passe : ")
        self.label_confirmPW.pack()

        self.entry_confirmPW=Entry(self.frame_inscri, show="*")
        self.entry_confirmPW.pack()

        self.button_valider=Button(self.frame_inscri, text="Valider")
        self.button_valider.pack()

        self.button_annuler=Button(self.frame_inscri, text="Annuler", command=self.AnnulerInscription)
        self.button_annuler.pack()

    def AnnulerInscription(self):
        self.frame_inscri.pack_forget()
        self.FrameAccueil()

    def FrameMenu(self):
        self.frame_connex.pack_forget()

        self.frame_menu=Frame(self.root)
        self.frame_menu.pack()

        self.button_ajoutProduit=Button(self.frame_menu, text="Ajouter un nouveau produit")
        self.button_ajoutProduit.pack()

        self.button_modifStock=Button(self.frame_menu, text="Modifier le stock")
        self.button_modifStock.pack()

        self.button_affichageStock=Button(self.frame_menu, text="Afficher le stock complet")
        self.button_affichageStock.pack()

        self.button_deconnex=Button(self.frame_menu, text="Se déconnecter", command=self.Deconnex)
        self.button_deconnex.pack()

        self.button_quitter=Button(self.frame_menu, text="Quitter le logiciel", command=quit)
        self.button_quitter.pack()

    def Deconnex(self):
        self.frame_menu.pack_forget()
        self.FrameAccueil()



essai = GeStock()