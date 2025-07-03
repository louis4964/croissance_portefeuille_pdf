# Simulation de Croissance de Portefeuille à investissement annuel avec PDF bilan

## Description
1. Ce logiciel est conçu pour aider les utilisateurs à estimer la croissance d'un portefeuille financier sur une période définie, en tenant compte des ajouts annuels et des intérêts composés. Les résultats fournissent une vue d'ensemble des gains, avec un affichage du total avec et sans les intérêts.

## Fonctionnalités
1.  Calculateur de croissance : Calcule la croissance du portefeuille sur n années en fonction des taux et des valeurs investies.
2. Affichage dde la valeur du portefeuille avec et sans interêts au bout de n années pour comparer.
3. Interface utilisateur : Interface simple et intuitive réalisée avec Tkinter, comprenant des zones de textes pour les actifs, les intérêts de chacun et le nombre d'années.
4. Personnalisation : nombre d'actifs souhaités
5. Possibilité de Téléchargement de PDF qui récapitule la simulation.

## Utilisation
- Entrez le nombre d'années pour la prévision.
- Entrez la liste des montants investis (séparés par des espaces).
- Entrez la liste des croissances annuelles + 1 (séparés par des espaces).
- Cliquez sur "Valider" pour afficher les résultats.
- Cliquer sur "PDF" pour accéder au PDF de la simulation.

## Structure 
- prog_logiciel.py : Fichier principal de l’application, contenant l’interface utilisateur et la logique de calcul avec les 4 fonctions principales.
    1. Prevision - Permet de prevoir l'evolution du prix des actifs au bout de n années avec le reinvestissement annuel.
    2. Total_avec_interets - Calcule le total de la valeur du portefeuille au bout de n années avec les intérêts. 
    3. Total_sans_interet - Calcule le total de la valeur de l'investissement au bout de n années sans les intérêts.
    4. Croissance_portefeuille - Permet de connaître la croissance du portefeuille créé sur les n années de prevision.
    5. Official.pdf - Permet de générer un PDF bilan de la simulation 
- README.md : Documentation du projet.
- requirements.txt : Fichier listant les dépendances nécessaires pour exécuter le projet.

## Contributions
Les contributions sont les bienvenues ! N'hésitez pas à soumettre un pull request.

## Licence
Ce projet est sous licence MIT.

## Auteur 
Louis Thomas