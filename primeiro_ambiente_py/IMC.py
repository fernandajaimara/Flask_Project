from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])

def calcular():
    imc = ''
    if request.method == 'POST' and 'peso' in request.form and 'altura' in request.form:
        p = float(request.form.get('peso'))
        a = float(request.form.get('altura'))
        imc = round(p / (a*a),2)
    return render_template('index.html', imc=imc)

app.run()
