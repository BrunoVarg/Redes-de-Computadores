# Como Rodar a Aplicação

1. Na pasta /Projeto1 rode primeiro:

`pip install -r requirements.txt`

2. Descubra o seu IP/HOST rodando o comando

`ipconfig(Windows) ou ifconfig(Linux)`

O IP estará em "Endereço IPv4"

3. Após saber seu IP, vá até a main.py e altere a linha 50 para o seu IP

`app.run(host='yourIP', debug=True)`

4. Rode a aplicação "main.py"

`py main.py`

5. Entre no navegador através do link 

`yourIP:5000`