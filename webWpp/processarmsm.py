from typing import List
import json
from supabase import create_client
from unidecode import unidecode

import requests

class PMsm:

    def __init__(self, id_loja=1):
        self.url = "https://odtsaxxshxzdatavzftv.supabase.co"
        self.chave_api = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9kdHNheHhzaHh6ZGF0YXZ6ZnR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE0OTYzNDMsImV4cCI6MjAyNzA3MjM0M30.04XvHLUvjkIdsmu5keJGbUL88DAp97H5bE_a06DdpW4"
        self.cliente_supabase = create_client(self.url, self.chave_api)
        self.id_loja=id_loja




    def boasVindasPrimeiraVez(self,):
        return f"Olá, Seja Bem vindo a {self.pegar_nome_loja(self.id_loja)}! \nComo posso lhe ajudar?  "

    def boasVindasPrimeiraVezDoDia(self, numero):
        return f"Olá {self.pegar_nome_usuario_na_compra_pelo_numero()}, Seja Bem vindo de volta! \nComo posso lhe ajudar?  "

    def cardapiosDeMaisVendidos(self):
        msm='*Esse é nosso cardápio de produtos mais vendidos:*\n\n'
        i=1
        for produto in self.pegar_produtos_mais_vendidos():
            msm+= f'*{i}-{produto["nome_produto"]}* - R${str(produto["valor"]).replace(".", ",")}\n'
            i+=1
        msm+='\nQual produto Você deseja comprar? Ou "Ver Mais"?'
        return msm


    def cardapio(self, msm):
        pelo_id=False
        try:
            msm_inteiro=int(msm)
            pelo_id=True
        except:
            pass

        if pelo_id:
            return self.pegarLinkPeloNumero(msm_inteiro)
        else:
            return 'Faça seu pedido em 1 minuto pelo site:\nhttps://th-lanche.flutterflow.app/inicio'




    def pegarLinkPeloNumero(self, numero):
        produto=self.pegar_produtos_mais_vendidos()[(numero-1)]
        msm= f'Compre Rapidamente esse produto pelo Site:\n https://th-lanche.flutterflow.app/detalhesProduto?idProduto={produto["id_produto"]}'
        return msm


    def tratarSupabae(self, resposta):
        string_json = str(resposta).replace("'", "\"").replace('data=', '').replace(' count=None', '')
        return json.loads(string_json)

    def pegar_status_loja(self, id_loja: int) -> str:
        resposta = self.cliente_supabase.from_("loja").select("status").eq('id', id_loja).execute()
        resposta = self.tratarSupabae(resposta)[0]['status'].replace(' ', '')
        if 'false' in resposta:
            return [False, 'Loja Fechada']
        else:
            return [True, 'Loja Aberta']

    def pegar_nome_loja(self, id_loja: int) -> str:
        resposta = self.cliente_supabase.from_("loja").select("nome").eq('id', id_loja).execute()
        resposta = self.tratarSupabae(resposta)[0]['nome'].replace(' ', '')
        return resposta

    def pegar_nome_usuario_na_compra_pelo_numero(self, numero_usuario: int) -> str:
        resposta = self.cliente_supabase.from_("compra").select("nome_usuario").eq('numero_usuario', numero_usuario).execute()
        resposta = self.tratarSupabae(resposta)[0]['nome_usuario'].replace(' ', '')
        return resposta

    def pegar_produtos_mais_vendidos(self):
        # Define o endpoint da API
        endpoint = self.url + '/rest/v1/rpc/obter_produtos_comprados'

        # Define os dados a serem enviados na solicitação
        payload = {

            "id_loja_param": self.id_loja
        }

        # Define os cabeçalhos da solicitação
        headers = {
            "Content-Type": "application/json",
            "apikey": self.chave_api,
            "Authorization": self.chave_api
        }

        try:
            # Realiza a solicitação HTTP POST
            response = requests.post(endpoint, json=payload, headers=headers)

            # Verifica se a solicitação foi bem-sucedida
            if response.status_code == 200:
                # Retorna os dados da resposta
                return response.json()
            else:
                # Se a solicitação não for bem-sucedida, lança uma exceção
                response.raise_for_status()

        except requests.exceptions.RequestException as e:
            # Captura e imprime qualquer exceção que ocorra durante a solicitação
            print(e)



a=PMsm()
print(a.cardapio('olald'))

