import pandas as pd
import streamlit as st
from jogo import ListJogos


def tab_torneio(jogos: ListJogos):
    torneios = jogos.lista
    torneios.sort(key=lambda x: x.tipo)
    torneios = [{'data': item.data, 'modalidade': item.tipo} for item in torneios]
    torneios = [dict(t) for t in {tuple(d.items()) for d in torneios}]
    for torneio in torneios:
        lista_torneio = [item for item in jogos.lista if item.data == torneio["data"]
                         and item.tipo == torneio["modalidade"]]
        lista_torneio.sort(key=lambda x: x.posicao)
        st.write(f'Torneio de {torneio["modalidade"]} Data {torneio["data"]}')
        jogador = []
        pontos = []
        vpg = []
        vj = []
        vjg = []
        for linha in lista_torneio:
            jogador.append(linha.jogador)
            pontos.append(linha.pontos)
            vpg.append(linha.vpg)
            vj.append(linha.vj)
            vjg.append(linha.vjg)
        final = {
            'jogador': jogador,
            'pontos': pontos,
            'vpg': vpg,
            'vj': vj,
            'vjg': vjg
        }
        st.dataframe(pd.DataFrame(final, index=range(1, len(jogador)+1)))
