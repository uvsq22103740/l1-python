import tkinter as tk
racine = tk.Tk() # Création de la fenêtre racine
racine.title("affichage") # ajoute un titre
label = tk.Label(racine, text="affichage", font=("helvetica", "20")) # création du widget
label.grid() # positionnement du widget
racine.mainloop() # Lancement de la boucle principale