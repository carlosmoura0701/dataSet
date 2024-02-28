import pickle
from pathlib import Path
from streamlit_option_menu import option_menu
import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
import csv
import numpy as numpy
import requests
import altair as alt

#PIPES

#pip install pandas
#pip install jupyter

#obs: nao esquecer o sep=';' ou outro tipo de separador que exista no arquivo
#mostrando apenas o inicio: .head() . dentro do .head('quantidade de linhas')
#mostrar informações do dataSet .info()
#fazer o tratamento de de valores nulos nas colunas
#objetc = str
#type(data) Data Frame, tabela bidimensional de tamanho mutável com dados potencialmente hetereogeneos
#atributo .shape (colunas x linhas), passeando pelo df .shace[n], n=0 'qtd de linhas',n=1 'qtd de colunas'



import pandas as pd 

data = pd.read_csv('dataSet\csv\dataBase.csv', sep=';')

print('\n')

print('Tipo de dados de data: ',type(data))
print('\n')

print('Quantidade de linhas: ',data.shape[0],'Quantidade de colunas: ',data.shape[1])
print('\n')

print('Quantidade de linhas x colunas: ', data.shape)
print('\n')

print('DataFrame inteiro: ')
print('\n')

print(data)

#CRIAÇÃO DE UM DF - criar um df a partir de um dicionário:


personagens_df = pd.DataFrame({
    'nome': ['Luke Skywalker','Yoda','Palpatine'],
    'idade':[16,1000,70],
    'eh jedi':[True,True,False]
})
print('\n')

print('Tipo de dados de personagens_df: ',type(personagens_df))
print('\n')

print('Dados de personagens_df: ')
print('\n')

print(personagens_df.info())

print('Df personagens_df: \n', personagens_df)
print('\n')

#RENOMEAR TODAS AS COLUNAS DE UM DF - o atributo .columns retorna uma lista com o nome de todas as colunas do df

#personagens_df.rename() renomear

personagens_df_renomeado = personagens_df.rename(columns={
    'nome' : 'nome completo', #renomeia coluna nome
    'idade':'Idade' #renomeia coluna idade
})

print('Df personagens_df_renomeado: \n', personagens_df_renomeado)
print('\n')

#MODIFICAR O DF NO LOCAL ORIGINAL - inplace=True:

personagens_df.rename(columns={
    'nome' : 'nome completo', 
    'idade':'Idade'}, inplace=True) 

print('Df personagens_df: \n', personagens_df)
print('\n')

#RENOMEAR COLUNAS - renomear todas as colunas de uma vez, passar uma lista com todos os novos nomes personagens_df.columns = ['n','n','n']

personagens_df.columns = ['NOME','IDADE','JEDI?']

print('Df personagens_df: \n', personagens_df,'\n')

#SERIES - array unidimensional com os dados e rotulos de um eixo personangens_df['n'] ou personagens_df.N

print('Somente a coluna NOME: \n')
print(personagens_df['NOME'],'\n')

print('Somente a coluna IDADE: \n')
print(personagens_df.IDADE)

#SERIES II - selecionando a observação indexada no indice n, personagen_df.iloc[n]

print('Verificando terceira linha: \n')
print(personagens_df.iloc[2])

#CRIAÇÃO DE SERIES - pd.Series([n,n,n]) ainda outro: pd.Series([5.5,6.0,9.5], index=['p1','p2','teste'], name=Notas do Luke)

NovaLinha = pd.Series(['Dokan',65,False], index=['NOME','IDADE','JEDI?'])

personagens_df.iloc[2] = NovaLinha

print('Verificando terceira linha novamente: \n\n')
print(personagens_df.iloc[2])

print('Df personagens_df: \n\n', personagens_df)

#atribuindo dados ao df personagens_df['N'] <- não é uma cópia, é um ponteiro!

print(personagens_df['JEDI?'],'\n')

#copiaDaSeries = personagens_df['N'].copy() <- fazer uma cópia da series: 

copiaDaSeries = personagens_df['IDADE'].copy()

