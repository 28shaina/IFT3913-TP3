import pandas as pd
import matplotlib as plt
import seaborn as sns

# Lire les données
fichier = pd.read_csv('jfreechart-test-stats.csv')

# Calculer les statistiques
stats = fichier[['TLOC', ' WMC', ' TASSERT']].describe()

# Afficher la médiane, le premier et le troisième quartile
print("Médiane (m) :\n", stats.loc['50%'])
print("\nPremier quartile (l) :\n", stats.loc['25%'])
print("\nTroisième quartile (u) :\n", stats.loc['75%'])

# T1: Visualisation des métriques
plt.figure(figsize=(10, 7))
sns.boxplot(data=fichier[['TLOC', ' WMC', ' TASSERT']])
plt.title('Boîtes à moustaches pour TLOC, WMC et TASSERT')
plt.show()









