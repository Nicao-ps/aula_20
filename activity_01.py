import pandas as pd
import numpy as np
import os

try:
    print('Loading Data...')
    PATH_ARCHIVE = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"

except:


df_estelionatos = pd.read_csv(PATH_ARCHIVE, sep=';', encoding='iso-8859-1')

# array da serie de estelionatos
array_estelionatos = np.array(df_estelionatos)

# média da serie de estelionatos
media_estelionatos = np.mean(array_estelionatos)

# mediana da serie de estelionatos
mediana_estelionatos = np.median(array_estelionatos)  

# distância absoluta da serie de estelionatos
distancia_estelionatos = np.abs((media_estelionatos - mediana_estelionatos) / mediana_estelionatos)  