print('Cópia da Series personagens_df atributo IDADE: \n\n',copiaDaSeries,'\n')

#atribuindo um unico valor à coluna inteira ' <- Atribuindo o valor constante 'n' para cada linha da coluna n

jediBkcp = personagens_df['JEDI?'] = False
personagens_df['JEDI?'] = False

print('\n',personagens_df,'\n')

# atribuir lista ou series, é preciso passar a mesma quantidade de linhas. Percorrer a coluna:

nrows, ncols = personagens_df.shape #aqui conseguimos pegar o tamanho total de linhas e colunas como visto antes
 
novos_jedis = [f'Jedi {i}' for i in range(nrows)] 

print('Nova lista de Jedis:\n',novos_jedis,'\n')

#OBS: atribuindo a nova quantidade de elementos e essa quantidade é igual ao número de linhas do df

personagens_df['JEDI?'] = novos_jedis

print('Df modificado:\n', personagens_df,'\n\n')

#voltando aos valores iniciais:

personagens_df['JEDI?'] = jediBkcp

print('df modificado:\n', personagens_df,'\n\n')

#CRIAÇÃO DE COLUNA I - basta atribuir lista/Series de valores ou uma constante a uma nova "chave" do df. OBS: A quantidade de valores da lista precisa ser
#igual ao número de linhas/registros do df. A nova chave é o nome da coluna!

personagens_df['NOVA COLUNA'] = range(personagens_df.shape[0]) #personagens_df.shape[0] retorna a quantidade de linhas do df

print('Tabela com NOVA COLUNA: \n\n', personagens_df,'\n')

#CRIAÇÃO DE COLUNA II - criando uma coluna a partir de outra que já existe

personagens_df['IDADE DAQUI A 10 ANOS'] = personagens_df['IDADE'] + 10 #aumentando o atributo 'IDADE' linha por linha!

print('Tabela com nova coluna de IDADES: \n\n', personagens_df,'\n')

#range(personagens_df.shape[0]) <- INDICES 0 - 

#criando novo df para pesquisa com indices textuais (labels)

pesquisa_de_satisfacao = pd.DataFrame({
    'bom': [50,21,100],
    'ruim':[131,2,30],
    'pessimo':[30,20,1]
})

print('Novo df com indice numérico automático, pesquisa de satisfação:\n\n',pesquisa_de_satisfacao,'\n')

#ATRIBUINDO UM VALOR STR AO INDICE:

pesquisa_de_satisfacao = pd.DataFrame({
    'bom': [50,21,100],
    'ruim':[131,2,30],
    'pessimo':[30,20,1]
}, index=['Xbox One','PS4','Switch']) #<-- indice com nomes ao inves de valores! Mas continua funcionando o indice numérico!(OBS: O indice numérico é implícito)

print('Novo df com indice str criado, pesquisa de satisfação:\n\n',pesquisa_de_satisfacao,'\n')

#selecionando uma ou mais observações (Indexação)

# .iloc[n,n] <- seleciona elementos do df, baseado em seu índice(número) --> iloc.[row-first,column-second] <--

print('Indice 1 da pesquisa de satisfação: \n\n',personagens_df.iloc[1],'\n')

print(data,'\n\n')

print(data.iloc[1,1],data.iloc[1,0],'\n\n')

# .iloc[n:n] <- selecionando "slices", selecionando as linhas de 0 a 3 (sendo o 3 incluso) 

print(data.iloc[:4],'\n\n')

# .iloc[[n,n,n,n]] <- selecionando apenas as linhas n

print(data.iloc[[3,2,4]],'\n\n')

# .loc['n'] <- seleção baseada em rótulos, Label based selection

print('Rótulo PS4:',pesquisa_de_satisfacao.loc['PS4'],'\n\n') #<- retorna a linha cujo o rótulo é 'PS4'

# .loc[n,n]pesquisando dentro da linha pelo label

print('Quantas pessoas acharam PS4 Ruim: ',pesquisa_de_satisfacao.loc['PS4','ruim'],'\n\n')

# .loc[[n,n]]pesquisando somente pelo indice label

