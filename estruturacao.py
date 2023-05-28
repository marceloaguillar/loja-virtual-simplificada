import requests
from bs4 import BeautifulSoup

#ACESSAR PLANILHA COM OS PRODUTOS
import gspread
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials

#CREDENCIAIS GOOGLE DRIVE
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\positivo\\Documents\\python\\projeto_mae\\projeto-mae-387416-f90f9773ee1f.json', scope)
client = gspread.authorize(credentials)


#LEITURA DOS DADOS
planilha = client.open('produtos_preco')
pagina2 = planilha.get_worksheet(1)
dados2 = pagina2.get_all_values()[:17]
df2 = pd.DataFrame(dados2[1:], columns=dados2[0])
pd.set_option('display.max_rows', None)
print(df2)
descricao = df2['PRODUTO'].tolist()

#PESQUISA NO MERCADO LIVRE
n = 0
url_padrao = 'https://lista.mercadolivre.com.br/'
for pesquisa in descricao:
    c= 1
    response = requests.get(url_padrao + pesquisa)
    site = BeautifulSoup(response.text, 'html.parser')
    produtos = site.findAll('div', attrs={'class': 'ui-search-result__wrapper'})
    palavras_evitadas = ['Edição Especial', 'Case', 'Pronta Entrega', '+', 'Zelda', 'Mario', 'Kit', 'Adesivo', 'FIFA', 'God', 'Jogo', 'Capa', 'Pulseira','Película','Pelicula']
    
    #PESQUISA E COLETA DE DADOS DOS PRODUTOS
    contador = 0
    for produto in produtos:
        if contador == 10:
            break
        titulo_principal = produto.find('a', attrs={'class': 'ui-search-item__group__element shops__items-group-details ui-search-link'})
        titulo = titulo_principal.find('h2').text.strip()
        link = produto.find('a', attrs={'class': 'ui-search-link'})
        preco_principal = produto.find('div', attrs={'class': 'ui-search-price__second-line shops__price-second-line'})
        valor = preco_principal.find('span', attrs={'class': 'price-tag-fraction'}).text
        centavos = preco_principal.find('span', attrs={'class': 'price-tag-cents'})


        
        palavras_pesquisa = pesquisa.split()
        for item in palavras_pesquisa: #FILTRO DE RESULTADOS
            if item in titulo:
                if (centavos): #ISSO SIGNIFICA QUE SE O 'CENTAVOS' NÃO FOR NONE
                    valor_final = f'R$ {valor},{centavos.text}'
                    
                else:
                    valor_final = f'R$ {valor},00'
                    
            else:
                continue
                
        contador += 1
        df2.loc[n, f'VALOR {c}'] = valor_final #ADICIONAR NA TABELA
        c += 1
        if c == 6:
            break 
    n += 1
        

print(df2)


    



#MANTENDO UMA EXTRAÇÃO DE 20 ITENS, PODE SER UMA MARGEM BOA PARA APÓS O FILTRO MANTER OS 10 ITENS NECESSÁRIOS
#MELHORAR O MODO DE PESQUISA, TALVE CRIAR UM NOVO FILTRO PARA O DICIONARIO CARRINHO, EXCLUINDO OS ITENS COM AS PALAVRAS EVITADAS
#ADICIONAR DADOS A TABELA 
#CRIAR UMA BASE DE DADOS QUE PEGA AS PALAVRAS NÃO COMUNS DAS PESQUISA E 
#COLOCA NUMA BASE DE DADOS, COMO PALAVRAS EVITADAS, E AO PESQUISAR NOVAMENTE, ELE USA COMO FILTRO ESSA BASE DE DADDOS



