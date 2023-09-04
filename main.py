import streamlit as st
from banco import get_all_jogos
from login import check_login
from tab_inserir import tab_inserir
from tab_rank import tab_rank
from tab_torneios import tab_torneio

if check_login():
    st.set_page_config(layout="wide", page_title="Rank")

    jogos = get_all_jogos()

    if st.session_state['login'] == 'visitante':
        tabs = st.tabs(
            ['Rank', 'Torneios'])
        with tabs[0]:
            tab_rank(jogos)
        with tabs[1]:
            tab_torneio(jogos)
    else:
        tabs = st.tabs(
            ['Inserir Novo Torneio', 'Rank', 'Torneios'])
        with tabs[0]:
            tab_inserir(jogos)
        with tabs[1]:
            tab_rank(jogos)
        with tabs[2]:
            tab_torneio(jogos)
