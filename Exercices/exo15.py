# Créez un graphique interactif avec Plotly pour explorer les données sur les passagers du Titanic.

import seaborn as sns
import plotly.express as px

# Charger les données sur les passagers du Titanic
titanic_data = sns.load_dataset('titanic')

# Créer un graphique interactif avec Plotly Express
fig = px.scatter(titanic_data, x='age', y='fare', color='survived', 
                 hover_data=['sex', 'class', 'who'], 
                 title='Exploration des données des passagers du Titanic',
                 labels={'age': 'Âge', 'fare': 'Tarif', 'survived': 'Survécu'})

# Afficher le graphique interactif
fig.show()
    