print('Mostrando somente Xbox e Ps4: \n\n',pesquisa_de_satisfacao.loc[['PS4','Xbox One']],'\n\n')

# selecionando todas as linhas e apenas as colunas com rótulos 'bom' e 'pessimo', OBS: não é preciso o .loc[n]

print('Pesquisa bom e péssimo(sem .loc): \n\n',pesquisa_de_satisfacao[['bom','pessimo']],'\n\n')

# selecionando todas as linhas e apenas as colunas com rótulos 'bom' e 'pessimo', OBS: usando o .loc[:,['bom','pessimo']] <-- conceito de slices

print('Pesquisa bom e péssimo(com .loc): \n\n', pesquisa_de_satisfacao.loc[:,['bom','pessimo']])

#OBS: IMPLICITAMENTE O PANDAS CONSIDERA O INDICE NUMÉRICO COMO RÓTULO (LABEL)! 

print('Exemplo do panda considerando o índice numérico como rótulo (label): \n\n',data.loc[2])

# n.[['n','n','n']] <- selecionando coluna inteira

print('Selecionando Colunas: Nome e Dias:\n\n', data[['Nome','Dias']],'\n\n')

# n.loc[:,'n'] <- selecionando todas as linhas da coluna n <- I

print('Selecionando todas as linhas da coluna Nome:\n\n', data.loc[:,'Nome'],'\n\n')

# n.coluna <- selecionando todas as linhas de uma coluna <- II

print('Selecionando todas as linhas da coluna Nome:\n\n', data.Nome,'\n\n') #<- OBS: SÓ FUNCIONA SE O NOME DA COLUNA NÃO POSSUIR ESPAÇOS! 

# n.['coluna'] <- para colunas cujos rótulos possuem caracteres inválidos, apenas a seleção via str é válida

print('Selecionando todas as linhas da coluna Nome:\n\n', data['Nome'],'\n\n')

# del df['n']<- removendo coluna n de um df, 

del data['Nome']

print('df sem a coluna Nome: \n\n',data,'\n\n')

# inserindo a coluna Nome no df

listaNomesNovos = ['Carlos','Miguel','Gabriel','Marcos','José','ELias','Juan']

data['Nomes Novos'] = listaNomesNovos

print('df com a nova coluna Nomes Novos: \n\n',data,'\n\n')

# salvando para csv, sempre usando o index = false

data.to_csv(r'C:\Users\889612123\Documents\GitHub\coding\dataSet\csv\dataBaseTest.csv',index=False,encoding='utf-8-sig')

# .unique(n) <- seleção de conteúdo, mostra os atributos da coluna n

print(data['Designacao'].unique(),'\n\n') # selecionando coluna estado, mostrandos os atributos da coluna 'Designacao'

# -------------- IMPORTANTE -------------- #

# df['n'] == 'i' <- retorna uma series onde o elemento i é pesquisado dentro da coluna n, compara elemento a elemento da series, retornando uma serie de booleans

print(data['Designacao']=='eletricista','\n\n')

selecao = data['Designacao'] == 'eletricista' 

print('Tipo da Series selecao: ', type(selecao),'\n')
print('Tamanho da selecao: ', selecao.shape,'\n')

# TOP!

print('Filtrando os elementos eletricista da coluna desiginação: \n',data[selecao],'\n\n') # TOP! Filtrando os elementos da coluna usando a serie de booleans

# df.loc[n] <- outro, também é possível retornar a seleção usando o método loc

print('Filtrando os elementos eletricista da coluna desiginação usando data.loc[selecao]: \n',data.loc[selecao],'\n\n')

# data.query('n') <- outro, também é possível retornar a seleção usando o método query, n é a pergunta

print('Busca utilizando o Query: \n',data.query('Designacao == "soldador"'),'\n\n') # utilizando aspas duplas dentro das aspas simples

# uma boa prática é salvar a pesquisa em uma variável!

soldadores = data.query('Designacao == "soldador"') # é umda df!

