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

#Leitura de dados
dados = planilha.get_all_values()[:17]

pd.set_option('display.max_rows', None)
df = pd.DataFrame(dados[1:], columns=dados[0])
with pd.option_context('display.max_rows', None):
    print(df.to_string(index=False))
produto1 = df.loc[5, 'DESCRIÇÃO']

#MPORTAÇÃO DO SELENIUM PARA PESQUISA EM ALGUM SITE
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

#PESQUISAR OS PRODUTOS EM ALGUM LUGAR
driver.get("https://www.mercadolivre.com.br/")
input_element = driver.find_element(By.CSS_SELECTOR, 'input#cb1-edit')
input_element.send_keys(f"{produto1}")
input_element.send_keys(Keys.RETURN)
nome = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/ol/li[1]/div/div/div[2]/div[1]/a/h2').text
valor1 = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/ol/li[1]/div/div/div[2]/div[2]/div[1]/div/div/div/div/span[1]/span[2]/span[1]').text
valor2 = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/ol/li[1]/div/div/div[2]/div[2]/div[1]/div/div/div/div/span[1]/span[2]/span[2]').text
valor3 = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/ol/li[1]/div/div/div[2]/div[2]/div[1]/div/div/div/div/span[1]/span[2]/span[3]').text
valor4 = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/ol/li[1]/div/div/div[2]/div[2]/div[1]/div/div/div/div/span[1]/span[2]/span[4]').text

driver.quit()
valor_final = f'{valor1} {valor2}{valor3}{valor4}'
print(nome)
print(valor_final)
#MERCADO LIVRE
#TENTAR MESCLAR SELENIUM COM PYAUTOGUI PARA FAZER A PESQUISA NO MERCADO LIVRE


#RETIRAR O VALOR DOS PRODUTOS
#JOGAR NA PLANILHA
#ANALISAR DADOS COLETADOS


#https://lista.mercadolivre.com.br/l%C3%A1pis-cor-color-case-c%2F-12-cores-%C3%BE-estojo-%C3%BE-apontador-c%2F-dep%C3%B3sito-cis#D[A:L%C3%A1pis%20Cor%20Color%20Case%20c/%2012%20Cores%20+%20Estojo%20+%20Apontador%20c/%20Dep%C3%B3sito%20-%20CIS]


