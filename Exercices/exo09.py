# Créez un graphique à barres pour comparer le nombre d'articles vendus dans 5 catégories différentes.

import matplotlib.pyplot as plt

# Catégories de produits
categories = ['A', 'B', 'C', 'D', 'E']

# Nombre d'articles vendus dans chaque catégorie
articles_vendus = [150, 200, 175, 300, 250]

# Création du graphique à barres
plt.bar(categories, articles_vendus, color='skyblue')

# Ajout d'un titre et de labels pour les axes
plt.title('Nombre d\'articles vendus par catégorie')
plt.xlabel('Catégories')
plt.ylabel('Nombre d\'articles vendus')

# Affichage du graphique
plt.show()