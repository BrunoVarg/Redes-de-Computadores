from flask import Flask, render_template, request, redirect
#from flask_ngrok import run_with_ngrok
import requests as rq
import random
app = Flask(__name__)
mynumber = random.randrange(0, 500)
#print(mynumber)
tentativas = 0
first_connection = True
#run_with_ngrok(app)
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        global first_connection
        global tentativas
        first_connection = False
        numero = int(request.form['numero'])
        string = ''
        if(numero < mynumber):
            string = 'MAIOR'
            tentativas += 1
            #print(tentativas)
        elif numero > mynumber:
            string = 'MENOR'
            tentativas += 1
            #print(tentativas)
        else:
            return redirect("/success")
        
        return render_template('index.html', string = string, first_connection=first_connection)

@app.route("/generate", methods=['GET', 'POST'])
def generate():
    global mynumber
    global tentativas
    tentativas = 0
    mynumber = random.randrange(0, 500)
    
    return redirect("/")

@app.route("/success", methods=['GET', 'POST'])
def success():
    global tentativas
    global mynumber
    return render_template('success.html', mynumber=mynumber, tentativas=tentativas)
    
if __name__ == "__main__":
    app.run(host='192.168.1.16', debug=True)