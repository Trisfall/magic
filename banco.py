import sqlite3
from jogo import Jogo, JogoCreate, ListJogos


def create_table():
    with sqlite3.Connection('torneio.db') as db:
        db.cursor().execute("""
        CREATE TABLE IF NOT EXISTS resultado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            tipo TEXT NOT NULL,
            jogador TEXT NOT NULL,
            posicao INTEGER NOT NULL,
            pontos INTEGER NOT NULL,
            vpg INTEGER NOT NULL,
            vj INTEGER NOT NULL,
            vjg INTEGER NOT NULL,
            tamanho TEXT NOT NULL
        )
        """)


def inserir_jogo(jogo: JogoCreate):
    with sqlite3.Connection('torneio.db') as db:
        campos = list()
        campos.append('data')
        campos.append('tipo')
        campos.append('jogador')
        campos.append('posicao')
        campos.append('pontos')
        campos.append('vpg')
        campos.append('vj')
        campos.append('vjg')
        campos.append('tamanho')
        command = f'INSERT INTO resultado ({",".join(campos)}) VALUES ({ ",".join(["?"]*len(campos)) })'
        variables = (jogo.data, jogo.tipo, jogo.jogador, jogo.posicao,
                     jogo.pontos, jogo.vpg, jogo.vj, jogo.vjg, jogo.tamanho)
        db.cursor().execute(command, variables)
        db.commit()


def deletar_jogo(jogo_id: int):
    with sqlite3.Connection('torneio.db') as db:
        command = 'DELETE FROM resultado WHERE id = ?'
        variables = (jogo_id,)
        db.cursor().execute(command, variables)
        db.commit()


def get_all_jogos():
    with sqlite3.Connection('torneio.db') as db:
        result = list()
        for elemento in db.cursor().execute('SELECT * FROM resultado').fetchall():
            result.append(Jogo(id=elemento[0],
                               data=elemento[1],
                               tipo=elemento[2],
                               jogador=elemento[3],
                               posicao=elemento[4],
                               pontos=elemento[5],
                               vpg=elemento[6],
                               vj=elemento[7],
                               vjg=elemento[8],
                               tamanho=elemento[9]))
        return ListJogos(lista=result)
