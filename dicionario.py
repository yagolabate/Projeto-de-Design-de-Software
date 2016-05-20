# -*- coding: utf-8 -*-
import pickle

arquivo = open("projeto.pickle", "rb")
dados_salvos = pickle.load(arquivo)
arquivo.close()

class dicionario:
    def __init__(self):

        self.dici = {}
