# Générez un pairplot avec Seaborn pour visualiser les relations entre quatre variables aléatoires.

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Génération de données aléatoires
data = np.random.rand(100, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Création du pairplot avec Seaborn
sns.pairplot(df)

# Affichage du pairplot
plt.show()
