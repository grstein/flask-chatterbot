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

# greetings: https://github.com/gunthercox/chatterbot-corpus/blob/master/chatterbot_corpus/data/portuguese/greetings.yml
# denisbot.yaml arquivo de treinamento do Denisbot desenvolvido pela equipe
trainer.train(
    "chatterbot.corpus.portuguese.greetings",
    "./conversas/denisbot.yaml",
    "./conversas/misc.yaml",
    "./conversas/nerds.yaml"
    )

# https://chatterbot.readthedocs.io/en/stable/training.html
# Treinar o robô com uma lista de convesas em português feito pela comunidade
trainer = ListTrainer(portuguese_bot)

@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/denisbot")
def denisbot():
    return render_template("denisbot.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(portuguese_bot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
