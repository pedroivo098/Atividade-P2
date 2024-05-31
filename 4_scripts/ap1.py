import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by  import By
import time as tm
import missingno as msno
import numpy as np
import math
import statistics
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import warnings
import sqlalchemy as sqa
import streamlit as st 
warnings.filterwarnings('ignore')

navegador = webdriver.Chrome()

navegador.maximize_window()

navegador.get('https://www.lolvvv.com/pt')

navegador.find_element(By.XPATH, '//*[@id="__next"]/div/nav/div/a[2]').click()
tm.sleep(3)

#navegador.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/table/thead/tr/th[3]').click()
#tm.sleep(3)

nome = navegador.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/table/tbody/tr[1]/td[2]/a/div[2]/div').text
taxa = navegador.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/table/tbody/tr[1]/td[3]/span').text
ama = navegador.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/table/tbody/tr[1]/td[6]/div').text
dano = navegador.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/table/tbody/tr[1]/td[8]').text
ouro = navegador.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/table/tbody/tr[1]/td[10]').text

lista_vazia_nome = []
for i in range(1, 101):
    nomes = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/table/tbody/tr['+str(i)+']/td[2]/a/div[2]/div').text
    lista_vazia_nome.append(nomes)
print(lista_vazia_nome)

df = pd.DataFrame(lista_vazia_nome, columns=['Nome'])

lista_vazia_taxa= []
for i in range(1, 101):
    taxas = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/table/tbody/tr['+str(i)+']/td[3]/span').text
    lista_vazia_taxa.append(taxas)
print(lista_vazia_taxa)

df['Taxa de Vitoria'] = lista_vazia_taxa

lista_vazia_AMA= []
for i in range(1, 101):
    AMA = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/table/tbody/tr['+str(i)+']/td[6]/div').text
    lista_vazia_AMA.append(AMA)
print(lista_vazia_AMA)

df['AMA'] = lista_vazia_AMA

lista_vazia_dano= []
for i in range(1, 101):
    DANO = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/table/tbody/tr['+str(i)+']/td[8]').text
    lista_vazia_dano.append(DANO)
print(lista_vazia_dano)

df['Dano Causado'] = lista_vazia_dano

lista_vazia_ouro= []
for i in range(1, 101):
    OURO = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/table/tbody/tr['+str(i)+']/td[10]').text
    lista_vazia_ouro.append(OURO)
print(lista_vazia_ouro)

df['Ouro Recebido'] = lista_vazia_ouro

df.to_csv('../0_bases_originais/dados_originais_atividade.csv', sep= ';', index = False, encoding='UTF-8')
df['Taxa de Vitoria'] = df['Taxa de Vitoria'].str.replace('%', '').str.replace(',', '.').str.replace(' ','')
df['Taxa de Vitoria'].astype(float)

df['AMA'] = df['AMA'].str.replace(',', '.').str.replace(' ', '').str.replace('Perfeito', '10')
df['AMA'].astype(float)

df['Dano Causado'] = df['Dano Causado'].str.replace(',', '.').str.replace(' ', '').str.replace('mil', '')
df['Dano Causado'].astype(float)

df['Ouro Recebido'] = df['Ouro Recebido'].str.replace(',', '.').str.replace(' ', '').str.replace('mil', '')
df['Ouro Recebido'].astype(float)

df.to_csv('../1_bases_tratadas/dados_tratados_atividade.csv', sep=';', index = False, encoding='UTF-8')

engine = sqa.create_engine("sqlite:///dflol.db", echo=True)
conn = engine.connect()

df.to_sql('dflol.db', con=conn, if_exists='replace', index=0)
df1 = pd.read_sql('dflol.db', con=conn)
st.write("DataFrame com os arquivos salvos no banco:")
st.dataframe(df1)