print('df salvo em uma variavel soldadores, que é um novo df: \n',soldadores,'\n\n') #vide os indices!

# df.reset_index() <- resetando os indices (se necessário)

soldadoresNovo = soldadores.reset_index()

print('Novo df com os indices resetados: \n',soldadoresNovo,'\n\n') # assim o indice antigo continua dentro do novo

# df.reset_index(drop=True) <- retorna uma cópia

soldadoresNovo = soldadores.reset_index(drop=True) # utilizando uma variável nova para não alterar o valor da variável original

print('Novo df com os indices resetados e sem os indices antigos: \n',soldadoresNovo,'\n\n')

# df.reset_index(drop=True,inplace=True) <- modifica a variável

soldadores.reset_index(drop=True,inplace=True)

print('Modificando a variavel soldadores: \n',soldadores,'\n\n')

# FAZENDO TUDO EM UMA LINHA SOMENTE!

soldadoresTemp = data.query('Designacao == "soldador"').reset_index(drop=True)

print('Modificando a variavel soldadoresTemp em somente uma linha: \n',soldadoresTemp,'\n\n')

# TOP!
# Filtragem com mais comparações, pode-se usar os operadores booleanos normalmente (& | -)
#OBS <- o query não funciona caso existam caracteres especiais!

filtragem = ((data['Designacao'] == 'soldador') & (data['Dias']>=5)) # o resultado continua sendo uma series!

data2 = data[filtragem].reset_index(drop=True) # <- resetando o indice (se necessário!)

print('Filtragem do data: \n',data2,'\n\n')

# MELHOR DESEMPENHO PARA DATA FRAMES GRANDES!

filtragem2 = (data['Designacao'] == 'soldador')

dataTemp = data[filtragem2]

filtragem3 = dataTemp['Dias']>=5

filtragem4 = filtragem2 & filtragem3

print('Filtragem 4: \n',filtragem4,'\n\n')

print('Resultado final da filtragem: \n', data[filtragem4],'\n\n')

# carregando o dataSet da aula para filtrar por anos

dataProf = pd.read_csv(r'C:\Users\889612123\Documents\GitHub\coding\dataSet\csv\GasPricesinBrazil_2004-2019.csv', sep=';')

# alternativa 1 = selecao de anos usando booleano

selecao = ((dataProf['ANO'] == 2008) | (dataProf['ANO'] == 2010) | (dataProf['ANO'] == 2012))

print('(I) - Seleção utilizando o dataSet da aula: \n\n',dataProf[selecao],'\n\n') 

# alternativa 2 = selecao de anos usando lista

listaDeAnos = [2008,2010,2012]

selecao2 = dataProf['ANO'].isin(listaDeAnos)

print('(II) - Seleção utilizando o dataSet da aula: \n\n',dataProf[selecao2],'\n\n')

# alternativa 3 = selecao de anos usando o query

dataTemp = dataProf.query('ANO in @listaDeAnos') #<- precisa di @ para comparar com uma variável

print('(III) - Seleção utilizando o dataSet da aula: \n\n',dataTemp,'\n\n')

# interando valores em conjuntos pequenos de dados

#for index, row in dataProf.head(10).iterrows():
#    print(f'indice {index} ==> {row['ESTADO']}\n\n') # <- percorrendo com um for as linhas do df

# ----------------- TRATAMENTO DE DADOS ----------------- #
    
# Preparação dos dados, tratando observações com valores vazios (null / nan) no dataSet

print('Vendo informações do dataSet: \n\n')    

dataProf.info() # verifica se existe algum valor não registrado (não nulo), str geralmente o pandas nomea como object

# verificar se o object onde deveria conter somente variaveis do tipo numérico não possui algum caracter não numérico
# verificar se há algum tipo datetime sendo visualizado como object

dataPre = dataProf.copy() # <- criando uma cópia para o pré processamento

# convertendo as datas, como os atributos de data no dataSet já estão em uma formanto de data aceitável (YYYY-MM-DD), não precisamos forçar nenhuma conversão nesse sentido e atribuindo os valores da series já em datetima64 para o dataset dataPre

