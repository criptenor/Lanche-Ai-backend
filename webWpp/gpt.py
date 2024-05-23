import openai

class Chat:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def enviar_mensagem(self, mensagem):
        # Envia a mensagem para o modelo de chat
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Usando o modelo de chat Davinci
            prompt=mensagem,
            max_tokens=10,
        )

        return response.choices[0].text.strip()

# Exemplo de uso
api_key = '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'
chat = Chat(api_key)

# Enviar uma mensagem e obter a resposta
mensagem_usuario = "Olá, como você está?"
resposta = chat.enviar_mensagem(mensagem_usuario)
print("Resposta:", resposta)
