from flask import Flask

import Ifood.ifood

app = Flask(__name__)

@app.route('/iniciar_whatsapp')
def iniciar_whatsapp():
    from webWpp.pegarMensagens import whatsappWeb as end
    web = end(1)


@app.route('/iniciar_ifood')
def iniciar_ifood():
    ifood=Ifood.ifood.ExtrairIfood()

if __name__ == '__main__':
    app.run(debug=True)
