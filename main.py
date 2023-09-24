import pandas as pd
import matplotlib.pyplot as plt
import operator

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
    grouped = df.groupby(["Year"]).sum().reset_index() # Agrupando todos os dados para ter o total em todos os países dos anos 1990 - 2016
    columns = [df.index.name] + [i for i in df.columns] # Salvando o cabeçalho
    anos = list(range(1990, 2017)) # Salvando a lista de anos
    rows = [[i for i in row] for row in grouped.itertuples()] # Salvando todo o resto dos dados em uma lista de listas

    for i in range(4, len(columns)): # Iterador para acessar a posição do elemento, nas colunas de interesse
        lista_nums = []
        for j in rows: # Passando por cada linha para ter acesso à elementos
            lista_nums.append(j[i]) # Adicionando os totais de vitimas à uma lista para ter o desenvolvimento de gráfico
        ax.plot(anos, lista_nums, label=columns[i]) # Criando um elemento no gráfico com os dados de 1990-2016
    
    ax.set_xlabel('Anos') # X = Anos
    ax.set_ylabel('Quantidade de casos') # Y = Qtd de casos
    ax.legend() # Ativando a legenda do gráfico
    plt.show() # mostrando o gráfico

df_cancer = df.drop('Code', axis=1)






def op3(pais = 'Brazil', ano = 1990, td_pais = False) :
    anos = [x for x in range(1990, 2017)]
    for k, v in enumerate(anos):
        if ano == v:
            ano = k
            

    grouped = df_cancer.groupby(['Country', 'Year']).sum().round().reset_index()
    res = grouped[df['Country'] == pais].reset_index()
    lista = []
    pr = res.loc[ano].drop(labels=['index', 'Country', 'Year']).sort_values(ascending=False).head()
    pr_1 = res.loc[ano].drop(labels=['index', 'Country', 'Year']).sort_values(ascending=True).head()
    
    
    colunas = []
    valores = []
    
    
    x = [dict(pr),  dict(sorted(pr_1.items(),key=lambda item: item[1],  reverse=True))]
    
    
    for i in range(2):
         for k, v in x[i].items():
            colunas.append(k)
            valores.append(v)
    
    for i in res.loc[ano].drop(labels=['index', 'Country', 'Year']):
        lista.append(i)
    maior = max(lista)

    for k, v in dict(res.loc[ano]).items(): 
        if v == maior:
            return k if td_pais  else printa3(valores, colunas)


def op4(pais=[]):
    
    todos_paises = df['Country'].drop_duplicates().reset_index().drop(['index'], axis=1)
    
    if pais:
         paises = pais
    else:
        paises = todos_paises['Country']
        
    anos = [x for x in range(1990, 2017)]
    cancer = {}
        
    for p in paises:
        print(p)
        for ano in anos:
            nome = op3(p, ano, True)
            if nome not in cancer:
                cancer[nome] = 1
            else:
                cancer[nome] += 1
                
    return print(max(cancer.items(), key=operator.itemgetter(1))[0])



def printa3(valores, colunas):
    fig, ax = plt.subplots()
    fig, ab = plt.subplots()
    maiores_val = valores[0:5]
    maiores_nome = colunas[0:5]
    menores_val= valores[5:]
    menores_nome= colunas[5:]

    ax.bar(maiores_nome, maiores_val)
    ax.set_xlabel('Tipos de Câncer')
    ax.set_ylabel('Quantidade de casos')
    ax.set_title('5 Maiores')

    ab.bar(menores_nome, menores_val)
    ab.set_xlabel('Tipos de Câncer')
    ab.set_ylabel('Quantidade de casos')
    ab.set_title('5 Menores')
    plt.show()


op4()