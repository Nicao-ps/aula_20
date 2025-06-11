import numpy as np
import pandas as pd

PATH_ARCHIVE = 

# dataframe da serie
df_roubo_veiculo = pd.read_csv(PATH_ARCHIVE, sep=';', encoding='iso-8859-1')

# array da serie
array_roubo_veiculo = np.array(df_roubo_veiculo)

print('\n'+89*'*')
print('\nMedidas de Tendência Central: \n')

# média da serie
media_roubo_veiculo = np.mean(array_roubo_veiculo)
print(f'Média: {media_roubo_veiculo}')

# mediana da serie
mediana_roubo_veiculo = np.median(array_roubo_veiculo)
print(f'Mediana: {mediana_roubo_veiculo}')

# distância absoluta da serie
distancia_roubo_veiculo = np.abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo)  

print('\n'+89*'*')
print('\nMedidas de Dispersão: \n')

# máximo da serie
maximo_roubo_veiculo = np.max(array_roubo_veiculo)

# mínimo da serie
minimo_roubo_veiculo = np.min(array_roubo_veiculo)

# amplitude total da serie
amplitude_roubo_veiculo = maximo_roubo_veiculo - minimo_roubo_veiculo


list_qn = []
qtt_qn = int(input('\nInforme quantos quantis serão utilizados: '))
for i in range(qtt_qn):
	qn = float(input(f'Informe o q{i + 1}: '))
	list_qn.append(qn)
print(f'\nOs quantis serão {list_qn}\n')

for i in range(qtt_qn):
	print(f'q[{i}] = {np.quantile(array_serie, list_qn[i], method="weibull")}')

# limite superior


# limite inferior