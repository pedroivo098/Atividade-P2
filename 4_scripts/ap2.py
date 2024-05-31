#Pedor Ivo					            RA:2303212
#Vitor Barroso			        		RA:2301249
import pandas as pd
import sqlalchemy as sqa
import streamlit as st 
import numpy as np
import plotly.express as px

st.write('***LoL***')

#Código da logo
st.logo('Bee_Mad_Emote.png')

#Estrutura do toggle
st.write('Escolha um:')
t = st.toggle('Gráficos', value=0)
t2 = st.toggle('Informações por campeão', value=0)
t3 = st.toggle('DataFrame Completo', value=0)

#Leitura do Banco para o DataFrame
engine = sqa.create_engine("sqlite:///dflol.db", echo=True)
conn = engine.connect()
dados = pd.read_csv('../1_bases_tratadas/dados_tratados_atividade.csv',sep=';')
df = pd.DataFrame(dados)

#Código dos gráficos
if t:
    vi = st.sidebar.checkbox("Visualizar o DataFrame Completo")
    if vi:
        dfbd = pd.read_csv('../1_bases_tratadas/dados_tratados_atividade.csv',sep=';')
        st.dataframe(dfbd,hide_index=1)

    dfnome = df['Nome']
    dfnome = dfnome.sort_values(ignore_index=0, ascending=1)
    dfama = df['AMA']
    dfnome = pd.concat([dfnome, dfama], axis=1)
    st.sidebar.header('Nome dos campeões e seus AMA:')
    st.sidebar.dataframe(dfnome, hide_index=1)
    dftx = df['Taxa de Vitoria']
    dftx = pd.concat([dftx, dfnome], axis=1)
    dftx = dftx.sort_values(by='Taxa de Vitoria', ignore_index=0, ascending=0)
    st.write('Clique para ampliar.')
    graftx = st.scatter_chart(dftx,x='Nome',y='Taxa de Vitoria', color='#00ff00', use_container_width=True)
    

    dfama = df['AMA']
    grafama = px.box(df, x = 'AMA')
    st.plotly_chart(grafama)

    dfnome = df['Nome'].drop_duplicates()
    dfdano = df['Dano Causado']
    dfdano = pd.concat([dfdano, dfnome], axis=1)
    dfdano = dfdano.sort_values(by='Nome', ignore_index=1, ascending=1)
    st.write('Clique para ampliar.')
    grafdano = px.bar(dfdano, x='Nome', y='Dano Causado',color='Nome')
    st.plotly_chart(grafdano)


    dfnome = df['Nome']
    dfnome = dfnome.sort_values(ignore_index=0, ascending=1)
    dfouro = df['Ouro Recebido']
    dfouro = dfouro.sort_values()
    dfouro = pd.concat([dfouro, dfnome], axis=1)
    dfouro = dfouro.sort_values(by='Ouro Recebido', ignore_index=0, ascending=0)
    st.write('Clique para ampliar.')
    grafouro = st.bar_chart(dfouro,x='Nome', y='Ouro Recebido', color='#ffff00')

#Código das informações por campeão
elif t2:
    vi = st.sidebar.checkbox("Visualizar o DataFrame Completo")
    if vi:
        dfbd = pd.read_csv('../1_bases_tratadas/dados_tratados_atividade.csv',sep=';')
        st.dataframe(dfbd,hide_index=1)

    st.sidebar.header('Escolha um campeão:')
    champ = df['Nome'].drop_duplicates()
    champ = champ.sort_values()
    escolha_champ = st.sidebar.selectbox( '',champ) 
    df2 = df[df['Nome']==escolha_champ]
    st.write(f'Taxa de Vitória {escolha_champ}:')
    st.dataframe(df2, hide_index=1)
#Código do DataFrame Completo  
elif t3:
<<<<<<< HEAD
    dfbd = pd.read_csv('../1_bases_tratadas/dados_tratados_atividade.csv',sep=';')
    st.dataframe(dfbd,hide_index=1)
=======
    dfbd = pd.read_sql('dflol.db', con=conn)
    st.dataframe(dfbd,hide_index=1)
>>>>>>> 519dedcea36a39df6432bae7a77ef722ac86ef3a
