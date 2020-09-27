# Denisbot

#### Uma implementação do [ChatterBot](https://github.com/gunthercox/ChatterBot) usando Flask.

O Denisbot foi criado no Hackathon promovido pelo Judiciário Exponencial em 2020 em solução ao desafio 2: Uso de IA e Mineração de Dados para melhoria do Processo Judicial Eletrônico. O objetivo deste chatbot é otimizar o tempo, buscamos focar em partes burocráticas que poderiam ser resolvidas sem demandar tempo dos servidores e que pudessem dar celeridade aos processos. 

Criamos, então, o DenisBot. Um sistema de bots inteligentes que ajudam na experiência do usuário em manter o controle dos seus dados. Esse bot interage naturalmente com os usuários quando é treinado com uma base de conversação saneada e concisa. O framework chatterbot utiliza algorítmos de IA para seu processamento de linguagem natural e é capaz de traçar índice de similaridade entre as frases. Além disso, como o Denisbot foi criado em Python, é possível integrá-lo com algoritmos muito mais avançados de Inteligência Artificial, Machine Learning e DeepLearning.

Quando o usuário for inserir um processo no sistema, o DenisBot irá informar quais os documentos são necessários de acordo com o pedido da demanda. O Denisbot irá capturar os dados necessários para abrir o processo conversando com o usuário. De acordo com o fluxo conversacional, o sistema vai orientando o usuário a fazer upload dos documentos, que devem ser então validado por um algoritmo de reconhecimento de padrões. 

O Denisbot busca evitar a ocorrência de erros ou de não indexação de documentos necessários para aquela demanda, pois nesses casos o processo teria que voltar ao solicitante para que ele pudesse corrigi-lo, o que demandaria mais tempo. E do outro lado tem o servidor, que não precisará mais fazer essa análise, economizando seu tempo de trabalho, de forma que possa estar envolvido na resolução de outros procedimentos. Desta forma, o pedido chegará pronto para que esse servidor dê seguimento ao processo.

Acesse a [DEMO](http://104.131.52.240:8080/)

## Instalar local:
 1. Clone o repositório e rode `pip install -r requirements.txt`).
 2. Inicie com o comando `python app.py`.
 3. Acesse o Denisbot em [http://localhost:5000/](http://localhost:5000/)

## Usando docker
 1. Rode o comando `docker build . -t denisbot:0.1`
 2. Inicie com o comando `docker run -it -p 8080:5000 --entrypoint /bin/bash -v $(pwd):/app denisbot:0.1`
 3. Acesse o Denisbot em [http://localhost:8080/](http://localhost:8080/)

## API de integração
O Denisbot é um microsserviço e pode ser acessado por outros sistemas por meio de uma interface REST API. Experimente no navegador acessando o [site](http://104.131.52.240:8080/) e experimente colocar `/get?msg=olá`. Essa funcionalidade permite ter uma base única de conversação que pode ser utilizado em todos os canais (telegram, whatsapp, sms, etc).

## Como treiná-lo?
No diretório `conversas` você encontra os arquivos de conversação, quanto mais conversas tiver nesses arquivos, mais inteligente o Denisbot ficará! No framework há também uma função de IA que faz com que o Denisbot aprenda sozinho, a partir das conversas que ele mesmo tiver com os usuários.

## Licença
Este código é livre para o seu uso, mas o ChatterBot possui uma licença que se aplica e pode ser lida [AQUI](https://github.com/gunthercox/ChatterBot/blob/master/LICENSE) page.
