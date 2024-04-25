# Créez une figure contenant deux subplots (graphiques) et tracez des données différentes dans chacun.

import matplotlib.pyplot as plt
import numpy as np

# Génération de la série de 50 nombres allant de 0 à 10
x = np.linspace(0, 10, 50)

# Création de la série y1 (par exemple, le carré des valeurs de x)
y1 = x**2

# Création de la série y2 (par exemple, le cube des valeurs de x)
y2 = x**3

# Création d'une figure contenant deux subplots
fig, ax = plt.subplots(1, 2)

# Tracé du graphique de ligne dans le premier subplot
ax[0].plot(x, y1, marker='o', linestyle='-', color='red', label='y = x^2')  # marker='o' pour afficher des points sur la ligne
ax[0].set_title('Graphique de ligne de y = x^2')
ax[0].set_xlabel('Valeurs de x')
ax[0].set_ylabel('Valeurs de y')
ax[0].legend()  # Affiche la légende
ax[0].grid(True)  # Ajout d'une grille pour une meilleure lisibilité

# Tracé du graphique de ligne dans le deuxième subplot
ax[1].plot(x, y2, marker='x', linestyle='--', color='blue', label='y = x^3')  # marker='x' pour afficher des croix sur la ligne
ax[1].set_title('Graphique de ligne de y = x^3')
ax[1].set_xlabel('Valeurs de x')
ax[1].set_ylabel('Valeurs de y')
ax[1].legend()  # Affiche la légende
ax[1].grid(True)  # Ajout d'une grille pour une meilleure lisibilité

plt.show()