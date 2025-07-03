from fpdf import FPDF
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import os

########################## Logiciel ############################################################

# Fonctions de calcul
def prevision(n, prix, croissance):
    F = []
    for j in range(len(prix)):
        f = 0
        for i in range(1, n + 1):
            f += prix[j] * (croissance[j] ** i)
        F.append(round(f, 2))
    return F

def total_avec_interets(n, prix, croissance):
    return round(sum(prevision(n, prix, croissance)), 2)

def total_sans_interet(n, prix):
    return round(sum(prix) * n, 2)

def croissance_portefeuille(n, prix, croissance):
    return round(((total_avec_interets(n, prix, croissance) / total_sans_interet(n, prix)) - 1) * 100, 2)

# Fonction pour valider et afficher les résultats dans un tableau
def afficher_resultats():
    try:
        # Récupération des valeurs saisies
        global T 
        T = int(entry_T.get())
        prix = list(map(float, entry_prix.get().split()))
        croissance = list(map(float, entry_croissance.get().split()))

        # Vérification des longueurs = 1e gestion + affichage erreur
        if len(prix) != len(croissance):
            messagebox.showerror("Erreur", "Les listes des montants et des croissances doivent être de la même longueur.")
            return

        # Calcul des résultats
        global croissance_val
        global total_int
        global total_sans_int
        croissance_val = croissance_portefeuille(T, prix, croissance)
        total_int = total_avec_interets(T, prix, croissance)
        total_sans_int = total_sans_interet(T, prix)

        # Effacer les résultats précédents
        for widget in result_frame.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()

        # Afficher les résultats dans un tableau
        headers = ["Statistique", "Valeur"]
        stats = [
            ("Croissance du portefeuille (%)", f"{croissance_val:.2f} %"),
            (f"Total avec intérêts après {T} ans", f"{total_int:.2f}"),
            (f"Total sans intérêts après {T} ans", f"{total_sans_int:.2f}")
        ]

        for i, header in enumerate(headers):
            tk.Label(result_frame, text=header, font=("Arial", 10, "bold")).grid(row=0, column=i, padx=5, pady=5)

        for i, (label, value) in enumerate(stats, start=1):
            tk.Label(result_frame, text=label).grid(row=i, column=0, padx=5, pady=5)
            tk.Label(result_frame, text=value).grid(row=i, column=1, padx=5, pady=5)

    except ValueError:  # 2e gestion + affichage erreur
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides pour toutes les entrées.")

# Code pour gérer affichage et organisation de la fenêtre
root = ttkb.Window(themename="superhero")
root.title("Calculateur de Croissance de Portefeuille")

# Question 1 : Nombre d'années
tk.Label(root, text="Sur combien d'années souhaitez-vous prévoir le rendement ?").pack()
entry_T = tk.Entry(root)
entry_T.pack()

# Question 2 : Liste des montants
tk.Label(root, text="Liste des montants investis dans les actifs par an (séparés par des espaces)").pack()
entry_prix = tk.Entry(root)
entry_prix.pack()

# Question 3 : Liste des croissances annuelles
tk.Label(root, text="Liste des croissances annuelles + 1 des actifs (séparés par des espaces)").pack()
entry_croissance = tk.Entry(root)
entry_croissance.pack()

# Bouton pour valider et afficher les résultats
btn_valider = tk.Button(root, text="Valider", command=afficher_resultats)
btn_valider.pack(pady=10)

############################### PDF ###########################################""

