# Modifiez le graphique précédent en ajoutant un titre, des labels pour les axes et changez la couleur de la ligne en rouge.

import matplotlib.pyplot as plt
import numpy as np

# Génération de la série de 50 nombres allant de 0 à 10
x = np.linspace(0, 10, 50)

# Création de la série y (par exemple, le carré des valeurs de x)
y = x**2

# Tracé du graphique de ligne
plt.plot(x, y, marker='o', linestyle='-', color='red')  # marker='o' pour afficher des points sur la ligne
plt.title('Graphique de ligne de la série de nombres')
plt.xlabel('Valeurs de x')
plt.ylabel('Valeurs de y')
plt.grid(True)  # Ajout d'une grille pour une meilleure lisibilité
plt.show()
