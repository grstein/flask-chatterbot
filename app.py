# Denisbot - 27/10/2020
# Gustavo Raphael Stein
# gustavostein@outlook.com

# API em Flask para interface com Chatterbot

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# Cria uma instância do Chatterbot
portuguese_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter",database_uri='sqlite:///database.sqlite3')
# Cria uma instância do treinador
trainer = ChatterBotCorpusTrainer(portuguese_bot)
trainer.train("chatterbot.corpus.portuguese")

# Treinar o robô com uma lista de convesas em português feito pela comunidade
trainer = ListTrainer(portuguese_bot)

# Treinar o robô com frases próprias para o sistema
trainer.train([
    "Olá, em que posso lhe ajudar?",
    "Eu gostaria de iniciar um processo.",
    "Qual é o assunto do seu processo?",
    "Processo de Aposentadoria por tempo de contribuição.",
    "Ah, que ótimo! Este processo precisa de alguns documentos específicos. Vamos verificar se você possui todos?",
    "Sim",
    "Eu preciso de uma cópia da carteira de trabalho",
    "Aqui está",
    "Ótimo, maravilha, fantástico!!!"
])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(portuguese_bot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
