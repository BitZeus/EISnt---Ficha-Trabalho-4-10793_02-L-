import pandas as pd

print("")
print("************* Consumo Energia electrica Mundial 1990-2000 *************")
print("")

# Carregar dados do Excel
data = pd.read_excel('WorldBank.xlsx', sheet_name='Data')
#print(data)

# Selecionar as colunas de interesse (País, Ano e Consumo de Energia)
data = data[['Country Name', '1990 [YR1990]', '2000 [YR2000]']]
print(data)

# Filtrar os dados para Portugal
data_portugal = data[data['Country Name'] == 'Portugal']
#print(data_portugal['1990 [YR1990]'].values[0])

# Calcular a variação percentual
def calcular_variacao_percentual(consumo_inicial, consumo_final):
    return (consumo_final - consumo_inicial) / consumo_inicial * 100

variacao_percentual= calcular_variacao_percentual(data_portugal['1990 [YR1990]'].values[0], data_portugal['2000 [YR2000]'].values[0])
#print(variacao_percentual)

print(f'Variação percentual no consumo de energia elétrica em Portugal entre 1990 e 2000: {variacao_percentual:.2f}%')
print("")