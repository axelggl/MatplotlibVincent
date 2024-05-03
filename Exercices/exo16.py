# Utilisez Seaborn pour tracer un boxplot montrant la distribution des valeurs dans plusieurs groupes.

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Génération de données factices pour les groupes
groupe1 = np.random.normal(0, 1, 100)
groupe2 = np.random.normal(1, 1.5, 100)
groupe3 = np.random.normal(2, 2, 100)

# Création du boxplot avec Seaborn
plt.figure(figsize=(10, 6))
sns.boxplot(data=[groupe1, groupe2, groupe3], palette='Set2')

# Ajout d'un titre
plt.title('Boxplot des trois groupes de données')

# Affichage du boxplot
plt.show()