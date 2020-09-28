# Denisbot - 27/10/2020
# Gustavo Raphael Stein
# gustavostein@outlook.com

import os
# API em Flask para interface com Chatterbot
from flask import Flask, render_template, request, flash, redirect, url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/app/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
# Upload máximo 10MB
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#

# Cria uma instância do Chatterbot
portuguese_bot = ChatBot("Chatterbot", read_only=True, storage_adapter="chatterbot.storage.SQLStorageAdapter",database_uri='sqlite:///database.sqlite3')
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

# Verifica extensão do arquivo
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/")
def login():
    return render_template("login.html")

# Upload de arquivos: https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('chatbot', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route("/chatbot", methods=['GET', 'POST'])
def chatbot():
    return render_template("chatbot.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(portuguese_bot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
