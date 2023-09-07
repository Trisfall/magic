import pandas as pd
import streamlit as st
from jogo import ListJogos, Rank


def tab_rank(jogos: ListJogos):
    opcoes = ('Todos', 'Modern', 'T2', 'Pionner')
    corte = st.selectbox(key='input_top', label='Selecione o corte (Ex. Top 4):', options=(4, 2, 8, 16, 32))
    tipo = st.selectbox(key='input_modalidade', label='Selecione o formato:', options=opcoes)

    dados = [item for item in jogos.lista if item.posicao <= corte and (tipo == 'Todos' or tipo == item.tipo)]

    final = {}

    for dado in dados:
        if dado.jogador in final:
            final[dado.jogador] += 1
        else:
            final[dado.jogador] = 1

    lista = []
    for key, valor in final.items():
        if key != '[REDACTED] [REDACTED]':
            lista.append(Rank(jogador=key, tops=valor))

    lista.sort(key=lambda x: x.tops, reverse=True)

    jogadores = []
    tops = []
    for elemento in lista:
        jogadores.append(elemento.jogador)
        tops.append(elemento.tops)

    st.dataframe(pd.DataFrame({
        'Jogadores': jogadores,
        'Tops': tops
    }))
