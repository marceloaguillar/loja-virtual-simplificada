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
planilha = client.open('pesquisa_fornecedores_teste')
pagina2 = planilha.get_worksheet(1)

dados2 = pagina2.get_all_values()[:17]

df2 = pd.DataFrame(dados2[1:], columns=dados2[0])
pd.set_option('display.max_rows', None)
print(df2)
produto1 = df2.loc[7, 'DESCRIÇÃO']
marca1 = df2.loc[7, 'MARCA']
descricao = df2['DESCRIÇÃO'].tolist()
produto_nome = f'{produto1} {marca1}'

print('\n',produto_nome,'\n')

#PESQUISA NO MERCADO LIVRE
url_padrao = 'https://lista.mercadolivre.com.br/'
response = requests.get(url_padrao + produto_nome)
site = BeautifulSoup(response.text, 'html.parser')
produtos = site.findAll('div', attrs={'class': 'ui-search-result__wrapper'})
palavras_evitadas = ['2 em 1', 'Kit', 'C/', '+',]
carrinho = []
#PESQUISA E COLETA DE DADOS DOS PRODUTOS
contador = 0
for produto in produtos:
    if contador == 20:
        break
    titulo_principal = produto.find('a', attrs={'class': 'ui-search-item__group__element shops__items-group-details ui-search-link'})
    titulo = titulo_principal.find('h2').text.strip()
    link = produto.find('a', attrs={'class': 'ui-search-link'})
    preco_principal = produto.find('div', attrs={'class': 'ui-search-price__second-line shops__price-second-line'})
    valor = preco_principal.find('span', attrs={'class': 'price-tag-fraction'}).text
    centavos = preco_principal.find('span', attrs={'class': 'price-tag-cents'})


    
    palavras_pesquisa = produto_nome.split()
    for item in palavras_pesquisa:
        if item in titulo:
            print(titulo)
            if (centavos): #ISSO SIGNIFICA QUE SE O 'CENTAVOS' NÃO FOR NONE
                print(f'R$ {valor},{centavos.text}')
                valor_final = f'R$ {valor},{centavos.text}'
                carrinho.append({titulo: valor_final})
            else:
                print(f'R$ {valor}')
                carrinho.append({titulo: f'R$ {valor},00'})
            
            contador += 1

        else:
            continue
            


        print('\n')

    #MELHORAR O MODO DE PESQUISA, TALVE CRIAR UM NOVO FILTRO PARA O DICIONARIO CARRINHO, EXCLUINDO OS ITENS COM AS PALAVRAS EVITADAS
    #MANTENDO UMA EXTRAÇÃO DE 20 ITENS, PODE SER UMA MARGEM BOA PARA APÓS O FILTRO MANTER OS 10 ITENS NECESSÁRIOS


print(carrinho)


