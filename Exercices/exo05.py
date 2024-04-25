# Ajoutez une légende au graphique précédent, placez-la dans le coin supérieur droit.

import matplotlib.pyplot as plt
import numpy as np

# Génération de la série de 50 nombres allant de 0 à 10
x = np.linspace(0, 10, 50)

# Création de la série y1 (par exemple, le carré des valeurs de x)
y1 = x**2

# Création de la série y2 (par exemple, le cube des valeurs de x)
y2 = x**3

# Tracé du graphique de ligne
plt.plot(x, y1, marker='o', linestyle='-', color='red', label='y = x^2')  # marker='o' pour afficher des points sur la ligne
plt.plot(x, y2, marker='x', linestyle='--', color='blue', label='y = x^3')  # marker='x' pour afficher des croix sur la ligne
plt.title('Graphique de ligne de deux séries de nombres')
plt.xlabel('Valeurs de x')
plt.ylabel('Valeurs de y')
plt.legend(loc='upper right')  # Affiche la légende
plt.grid(True)  # Ajout d'une grille pour une meilleure lisibilité
plt.show()

