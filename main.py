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

df = pd.read_csv("Dataset.csv", encoding="UTF-8")
df = round(df)

def op1():

    table_brazil = df[df["Country"] == "Brazil"]
    table_brazil = round(table_brazil)
    fig, ax = plt.subplots()
    
    columns = [df.index.name] + [i for i in df.columns]
    anos = list(range(1990, 2017))
    rows = [[i for i in row] for row in table_brazil.itertuples()]

    for i in range(4, len(columns)):
        lista_nums = []
        for j in rows:
            lista_nums.append(j[i])
        ax.plot(anos, lista_nums, label=columns[i])
    
    
    ax.set_xlabel('Anos')
    ax.set_ylabel('Quantidade de casos')
    ax.legend()
    plt.show()


def op2():
    
    
    fig, ax = plt.subplots()
    teste = df.groupby(["Year"]).sum().reset_index()
    columns = [df.index.name] + [i for i in df.columns]
    anos = list(range(1990, 2017))
    rows = [[i for i in row] for row in teste.itertuples()]

    for i in range(4, len(columns)):
        lista_nums = []
        for j in rows:
            lista_nums.append(j[i])
        ax.plot(anos, lista_nums, label=columns[i])
    
    ax.set_xlabel('Anos')
    ax.set_ylabel('Quantidade de casos')
    ax.legend()
    plt.show()

