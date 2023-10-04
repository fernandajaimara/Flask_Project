from flask import Flask

app = Flask(__name__)

@app.route('/')
def raiz():
    return 'Olá Mundo!'

@app.route('/calculadora/<int>:n1/<int>:n2/<string>:operador')
def calculadora(n1, n2, operacao):
    if operacao == "soma":
        resultado = n1 + n2
    elif operacao == "sub":
        resultado = n1 - n2
    elif operacao == "mult":
        resultado = n1 * n2
    elif operacao == "div":
        resultado = n1 / n2
    else:
        resultado = "Operação não suportada"

    return '{} {} {} = {}'.format(n1, operacao, n2, resultado)

app.run()