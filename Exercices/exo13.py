# Utilisez Seaborn pour créer un heatmap à partir d’une matrice de corrélations.

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Génération d'une matrice de corrélations aléatoire
data = np.random.rand(10, 10)
correlations = np.corrcoef(data)

# Création du heatmap avec Seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlations, annot=True, cmap='coolwarm')

# Ajout d'un titre
plt.title('Heatmap de la matrice de corrélations')

# Affichage du heatmap
plt.show()