from typing import List
import json
from supabase import create_client
from unidecode import unidecode

class processarMsm:
    def __init__(self, id_loja=1):
        self.url = "https://odtsaxxshxzdatavzftv.supabase.co"
        self.chave_api = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9kdHNheHhzaHh6ZGF0YXZ6ZnR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE0OTYzNDMsImV4cCI6MjAyNzA3MjM0M30.04XvHLUvjkIdsmu5keJGbUL88DAp97H5bE_a06DdpW4"
        self.cliente_supabase = create_client(self.url, self.chave_api)
        self.id_loja=id_loja




    #Primeira Camada Selecao

    def neuronio_1(self, msm):
        return 'ola'


    def neuronio_2(self, neuronio_1):
        return 'ola'












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




home=processarMsm()
print(home.neuronio_2(home.neuronio_1('ola')))
