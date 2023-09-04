from pydantic import BaseModel


class Jogo(BaseModel):
    id: int
    data: str
    tipo: str
    jogador: str
    posicao: int
    pontos: int
    vpg: int
    vj: int
    vjg: int


class JogoCreate(BaseModel):
    data: str
    tipo: str
    jogador: str
    posicao: int
    pontos: int
    vpg: int
    vj: int
    vjg: int


class ListJogos(BaseModel):
    lista: list[Jogo]


class Rank(BaseModel):
    jogador: str
    tops: int