a = pd.to_datetime(dataPre['DATA INICIAL']) 
b = pd.to_datetime(dataPre['DATA FINAL']) 

dataPre['DATA INICIAL'] = a
dataPre['DATA FINAL'] = b

print('Vendo informações do dataSet após a mudança para datetime64: \n\n') 

dataPre.info()

# ------------------ TOP! ------------------ #

# COLOCANDO UMA VALOR VAZIO NaN EM CASO DE ERRO DE CONVERSÃO E VERIFICANDO OS ERROS!

# convertendo atributos/colunas de str para um tipo numérico 

for atributo in ['MARGEM MÉDIA REVENDA','PREÇO MÉDIO DISTRIBUIÇÃO','DESVIO PADRÃO DISTRIBUIÇÃO','PREÇO MÍNIMO DISTRIBUIÇÃO','PREÇO MÁXIMO DISTRIBUIÇÃO','COEF DE VARIAÇÃO DISTRIBUIÇÃO']:
   dataPre[atributo] = pd.to_numeric(dataPre[atributo],errors='coerce') # errors='coerce' <- os erros serão setados como NaN

print('Vendo informações do dataSet após a mudança de str para numérico: \n\n') 

dataPre.info()

# LIMPEZA DE DADOS

# criando uma series tipo boll mask que retorna quais linhas da coluna data são NaN

mask = dataPre['PREÇO MÉDIO DISTRIBUIÇÃO'].isnull()

print('Linhas da coluna "PREÇO MÉDIO DISTRIBUIÇÃO" que são NaN: \n',mask)

# vendo os registros que são NaN conforme a máscara filtrou

print('Registros tipo NaN do dataPre: \n',dataPre[mask])

# vendo nos dados originais o que existia nesses registros que a máscara filtrou como NaN

print('Registros dos dados originais que são NaN na coluna "PREÇO MÉDIO DISTRIBUIÇÃO": \n',dataProf[mask])

df = dataProf[mask]

print('DF INFO: \n')

df.info()

print('\n\n Vendo a coluna "PREÇO MÉDIO DISTRIBUIÇÃO": \n',df['PREÇO MÉDIO DISTRIBUIÇÃO']) # <- Várias amostras possuem o a str - como elemento ao invés de um elemento numérico de fato. Ou seja, não há aferições destes atributos para essas amostras

# retorna uma cópia do df dataPre com todos os valores NaN de todas as colunas agora preenchidos com 0,  inplace = False, por enquanto para não motificar o dataPre, caso contrário inplace = True

dataPreFill = dataPre.fillna(0) 

print('Vendo a substituição dos NaN por 0: \n',dataPreFill[mask]) # <- valores que antes eram NaN agora são 0, o df original pré processado não foi alterado

# atribuindo valores ao invés de 0 para as colunas

dataPreFill = dataPre.fillna(value={
    'PREÇO MÉDIO DISTRIBUIÇÃO':10,
    'PREÇO PADRÃO DISTRIBUIÇÃO':20,
    'PREÇO MÍNIMO DISTRIBUIÇÃO':30,
    'PREÇO MÁXIMO DISTRIBUIÇÃO': 'vazio'
})

dataTemp = dataPreFill['PREÇO MÁXIMO DISTRIBUIÇÃO']

print('Atribuindo valores ao invés de 0 para as colunas: \n',dataTemp[mask])

#df.dropna(inplace=True) <- para remover todos os NaN em quaisquer colunas e atributos, alterando o próprio df

dataTemp.dropna(inplace=True)

dataPreFill.to_csv(r'C:\Users\889612123\Documents\GitHub\coding\dataSet\csv\temp.csv',index=False,encoding='utf-8-sig')

# ------------------ ESTATÍSTICAS DESCRITIVAS ------------------ #

# .describe <- exibe várias estatísticas descritivas para os atributos de um df ou para uma series

dataPreFill.describe() # visualizando para todas as colunas

print('Utilizando o .describe(): \n',dataPreFill.describe()) 

