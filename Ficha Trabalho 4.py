import pandas as pd

print("")
print("************* Consumo Energia electrica Mundial 1990-2000 *************")
print("")

# Carregar dados do Excel
data = pd.read_excel('WorldBank.xlsx', sheet_name='Data')
#print(data)

# Selecionar as colunas de interesse (País, Ano e Consumo de Energia)
data = data[['Country Name', '1990 [YR1990]', '2000 [YR2000]']]

# Filtrar os dados para Portugal
data_portugal = data[data['Country Name'] == 'Portugal']

# Filtrar os dados para Brasil
data_brasil = data[data['Country Name'] == 'Brazil']

# Calcular a variação percentual
def calcular_variacao_percentual(consumo_inicial, consumo_final):
    return (consumo_final - consumo_inicial) / consumo_inicial * 100

variacao_percentual= calcular_variacao_percentual(data_portugal['1990 [YR1990]'].values[0], data_portugal['2000 [YR2000]'].values[0])


print(f'Variação percentual no consumo de energia elétrica em Portugal entre 1990 e 2000: {variacao_percentual:.2f}%')
print("")


while True:
    print("\nMenu Opções:\n")
    print("1. Ver tabela todos os paises")
    print("2. **Ver dados Portugal")
    print("3. **Ver dados Brasil")
    print("4. Ver Variação Percentual Consumo Portugal 1990 e 2000")
    print("5. Ver Variação Percentual Consumo Brasil 1990 e 2000")
    print("6. Ver dados Outro País")
    print("7. Ver Variação Percentual Consumo outro país 1990 e 2000")
    print("8. Sair")
    print("")
    opcao=input("Escolha opção: ")
    
    if opcao=='1':
        print("\n",data,"\n")
    if opcao=='2':
        print("\n",data_portugal,"\n")
        #print(data_portugal['1990 [YR1990]'].values[0])
    if opcao=='3':
        print("\n",data_brasil,"\n")
        #print(data_portugal['1990 [YR1990]'].values[0])
    if opcao=='4':
        #print("")
        variacao_percentual= calcular_variacao_percentual(data_portugal['1990 [YR1990]'].values[0], data_portugal['2000 [YR2000]'].values[0])
        print(f'\nVariação percentual no consumo de energia elétrica em Portugal entre 1990 e 2000: {variacao_percentual:.2f}%\n')
        #print("")
    if opcao=='5':
        #print("")
        variacao_percentual= calcular_variacao_percentual(data_brasil['1990 [YR1990]'].values[0], data_brasil['2000 [YR2000]'].values[0])
        print(f'\nVariação percentual no consumo de energia elétrica em Brasil entre 1990 e 2000: {variacao_percentual:.2f}%\n')
        #print("")
    if opcao=='6':
        pais=input("\nQual o País: ")
        try:
            data_pais = data[data['Country Name'] == pais]
            #print("")
            print("\n",data_pais,"\n")
            #print("")
        except:
            print("\nInvalido. País nao encontrado.\n")
    if opcao=='7':
        pais=input("\nQual o País: ")
        try:
            data_pais = data[data['Country Name'] == pais]
            variacao_percentual= calcular_variacao_percentual(data_pais['1990 [YR1990]'].values[0], data_pais['2000 [YR2000]'].values[0])
            print(f'\nVariação percentual no consumo de energia elétrica em {pais} entre 1990 e 2000: {variacao_percentual:.2f}%\n')
        except:
            print("\nInvalido. País nao encontrado.\n")
    if opcao=='8':
        break