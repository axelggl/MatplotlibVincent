# Ajoutez des barres d’erreurs verticales à un graphique à barres simples pour indiquer l’incertitude sur chaque barre.

import matplotlib.pyplot as plt

# Catégories de produits
categories = ['A', 'B', 'C', 'D', 'E']

# Nombre d'articles vendus dans chaque catégorie
articles_vendus = [150, 200, 175, 300, 250]

# Incertitude sur chaque barre
incertitude = [20, 30, 25, 40, 35]

# Création du graphique à barres
plt.bar(categories, articles_vendus, color='purple', yerr=incertitude, capsize=5)

# Ajout d'un titre et de labels pour les axes
plt.title('Nombre d\'articles vendus par catégorie')
plt.xlabel('Catégories')
plt.ylabel('Nombre d\'articles vendus')

# Affichage du graphique
plt.show()