dataPreFill.describe()['PREÇO MÉDIO REVENDA'] # visualizando uma coluna inteira

print('Utilizando o .describe() em uma coluna somente: \n',dataPreFill.describe()['PREÇO MÉDIO REVENDA'],'\n\n') 

dataPreFill['PREÇO MÉDIO REVENDA'].describe() # visualizando uma series inteira

print('Utilizando o .describe() em uma series inteira: \n',dataPreFill['PREÇO MÉDIO REVENDA'].describe(),'\n\n')

# (I) retornando colunas selecionadas do df

stats = dataPreFill.describe()

print('Retornando colunas selecionadas do df: \n',stats[['PREÇO MÉDIO REVENDA','PREÇO MÁXIMO REVENDA','PREÇO MÉDIO DISTRIBUIÇÃO']])

# (II) retornando colunas selecionadas do df, OBS: MAIS RÁPIDO POIS HOUVE UMA PRÉ FILTRAGEM

stats = dataPreFill[['PREÇO MÉDIO REVENDA','PREÇO MÁXIMO REVENDA','PREÇO MÉDIO DISTRIBUIÇÃO']].describe()

print('\nRetornando colunas selecionadas de maneira mais eficiente: \n',stats)

# acessando apenas algumas estatísticas, acessando os rótulos de apenas alguns indices

# (I) acessando todas as colunas

temp = stats.loc[['min','max','mean']] 

print('Selecionando apenas alguns indices do método .describe(): \n',temp)

# acessando somente a coluna 'PREÇO MÉDIO REVENDA'
temp = stats.loc[['min','max','mean'],'PREÇO MÉDIO REVENDA']

print('Selecionando apenas alguns indices do método .describe() da coluna PREÇO MÉDIO REVENDA: \n',temp)

# acessando as coluna 'PREÇO MÉDIO REVENDA' e 'PREÇO MÉDIO DISTRIBUIÇÃO', OBS: LISTA DE INDICES E LISTA DE COLUNAS -> n.loc[[ln,ln,ln],[cl,cl,cl]]

temp = stats.loc[['min','max','mean'],['PREÇO MÉDIO REVENDA','PREÇO MÉDIO DISTRIBUIÇÃO']]

print('Selecionando apenas alguns indices do método .describe() da coluna PREÇO MÉDIO REVENDA e PREÇO MÉDIO DISTRIBUIÇÃO: \n',temp,'\n\n')

# mean, std, min, etc. cada uma das estatísticas do describe podem ser computadas individualmente

# qual o menor valor dopreço mínimo de revenda?

temp = dataProf['PREÇO MÍNIMO REVENDA'].min()

print('Menor valor do PREÇO MÍNIMO REVENDA:\n',temp)

# qual a média e desvio padrão dos preço mínimos de revenda?

mean = dataProf['PREÇO MÍNIMO REVENDA'].mean()
std = dataProf['PREÇO MÍNIMO REVENDA'].std()

print(f'\nA média dos preços mínidos de revenda é: {mean:.2f} +- {std:.2f}') # n:.2f <- quantidade de casas decimais desejadas

# quais estados são considerados? utiliza-se o método .unique()

temp =  dataProf['ESTADO'].unique() # <- não ordenado 

print('Estados considerados: \n',temp)

# PARA ORDENAR UTILIZA-SE o sorted()

temp =  sorted(dataProf['ESTADO'].unique()) # <- ordenado 

print('Estados ordenados considerados: \n',temp)

# retornando a quantidade de elementos com o .size

temp =  dataProf['ESTADO'].unique().size

print('Quantidade de estados ordenados considerados: \n',temp)

# quantos registros (aferições) cada estado possui?

temp = dataProf['ESTADO'].value_counts() # <- retorna em ordem decrescente a quantidade de registros (linhas) para cada estado

print('Quantidade de linhas cada estado possui: \n',temp)

# PODEMOS TRANFORMAR ESSA SERIES EM UM DATA FRAME

tempDf = temp.to_frame() 

tempDf.to_csv(r'C:\Users\889612123\Documents\GitHub\coding\dataSet\csv\seriesToDf.csv',encoding='utf-8-sig')

