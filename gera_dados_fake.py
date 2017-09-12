#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
import json
def gera_usuarios_prestador_pf():
    """
    Gera usuarios pretador pf
    """
    PRIMEIRO_NOME = [
        "Marcos", "Roberto", "Antonio", "Joao", "Maria", "Paulo", "Paula", "Marcio",
        "Germana", "Patricia", "Reno", "Levi", "Samuel", "Julia", "Cristiano",
        "Marcelo", "Ana", "Beatriz", "Juliana"
    ]

    SEGUNDO_NOME = [
        "Oliveira", "Silva", "Santos", "Barreto", "Ribeiro", "Rocha", "Fernandes",
        "Vasconcelos", "Gomes"
    ]

    DIAS_VENCIMENTO = [5, 10, 15, 20, 25, 30]
    DIAS_MES = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
        18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
    ]
    MES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    IN_PAG_DIA = ["S", "S", "S", "S", "N"]

    usuarios = []
    for i in range(2,51):
        primeiro_nome = PRIMEIRO_NOME[randint(0, len(PRIMEIRO_NOME) - 1)]
        segundo_nome = SEGUNDO_NOME[randint(0, len(SEGUNDO_NOME) - 1)]
        indice_foto = randint(1,4)
        dia_vencimento = DIAS_VENCIMENTO[randint(0, len(DIAS_VENCIMENTO) - 1)]
        dia_do_cadastro = DIAS_MES[randint(0, len(DIAS_MES) - 1)]
        mes_do_cadastro = MES[randint(0, len(MES) -1)]
        in_pag_em_dia = IN_PAG_DIA[randint(0, len(IN_PAG_DIA) - 1)]
        usuarios.append(
            {
                "id": i,
                "nome": primeiro_nome + " " + segundo_nome,
                "email": primeiro_nome.lower() + "." + segundo_nome.lower() + "@mail.com",
                "senha": "senha",
                "tipo": "Prestador",
                "endereco": "Rua 1 casa 6, Centro",
                "cidade": "Sobral",
                "cep": "62.040-750",
                "telefoneFixo1": "88-3677-1407",
                "telefoneFixo2": "88-3611-1111",
                "celuliar1": "99999-99999",
                "celular2": "99999-8888",
                "foto": "/assets/foto" + str(indice_foto) + ".PNG",
                "situacao": "ativo",
                "in_pf_pj": "PF",
                "CPF": "111.111.111-11",
                "CNPJ": ""
            }
        )
    return usuarios

def gera_usuarios_consumidor_pf():
    """
    Gera usuarios consumidor pf
    """
    PRIMEIRO_NOME = [
        "Marcos", "Roberto", "Antonio", "Joao", "Maria", "Paulo", "Paula", "Marcio",
        "Germana", "Patricia", "Reno", "Levi", "Samuel", "Julia", "Cristiano",
        "Marcelo", "Ana", "Beatriz", "Juliana"
    ]

    SEGUNDO_NOME = [
        "Oliveira", "Silva", "Santos", "Barreto", "Ribeiro", "Rocha", "Fernandes",
        "Vasconcelos", "Gomes"
    ]

    DIAS_VENCIMENTO = [5, 10, 15, 20, 25, 30]
    DIAS_MES = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
        18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
    ]
    MES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    IN_PAG_DIA = ["S", "S", "S", "S", "N"]

    usuarios = []
    for i in range(51,101):
        primeiro_nome = PRIMEIRO_NOME[randint(0, len(PRIMEIRO_NOME) - 1)]
        segundo_nome = SEGUNDO_NOME[randint(0, len(SEGUNDO_NOME) - 1)]
        indice_foto = randint(1,4)
        dia_vencimento = DIAS_VENCIMENTO[randint(0, len(DIAS_VENCIMENTO) - 1)]
        dia_do_cadastro = DIAS_MES[randint(0, len(DIAS_MES) - 1)]
        mes_do_cadastro = MES[randint(0, len(MES) -1)]
        in_pag_em_dia = IN_PAG_DIA[randint(0, len(IN_PAG_DIA) - 1)]
        usuarios.append(
            {
                "id": i,
                "nome": primeiro_nome + " " + segundo_nome,
                "email": primeiro_nome.lower() + "." + segundo_nome.lower() + "@mail.com",
                "senha": "senha",
                "tipo": "Consumidor",
                "endereco": "Rua 1 casa 6, Centro",
                "cidade": "Sobral",
                "cep": "62.040-750",
                "telefoneFixo1": "88-3677-1407",
                "telefoneFixo2": "88-3611-1111",
                "celuliar1": "99999-99999",
                "celular2": "99999-8888",
                "foto": "/assets/foto" + str(indice_foto) + ".PNG",
                "situacao": "ativo",
                "in_pf_pj": "PF",
                "CPF": "111.111.111-11",
                "CNPJ": ""
            }
        )
    return usuarios

def gera_servicos_prestados():
    """
    Gera servicos prestados
    """
    SERVICO = [1, 2, 3, 4, 5, 6, 7]
    DESCRICOES = [
        "Instalaçoes elétricas prediais e residenciais",
        "Serviçoes de cuidados com crianças",
        "Seviçoes contábeis e administração de pagamentos de impostos",
        "Seviços Advocatícios. Todos os tipos de causa.",
        "Corte de cabelo tradicional e personalizado estilo Neymar",
        "Aulas particulares a domicílio",
        "Desenvolvimento de software web e mobile. Linguagens C, Java, Python e Javascript"
    ]
    servicos_cadastrados = []
    cd = 1
    for i in range(2,51):
        usuario_id = i
        for j in range(1,4):
            servico_id = randint(1, 7)
            servicos_cadastrados.append(
                {
                    "id": cd,
                    "usuario_id": usuario_id,
                    "servico_id": servico_id,
                    "descricao": DESCRICOES[servico_id - 1]
                }
            )
            cd = cd + 1
    return servicos_cadastrados
 
def gerar_anuncios():
    """
    Gerar anuncios.
    """
    anuncios = []
    for i in range(1,148):
        anuncios.append(
            {
                "id": i,
                "servico_cadastrado_id": i,
                "in_exibir": "N"
            }
        )
    return anuncios

def gera_json(lista, arquivo):
    """
    Gera josn
    """
    arquivo = open(arquivo, "w")
    json.dump(lista, arquivo, indent=4, sort_keys=True)

if __name__  == "__main__":
    #l = gera_usuarios_prestador_pf()
    #l = gera_usuarios_consumidor_pf()
    #l = gera_servicos_prestados()
    l = gerar_anuncios()
    gera_json(l, "usuarios.json")