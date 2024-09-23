from sklearn.datasets import fetch_california_housing 
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


ch = fetch_california_housing()
chd = ch.data
# criacao do dataframe e adicao da nova coluna [medhousevalue] 
cdf = pd.DataFrame(chd, columns=ch.feature_names)
# gerando nova coluna usando a funcao target
cdf['MedhouseValue'] = ch.target


# Calculando a assimetria e a curtose para as variáveis de interesse
assimetrias = cdf[['HouseAge', 'MedInc', 'MedhouseValue']].skew()
curtoses = cdf[['HouseAge', 'MedInc', 'MedhouseValue']].kurt()

print("Assimetria:")
print(assimetrias)

print("\nCurtose:")
print(curtoses)