# ------------------ APLICANDO MÉTODOS EM LINHAS, COLUNAS, DF OU SERIES  ------------------ #

# execução de funções para cada item de um df ou series,uma alternativa ao for é utilizar funções próprias
# do pandas que aplicam/mapeiam uma data função a todos o elementos de um df ou series

#           | DataFrame | Series
# apply     |     X     |   X
# map       |           |   X    
# applymap  |     X     |

df = pd.DataFrame({ 'A': [1, 2, 3, 4], 
                    'B': [10, 20, 30, 40],
                    'C': [100, 200, 300, 400]}, 
                     index=['Linha 1', 'Linha 2', 'Linha 3', 'Linha 4'])
print('df: \n',df,'\n\n')

# apply() <- usado para aplicar uma função ao longo de um eixo de um df ou em valores de uma series

# axis=1 (horizontal), axis = 0 (vertical)

def nossaSoma(series): # retorna uma series que é a soma de todos os valores de uma linha
    return series.sum()

df['SOMA (A,B,C)'] = df.apply(nossaSoma,axis=1)

print('df após soma na linha: \n',df)

df.loc['Linha 5'] = df.apply(nossaSoma,axis=0) #criando uma linha nova e adicionando o resultado do método nossaSoma

print('df após soma na coluna: \n',df)

# criando uma função lambda (temporária)

df['MÉDIA (A, B e C)'] = df[['A','B','C']].apply(lambda series: series.mean(), axis=1) # <- aplicando a média para as linhas das colunas A, B e C

print('df após incluir coluna MÉDIA (A, B e C):\n',df)

# aplicar a lambda function abaixo para cada elemento da coluna

df['C*2'] = df['C'].apply(lambda x: x * 2) # <- APLICANDO O MÉTODO .apply() EM UMA SERIES!

print('df após adicionar uma nova coluna:\n',df)

# OUTRO!

df['A+2'] = df['A'] + 2

print('df após adicionar uma nova coluna com OUTRO:\n',df)

# .map() <- utilizada apenas em df, ela aplica uma função em cada elemento (element-wise) de um df

df = pd.DataFrame({ 'A': [1, 2, 3, 4], 
                    'B': [10, 20, 30, 40],
                    'C': [100, 200, 300, 400]}, 
                     index=['Linha 1', 'Linha 2', 'Linha 3', 'Linha 4'])

dfTemp = df.map(lambda x:x**2) #<- retorna uma cópia, não possui o inplace I

print('df após .map:\n',dfTemp)

nomes = pd.Series(['João','Maria','Alice','Pedro'])

nomes = nomes.map(lambda x: x.upper()) #<- retorna uma cópia, não possui o inplace II

print('nomes após .upper():\n',nomes)

# df.str.upper() <- APLICANDO UM MÉTODO PARA TODOS O ELEMENTOS DO DF (QUANDO TODOS SÃO STR)

nomes = nomes.str.lower()

print('nomes após .str.lower():\n',nomes)

# ------------------ AGRUPAMENTO  ------------------ #

# groupby.() <- usado para criar grupos de elementos baseados nos valores de um atributo (categórico).
# funções podem então ser aplicadas para os elementos de cada grupo, de modo que os resultados de cada grupo serão combinados.
# groupby.() <- VIDE DOC NO PANDAS!

grupos = dataProf.groupby('REGIÃO') # <- NÃO É UM DF, É UM AGRUPAMENTO DE AMOSTRAS DE UM DF!

print('df groups: ',grupos.groups,'\n\n')

print('df indices: ',grupos.indices,'\n\n')

print('df selecionando grupo: ',grupos.get_group('CENTRO OESTE'),'\n\n')

# podemos aplicar funções aos grupos

temp = grupos.describe()

temp.to_csv(r'C:\Users\889612123\Documents\GitHub\coding\dataSet\csv\describe2.csv',encoding='utf-8-sig')

temp = grupos.min() #< retornando somente a média para cada coluna

