import pandas as pd
from scipy.stats import linregress

# Lire les données
fichier = pd.read_csv('jfreechart-test-stats.csv')

# Régression linéaire pour TLOC et TASSERT
slope, intercept, r_value, p_value, std_err = linregress(fichier['TLOC'], fichier[' TASSERT'])
print(f'Régression linéaire pour TLOC et TASSERT: r(Pearson) = {r_value}')



# Régression linéaire pour WMC et TASSERT
slope, intercept, r_value, p_value, std_err = linregress(fichier[' WMC'], fichier[' TASSERT'])
print(f'Régression linéaire pour WMC et TASSERT: r(Pearson) = {r_value}')
