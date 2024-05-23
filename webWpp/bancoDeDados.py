from typing import List
import json
from supabase import create_client
from unidecode import unidecode

class processarMsm:
    def __init__(self, id_loja, msm):
        self.url = "https://odtsaxxshxzdatavzftv.supabase.co"
        self.chave_api = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9kdHNheHhzaHh6ZGF0YXZ6ZnR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE0OTYzNDMsImV4cCI6MjAyNzA3MjM0M30.04XvHLUvjkIdsmu5keJGbUL88DAp97H5bE_a06DdpW4"
        self.cliente_supabase = create_client(self.url, self.chave_api)
        self.id_loja=id_loja
        self.msm=msm
        self.neuronio_2(self.neuronio_1(msm))




    #Primeira Camada Selecao

    def neuronio_1(self, msm):
        msm=unidecode(msm.replace(' ','').lower())
        pesos={
            'cardapio': 0,
            'novaMensagem':0,
            'comprarProduto':0
        }
        # Seleção de cardápio
        if 'cardapio' in msm or 'site' in msm:
            pesos['cardapio']=10

        if 'oi' in msm or 'ola' in msm or 'boanoite' in msm:
            pesos['novaMensagem']=2

        for produto in self.buscar_produtos_por_id_loja(self.id_loja, 'nome'):
            if unidecode(produto) in msm:
                pesos['comprarProduto']=10


        return [pesos, msm]

    def neuronio_2(self, neuronio_1):
        peso_maior=['', 0]
        for peso in neuronio_1[0].items():
            if peso[1]>peso_maior[1]:
                peso_maior[1]=peso[1]
                peso_maior[0] = peso[0]
        if peso_maior[1]=='cardapio':
            return 'Entre aqui para ver nosso cardápio'
        elif peso_maior[1]=='novaMensagem':
            return 'Olá, como posso ajudar hoje?'
        elif peso_maior[1]=='comprarProduto':
            return 'Compre Esse produto Diretamente Por esse link'







        ###### Métodos Auxiliares  ######


    def buscar_produtos_por_id_loja(self, id_loja, campo) -> List[dict]:
        if self.pegar_status_loja(id_loja)[0]:
            produtos_str = []
            resposta = self.cliente_supabase.from_("produtos").select("*").eq('id_loja', id_loja).execute()
            for produto in self.tratarSupabae(resposta):
                produtos_str.append(produto[campo].replace(' ', '').lower())

            return produtos_str
        else:
            return [self.pegar_status_loja(id_loja)[1]]

    def pegar_status_loja(self, id_loja: int) -> str:
        resposta = self.cliente_supabase.from_("loja").select("status").eq('id', id_loja).execute()
        resposta = self.tratarSupabae(resposta)[0]['status'].replace(' ', '')
        if 'false' in resposta:
            return [False, 'Loja Fechada']
        else:
            return [True, 'Loja Aberta']


    def tratarSupabae(self, resposta):
        string_json = str(resposta).replace("'", "\"").replace('data=', '').replace(' count=None', '')
        return json.loads(string_json)





