import pandas as pd
import matplotlib.pyplot as plt
"""
print("[1] Grafico de acordo com os anos no Brasil.")
print("[2] Grafico de acordo com os anos no Mundo.")
print("[3] 5 tipos que afetaram mais e menos no país escolhido.")
print("[4] O tipo com mais ocorrência no mundo inteiro em todos os anos.")
print("[5] Sair.")
resp = int(input("Escolha: "))
"""

# Importando o dataset
df = pd.read_csv("Dataset.csv", encoding="UTF-8")

# Arredondando os números
df = round(df)

def op1():
    # Apenas pegando no dataset os dados onde o Contry é Brazil
    table_brazil = df[df["Country"] == "Brazil"]
    table_brazil = round(table_brazil)
    
    fig, ax = plt.subplots()
    

    columns = [df.index.name] + [i for i in df.columns] # Salvando o cabeçalho
    anos = list(range(1990, 2017)) # Salvando a lista de anos
    rows = [[i for i in row] for row in table_brazil.itertuples()] # Salvando todo o resto dos dados em uma lista de listas

    for i in range(4, len(columns)): # Iterador para acessar a posição do elemento, nas colunas de interesse
        lista_nums = []
        for j in rows: # Passando por cada linha para ter acesso à elementos
            lista_nums.append(j[i]) # Adicionando os totais de vitimas à uma lista para ter o desenvolvimento de gráfico
        ax.plot(anos, lista_nums, label=columns[i]) # Criando um elemento no gráfico com os dados de 1990-2016
    
    
    ax.set_xlabel('Anos') # X = Anos
    ax.set_ylabel('Quantidade de casos') # Y = Qtd de casos
    ax.legend() # Ativando a legenda do gráfico
    plt.show() # mostrando o gráfico


def op2():
    
    fig, ax = plt.subplots() # Iniciando o figure e o gráfico à ser programado
    teste = df.groupby(["Year"]).sum().reset_index() # Agrupando todos os dados para ter o total em todos os países dos anos 1990 - 2016
    print(teste)
    columns = [df.index.name] + [i for i in df.columns] # Salvando o cabeçalho
    anos = list(range(1990, 2017)) # Salvando a lista de anos
    rows = [[i for i in row] for row in teste.itertuples()] # Salvando todo o resto dos dados em uma lista de listas

    for i in range(4, len(columns)): # Iterador para acessar a posição do elemento, nas colunas de interesse
        lista_nums = []
        for j in rows: # Passando por cada linha para ter acesso à elementos
            lista_nums.append(j[i]) # Adicionando os totais de vitimas à uma lista para ter o desenvolvimento de gráfico
        ax.plot(anos, lista_nums, label=columns[i]) # Criando um elemento no gráfico com os dados de 1990-2016
    
    ax.set_xlabel('Anos') # X = Anos
    ax.set_ylabel('Quantidade de casos') # Y = Qtd de casos
    ax.legend() # Ativando a legenda do gráfico
    plt.show() # mostrando o gráfico

    