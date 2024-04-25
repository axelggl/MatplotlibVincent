# Créez un histogramme pour visualiser la distribution de 100 valeurs aléatoires tirées d'une distribution normale.

import matplotlib.pyplot as plt
import numpy as np

# Génération de 100 valeurs aléatoires tirées d'une distribution normale
data = np.random.randn(100)

# Tracé de l'histogramme
plt.hist(data, bins=10, color='blue', edgecolor='black') # bins=10 pour diviser les données en 10 intervalles
plt.title('Histogramme de la distribution normale')
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.grid(True)  # Ajout d'une grille pour une meilleure lisibilité

plt.show()