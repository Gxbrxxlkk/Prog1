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

print(ch)
# Supondo que df seja o seu DataFrame
# Calculando a matriz de correlação
correlacao = cdf.drop(columns=['Longitude', 'Latitude']).corr()

print(correlacao)
#     MedInc  HouseAge  AveRooms  AveBedrms  Population  AveOccup  MedhouseValue


# Gráfico de dispersão entre HouseAge e MedHouseVal
plt.figure(figsize=(15, 15))
sns.scatterplot(x='HouseAge', y='MedhouseValue', data=cdf)
plt.title('Relação entre Idade da Casa e Valor do Imóvel')
plt.xlabel('Idade da Casa (HouseAge)')
plt.ylabel('Valor do Imóvel (MedhouseValue)')
plt.show()

# Gráfico de dispersão entre MedInc e MedHouseVal
plt.figure(figsize=(15, 15))
sns.scatterplot(x='MedInc', y='MedhouseValue', data=cdf)
plt.title('Relação entre Renda Familiar e Valor do Imóvel')
plt.xlabel('Renda Familiar (MedInc)')
plt.ylabel('Valor do Imóvel (MedhouseValue)')
plt.show()

"""
import statsmodels.api as sm

# Definindo a variável dependente (target) e independentes
X = cdf[['HouseAge', 'MedInc']]
y = cdf['MedhouseValue']

# Adicionando uma constante ao modelo
X = sm.add_constant(X)

# Criando o modelo de regressão
modelo = sm.OLS(y, X).fit()

# Mostrando o resumo do modelo
print(modelo.summary())
"""
