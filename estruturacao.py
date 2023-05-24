#ACESSAR PLANILHA COM OS PRODUTOS
import gspread
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials

# Configuração das credenciais
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\positivo\\Documents\\python\\projeto_mae\\projeto-mae-387416-f90f9773ee1f.json', scope)

# Autenticação
client = gspread.authorize(credentials)

# Abertura da planilha
planilha = client.open('pesquisa_fornecedores_teste').sheet1


# Exemplo de operação: leitura de dados
dados = planilha.get_all_values()[:17]

pd.set_option('display.max_rows', None)
df = pd.DataFrame(dados[1:], columns=dados[0])
with pd.option_context('display.max_rows', None):
    print(df.to_string(index=False))

#PESQUISAR OS PRODUTOS EM ALGUM LUGAR
#MERCADO LIVRE
produto1 = df.loc[5, 'DESCRIÇÃO']

#TENTAR MESCLAR SELENIUM COM PYAUTOGUI PARA FAZER A PESQUISA NO MERCADO LIVRE

print(produto1)
#RETIRAR O VALOR DOS PRODUTOS
#JOGAR NA PLANILHA
#ANALISAR DADOS COLETADOS


https://lista.mercadolivre.com.br/l%C3%A1pis-cor-color-case-c%2F-12-cores-%C3%BE-estojo-%C3%BE-apontador-c%2F-dep%C3%B3sito-cis#D[A:L%C3%A1pis%20Cor%20Color%20Case%20c/%2012%20Cores%20+%20Estojo%20+%20Apontador%20c/%20Dep%C3%B3sito%20-%20CIS]


