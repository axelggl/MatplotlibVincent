# Créez un graphique à empilement qui montre comment trois groupes de données évoluent avec le temps.

import matplotlib.pyplot as plt
import numpy as np

# Données factices pour les trois groupes
temps = np.arange(10)  # Temps allant de 0 à 9
groupe1 = np.random.randint(1, 10, size=10)
groupe2 = np.random.randint(1, 10, size=10)
groupe3 = np.random.randint(1, 10, size=10)

# Créer le graphique à empilement
plt.figure(figsize=(10, 6))
plt.stackplot(temps, groupe1, groupe2, groupe3, labels=['Groupe 1', 'Groupe 2', 'Groupe 3'])

# Ajouter des étiquettes et des titres
plt.xlabel('Temps')
plt.ylabel('Valeurs')
plt.title('Évolution des groupes de données avec le temps')
plt.legend(loc='upper left')

# Afficher le graphique
plt.show()