temp.to_csv(r'C:\Users\889612123\Documents\GitHub\coding\dataSet\csv\describe3.csv',encoding='utf-8-sig')

# FAZENDO O .groupby() E O .min() EM UMA LINHA SOMENTE!

temp = dataProf.groupby('REGIÃO').min()

temp.to_csv(r'C:\Users\889612123\Documents\GitHub\coding\dataSet\csv\describe4.csv',encoding='utf-8-sig')

grupos = dataProf.groupby(['REGIÃO','PRODUTO']) # <- PREÇO MÁXIMO DE CADA PRODUTO(COMBUSTÍVEL) PARA CADA REGIÃO DO BRASIL

media = grupos.max()

media.to_csv(r'C:\Users\889612123\Documents\GitHub\coding\dataSet\csv\media.csv',encoding='utf-8-sig')

# aplicando a media para uma coluna

media2 = grupos['PREÇO MÉDIO REVENDA'].mean()

media2.to_csv(r'C:\Users\889612123\Documents\GitHub\coding\dataSet\csv\media2.csv',encoding='utf-8-sig')

# aplicando o .describe()

describe5 = grupos['PREÇO MÉDIO REVENDA'].describe()

describe5.to_csv(r'C:\Users\889612123\Documents\GitHub\coding\dataSet\csv\describe5.csv',encoding='utf-8-sig')

# ------------------ IMPORTANTE  ------------------ #

# .agg() <- agrega(roda) ma série de funções para os elementos de um df ou de grupos de um df

df = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [None, None, None]],
                  columns=['A', 'B', 'C'])

temp = df.agg([max, min])

print('Aplicando o agg nas colunas: \n',temp,'\n\n')

# usando o .agg() em um grupo

grupos = dataProf.groupby('REGIÃO')

# computa o menor e maior valor do 'PREÇO MÉDIO REVENDA' para cada região

temp = grupos['PREÇO MÉDIO REVENDA'].agg([min,max])

print('Aplicando o agg nas colunas: \n',temp,'\n\n')

# ordenação

# .sort_values() <- ordena valores ao longo de um eixo

notas = pd.DataFrame({
    'nome': ['João', 'Maria', 'José', 'Alice'],
    'idade': [20, 21, 19, 20],
    'nota_final': [5.0, 10.0, 6.0, 10.0]
})
notas

notasOrdenadas = notas.sort_values(by='nota_final') # <- por padrão ele ordena da menor para a maior norta

print('Notas ordenadas da menor nota final para a maior: \n',notasOrdenadas,'\n\n')

notasOrdenadas = notas.sort_values(by='nota_final',ascending=False) #<- usando o ascending = False para que a ordenação seja do maior para o menor valor 

print('Notas ordenadas da menor nota final para a maior: \n',notasOrdenadas,'\n\n')

# OBS: O PANDA MANTEM O ÍNDICE ORIGINAL

# Resetando os indices

notasOrdenadasIndiceResetado = notas.sort_values(by='nota_final',ascending=False).reset_index(drop=True) 

print('Notas ordenadas com indice resetado: \n',notasOrdenadasIndiceResetado,'\n\n')

# TOP!

# criando um critério de desempate, aqui no caso das notas iguais utilizar a ordem alfabética

notasOrdenadas = notas.sort_values(by=['nota_final','nome'],ascending=[False,True]) #<- ORDENE PELA NOTA, SE IMPATAR ORDENE PELO NOME!

#OBS: ordena os registros primeiramente pela coluna 'nota_final' em ordem decrescente. Então, reordena os registros empatados em ordem alfabética (crescente)
print('Notas ordenadas com mais de um critério: \n',notasOrdenadas,'\n\n')

# PARA ALTERAR O df ORIGINAL USE O inplace=True

notas.sort_values(by=['nota_final','nome'],ascending=[False,True], inplace=True)

notas = notas.reset_index(drop=True)

print('Notas ordenadas com mais de um critério, inplace=True: \n',notas,'\n\n')

#.to_frame() <- grupos['REGIÃO'].value_counts().to_frame()

print('FIM')
