import streamlit as st
import re
from datetime import date
from jogo import JogoCreate, ListJogos
from banco import deletar_jogo, inserir_jogo, get_all_jogos


def validacoes(texto: str, data: str):
    if not data:
        st.error('Escreva a data do torneio.')
        return False
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', data):
        st.error('Escreva a data de acordo com o exemplo dado.')
        return False
    if not texto:
        st.error('Insira os dados do torneio de acordo com o modelo ao lado.')
        return False
    dados = [item for item in texto.split('\n') if item != '']
    if len(dados) < 8:
        st.error('O torneio precisa ter 8 ou mais jogadores para ser cadastrado.')
        return False
    for dado in dados:
        sub = dado.split(' ')
        if len(sub) < 2:
            st.error('Não possui o número de colunas pedido.')
            return False
        elif not sub[0][0].isdigit() or sub[0][0] == '0':
            st.error('A primeira coluna deve ter números de 1 a X')
            return False
    return True


def substituir_torneio(data: str, jogos: ListJogos):
    jogos_dessa_data = [jogo for jogo in jogos.lista if jogo.data == data]
    for jogo in jogos_dessa_data:
        deletar_jogo(jogo.id)


def gravar_torneio(texto: str, data: str, tipo: str):
    dados = [item for item in texto.split('\n') if item != '']
    pattern = r'(\d+)\s+([^\d]+)(\d+)\s+(\d{2})\s+(\d{2})\s+(\d{2})'
    for dado in dados:
        if re.match(pattern, dado):
            match = re.search(pattern, dado)
            lista = match.groups()
            novo = JogoCreate(data=data,
                              tipo=tipo,
                              jogador=lista[1].strip(),
                              posicao=int(lista[0]),
                              pontos=int(lista[2]),
                              vpg=int(lista[3]),
                              vj=int(lista[4]),
                              vjg=int(lista[5]))
        else:
            lista = dado.split(' ')
            novo = JogoCreate(data=data,
                              tipo=tipo,
                              jogador=' '.join(lista[1:]).strip(),
                              posicao=int(lista[0]),
                              pontos=0,
                              vpg=0,
                              vj=0,
                              vjg=0)
        inserir_jogo(novo)


def tab_inserir(jogos: ListJogos):
    columns = st.columns(2)
    with columns[0]:
        st.write('A data deve ser escrita da seguinte maneira, Exemplo: 01/12/2023')
        st.write('''
            Exemplo de Input para Novo Torneio:\n
            "1 Jogador A 10 60 75 58\n
             2 Jogador B 10 58 66 58\n
             3 Jogador C 9 60 70 56\n
             4 Jogador D 9 47 60 47"\n
        ''')
        st.write('Primeira coluna é a posição do Jogador')
        st.write('Segunda coluna é o nome do Jogador separado por espaços, o nome não deve possuir números')
        st.write('Terceira coluna é são os pontos do jogador naquele torneio')
        st.write('Quarta coluna é a %VPG')
        st.write('Quinta coluna é a %VJ')
        st.write('Sexta coluna é a %VJG')
        st.write('As 2 primeiras colunas são obrigatórias, o restante se não passado é considerado 0.')
    with columns[1]:
        hoje = str(date.today()).split('-')
        hoje.reverse()
        st.text_input(key='input_data', label='Data do Torneio', value='/'.join(hoje))
        st.selectbox(key='input_tipo', label='Torneio', options=('Modern', 'T2', 'Pionner', 'Pauper'))
        st.text_area(key='input_torneio', label='Inserir Novo Torneio')
        if st.button('salvar'):
            texto = st.session_state['input_torneio'].strip()
            data = st.session_state['input_data'].strip()
            if validacoes(texto, data):
                substituir_torneio(data, jogos)
                gravar_torneio(texto, data, st.session_state['input_tipo'])
                jogos.lista = get_all_jogos().lista
                st.success('Inserido')
