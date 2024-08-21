import pandas as pd

import matplotlib.pyplot as plt

Simulação de dados jurídicos

data = {

    'Caso_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Advogado_Responsável': ['Carlos', 'Ana', 'Bruno', 'Carlos', 'Ana', 'Diana', 'Bruno', 'Carlos', 'Ana', 'Diana'],
    'Tipo_Proc': ['Cível', 'Trabalho', 'Cível', 'Empresarial', 'Cível', 'Trabalho', 'Empresarial', 'Cível', 'Empresarial', 'Trabalho'],
    'Data_Abertura': pd.to_datetime(['2024-01-10', '2024-02-15', '2024-01-20', '2024-03-10', '2024-01-25', 
                                     '2024-02-18', '2024-03-05', '2024-01-30', '2024-03-15', '2024-02-25']),
    'Valor_Causa': [15000, 8000, 12000, 20000, 18000, 7000, 22000, 16000, 21000, 7500],
    'Resultado': ['Ganho', 'Perda', 'Ganho', 'Ganho', 'Perda', 'Ganho', 'Perda', 'Ganho', 'Ganho', 'Perda']

}

Criação do DataFrame

df = pd.DataFrame(data)

1. Limpeza de Dados (verificação de dados faltantes)

print("Dados faltantes:\n", df.isnull().sum())

2. Análise Exploratória

print("\nEstatísticas Descritivas:\n", df.describe())

Distribuição dos tipos de processos

tipo_proc_dist = df['Tipo_Proc'].value_counts()

print("\nDistribuição de Tipos de Processos:\n", tipo_proc_dist)

3. Agrupamento por Advogado e Tipo de Processo

agrupamento_adv_proc = df.groupby(['Advogado_Responsável', 'Tipo_Proc']).agg({

    'Caso_ID': 'count',
    'Valor_Causa': 'sum',
    'Resultado': lambda x: (x == 'Ganho').sum() / len(x)

}).rename(columns={'Caso_ID': 'Número de Casos', 'Valor_Causa': 'Total Valor Causa', 'Resultado': 'Taxa de Sucesso'})

print("\nAgrupamento por Advogado e Tipo de Processo:\n", agrupamento_adv_proc)

4. Análise Temporal (Tendências ao longo do tempo)

df.set_index('Data_Abertura', inplace=True)

casos_por_mes = df.resample('M').size()

print("\nNúmero de Casos por Mês:\n", casos_por_mes)

5. Visualização dos Dados

plt.figure(figsize=(10, 6))

Gráfico de barras da distribuição de tipos de processos

plt.subplot(2, 1, 1)

tipo_proc_dist.plot(kind='bar', color='skyblue')

plt.title('Distribuição de Tipos de Processos')

plt.xlabel('Tipo de Processo')

plt.ylabel('Número de Casos')

Gráfico de linha para a tendência de casos ao longo do tempo

plt.subplot(2, 1, 2)

casos_por_mes.plot(kind='line', marker='o', color='green')

plt.title('Tendência de Casos ao Longo do Tempo')

plt.xlabel('Data de Abertura')

plt.ylabel('Número de Casos')

plt.tight_layout()

plt.show()

6. Exportação de Resultados

agrupamento_adv_proc.to_csv('agrupamento_adv_proc.csv')

casos_por_mes.to_csv('casos_por_mes.csv')


