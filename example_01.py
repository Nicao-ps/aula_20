import numpy as np
import pandas as pd

print('\nLoading Data...\n')
PATH_ARCHIVE = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"

# dataframe da serie
df_ocorrencias = pd.read_csv(PATH_ARCHIVE, sep=';', encoding='iso-8859-1')
df_ocorrencias = df_ocorrencias[['munic', 'roubo_veiculo']]
df_roubo_veiculo = df_ocorrencias.groupby('munic').sum(['roubo_veiculo']).reset_index()
print(df_roubo_veiculo)

# array da serie
array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

print('\n'+89*'-')
print('\nMedidas de Tendência Central: \n')

# média da serie
med_roubo_veiculo = np.mean(array_roubo_veiculo)
print(f'Média: {med_roubo_veiculo:.2f}')

# mediana da serie
median_roubo_veiculo = np.median(array_roubo_veiculo)
print(f'Mediana: {median_roubo_veiculo:.2f}')

# distância absoluta da serie
distance_roubo_veiculo = np.abs((med_roubo_veiculo - median_roubo_veiculo) / med_roubo_veiculo)  
print(f'Distância: {distance_roubo_veiculo:.2f}')

print('\nMedidas de Dispersão: \n')

# máximo da serie
max_roubo_veiculo = np.max(array_roubo_veiculo)
print(f'Máximo: {max_roubo_veiculo:.2f}')

# mínimo da serie
min_roubo_veiculo = np.min(array_roubo_veiculo)
print(f'Mínimo: {min_roubo_veiculo:.2f}')

# amplitude total da serie
amp_roubo_veiculo = max_roubo_veiculo - min_roubo_veiculo
print(f'Amplitude: {amp_roubo_veiculo:.2f}')

print('\nMedidas de Posição: \n')

list_qn = []
qtt_qn = int(input('Informe quantos quantis serão utilizados: '))
for i in range(qtt_qn):
	qn = float(input(f'Informe o q{i + 1}: '))
	list_qn.append(qn)
print(f'\nOs quantis serão {list_qn}\n')

for i in range(qtt_qn):
	print(f'q{i + 1} = {np.quantile(array_roubo_veiculo, list_qn[i], method="weibull"):.2f}')

# limite superior


# limite inferior
