# Générez deux séries de 100 points chacune, suivant une distribution normale, et affichez-les dans un graphique de dispersion.

import matplotlib.pyplot as plt
import numpy as np

# Génération des données
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)

# Création du graphique de dispersion
plt.scatter(x, y, color='green')

# Ajout d'un titre et de labels pour les axes
plt.title('Graphique de dispersion')
plt.xlabel('X')
plt.ylabel('Y')

# Affichage du graphique
plt.show()