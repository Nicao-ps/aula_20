import numpy as np
import pandas as pd

try:
	print('\nCarregando banco de dados ...')
	PATH_ARCHIVE = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"
	
	print('\n'+(89*'-'))
	print('                              Base DP Evolução Mensal Cisp                              ')
	print((89*'-')+'\n')

	# dataframe da serie
	df_ocorrencias = pd.read_csv(PATH_ARCHIVE, sep=';', encoding='iso-8859-1')
	df_ocorrencias = df_ocorrencias[['munic', 'roubo_veiculo']]
	df_roubo_veiculo = df_ocorrencias.groupby('munic').sum(['roubo_veiculo']).reset_index()	
	print(df_roubo_veiculo)

except Exception as e:
	print(f"Erro ao carregar dados: {e}")
	exit()

try:
	print('\nManipulando os dados para apresentação ...')

	# array da serie
	array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

	print('\n'+(89*'-'))
	print('                              Medidas de Tendência Central                              ')
	print((89*'-')+'\n')

	# média da serie
	med_roubo_veiculo = np.mean(array_roubo_veiculo)
	print(f'Média: {med_roubo_veiculo:.2f}')

	# mediana da serie
	median_roubo_veiculo = np.median(array_roubo_veiculo)
	print(f'Mediana: {median_roubo_veiculo:.2f}')

	# distância absoluta da serie
	distance_roubo_veiculo = np.abs((med_roubo_veiculo - median_roubo_veiculo) / med_roubo_veiculo)  
	print(f'Distância: {distance_roubo_veiculo:.2f}')

	print('\n'+(89*'-'))
	print('                                 Medidas de Dispersão                                 ')
	print((89*'-')+'\n')

	# máximo da serie
	max_roubo_veiculo = np.max(array_roubo_veiculo)
	print(f'Máximo: {max_roubo_veiculo:.2f}')

	# mínimo da serie
	min_roubo_veiculo = np.min(array_roubo_veiculo)
	print(f'Mínimo: {min_roubo_veiculo:.2f}')

	# amplitude total da serie
	amp_roubo_veiculo = max_roubo_veiculo - min_roubo_veiculo
	print(f'Amplitude: {amp_roubo_veiculo:.2f}')

	print('\n'+(89*'-'))
	print('                              Medidas de Posição                              ')
	print((89*'-')+'\n')
	
	# quantis da serie
	print('Quantis:\n')
	list_q = []
	qtt_q = int(input('Quantis utilizados para análise: '))
	print('')
	for i in range(qtt_q):
		q = float(input(f'Informe o q{i + 1}: '))
		list_q.append(q)
	print('')
	for i in range(qtt_q):
		print(f'q{i + 1} = {np.quantile(array_roubo_veiculo, list_q[i], method="weibull"):.2f}')
	print('')

	# intervalo interquantil
	iqr = np.quantile(array_roubo_veiculo, list_q[qtt_q - 1], method="weibull") - np.quantile(array_roubo_veiculo, list_q[0], method="weibull")
	print(f'Intervalo interquantil: {iqr:.2f}')

	print('\nLimites:\n')

	# limite superior da serie
	mayor_limit = np.quantile(array_roubo_veiculo, list_q[qtt_q - 1], method="weibull") + (1.5 * iqr)
	print(f'Limite superior: {mayor_limit:.2f}')

	# limite inferior da serie
	minor_limit = np.quantile(array_roubo_veiculo, list_q[0], method="weibull") - (1.5 * iqr)
	print(f'Limite inferior: {minor_limit:.2f}')

	# maiores da serie
	print('\nMaiores:\n')
	df_roubo_veiculo_mayors = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > np.quantile(array_roubo_veiculo, list_q[qtt_q - 1], method="weibull")]
	print(df_roubo_veiculo_mayors.sort_values(by='roubo_veiculo', ascending=False))

	# menores da serie
	print('\nMenores:\n')
	df_roubo_veiculo_minors = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < np.quantile(array_roubo_veiculo, list_q[0], method="weibull")]
	print(df_roubo_veiculo_minors.sort_values(by='roubo_veiculo', ascending=True))

	print('\nOutliers:\n')
	
	# outliers superiores da serie
	df_roubo_veiculo_mayors_outliers = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > mayor_limit]
	if len(df_roubo_veiculo_mayors_outliers) == 0:
		print('\nNão existe outliers superiores!')
	else:
		print('\nOutliers Superiores:\n')
		print(df_roubo_veiculo_mayors_outliers.sort_values(by='roubo_veiculo', ascending=False))

	# outliers inferiores da serie
	df_roubo_veiculo_minors_outliers = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < minor_limit]

	if len(df_roubo_veiculo_minors_outliers) == 0:
		print('\nNão existem outliers inferiores!')
	else:
		print('\nOutliers Inferiores:\n')
		print(df_roubo_veiculo_minors_outliers.sort_values(by='roubo_veiculo', ascending=True))

except Exception as e:
	print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
	exit()

# plotar graficos da serie:
	# pip install matplotlib

try:
	import matplotlib.pyplot as plt
	
	fig, ax = plt.subplots(1, 2, figsize=(18, 6))

	if not df_roubo_veiculo_minors_outliers.empty:
		lower_data = df_roubo_veiculo_minors_outliers.sort_values(by='roubo_veiculo', ascending=True)
		ax[0].barh(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'], color='#FF6000')
		
	else:
		dados_inferiores = df_roubo_veiculo_minors_outliers.sort_values(by='roubo_veiculo', ascending=False)
		ax[0].bar(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'], color='#FF6000')
		ax[0].set_title('Menores Roubos')
		ax[0].set_xticks([])
		ax[0].set_yticks([])

	plt.tight_layout()
	plt.show()

except Exception as e:
	print(f'Erro ao plotar o gráfico: {e}')