class OfficialPDF(FPDF):
    def header(self):
        # Drapeau français
        self.set_fill_color(0, 0, 255)  # Bleu
        self.rect(10, 10, 10, 20, 'F')
        self.set_fill_color(255, 255, 255)  # Blanc
        self.rect(20, 10, 10, 20, 'F')
        self.set_fill_color(255, 0, 0)  # Rouge
        self.rect(30, 10, 10, 20, 'F')
        
        # Date en haut à droite
        self.set_y(10)
        self.set_x(-50)
        self.set_font('Arial','', 12)
        date_str = datetime.now().strftime('%d/%m/%Y')
        self.cell(40, 10, f'Date : {date_str}', 0, 0, 'R')

    def footer(self):
        # Signature officielle (bas gauche)
        self.set_y(-35)
        self.set_font('Arial', 'B', 10)
        self.set_x(10)
        self.cell(0, 10, 'Signature officielle :', 0, 1, 'L')
        self.image('c:\\Dossier Perso\\Code informatique\\programme python\\Logiciels\\logiciel portefeuille pdf\\RF.png', 
               x=10, y=self.get_y() + 5, w=35)

        # Signature (bas droite)
        self.set_y(-30)
        self.set_x(-70)
        self.cell(-10, 10, 'Signature :', 0, 1, 'R')
        self.set_x(-70)
        self.line(self.get_x(), self.get_y() + 5, self.get_x() + 50, self.get_y() + 5)
    
    
    def add_content(self, croissance_val, total_int, total_sans_int, T):
        # Afficher les résultats dans un tableau
        long_text = (
            "Voici les résultats financiers concernant la croissance de votre portefeuille : "
        )
        self.set_font("Arial", size=12)
        self.multi_cell(0, 10, long_text, align='L')
        self.ln(5)

        # Définir les entêtes du tableau
        headers = ["Statistique", "Valeur"]
        stats = [
            ("Croissance du portefeuille (%)", f"{croissance_val:.2f} %"),
            (f"Total avec intérêts après {T} ans", f"{total_int:.2f}"),
            (f"Total sans intérêts après {T} ans", f"{total_sans_int:.2f}")
        ]

        # Afficher les entêtes du tableau
        self.set_font("Arial", "B", 12)
        col_widths = [90, 100]  # Largeur des colonnes
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align='C')
        self.ln()

        # Afficher les lignes de données
        self.set_font("Arial", size=12)
        for stat in stats:
            self.cell(col_widths[0], 10, stat[0], border=1, align='L')
            self.cell(col_widths[1], 10, stat[1], border=1, align='L')
            self.ln()

        # Calcul des 2/3 de la largeur de la page
        page_width = self.w  # Largeur totale de la page
        margin = self.l_margin  # Marge gauche
        x_start = margin  # La ligne commence à la marge gauche
        x_end = x_start + (page_width * 2 / 3)  # 2/3 de la largeur de la page

        # Tracer une ligne horizontale sous le tableau
        self.ln(5)  # Un petit espace pour ne pas toucher le texte
        
        
    def corp_sup(self):
        # Fonction pour ajouter le titre "Compte rendus" et le texte
        self.set_font("Arial", 'B', size=12)
        # Ajouter le titre "Compte rendus"
        self.cell(-180, 50, "Compte rendus", ln=True, align='C')  # Utilisation de 0 pour la largeur maximale
        self.ln(5)  # Ajouter un petit espace après le titre
        
        # Ajouter un paragraphe long
        long_text = (
            "Ceci est un document officiel généré par ce logiciel. Il contient les résultats "
            "de votre étude. Ce document fournit un aperçu des performances et des analyses "
            "qui ont été effectuées au sujet de la croissance du portefeuille et des diverses simulations."
        )
        self.set_font("Arial", size=12)
        self.multi_cell(0, 10, long_text, align='L')  # Texte justifié à gauche
        self.ln(5) 
    
# Créer un PDF et afficher
def afficher_pdf():
    # Créer un PDF
    pdf = OfficialPDF()
    pdf.add_page()
    pdf.corp_sup()
    pdf.add_content(croissance_val, total_int, total_sans_int, T)
    output_pdf_path = "Compte_rendus_étude.pdf"  # Vous pouvez changer cette ligne pour demander un fichier spécifique
    pdf.output(output_pdf_path)
    
    # Ouvrir le PDF
    os.startfile(output_pdf_path)

# Bouton pour afficher le PDF
btn_afficher_pdf = tk.Button(root, text="Afficher PDF", command=afficher_pdf)
btn_afficher_pdf.pack(pady=5)

# Cadre pour afficher les résultats
result_frame = tk.Frame(root)
result_frame.pack(pady=10)

# Lancement de l'interface
root.mainloop()
