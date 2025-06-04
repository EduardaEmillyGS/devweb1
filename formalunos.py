from flask import *

#instanciando o servidor flask
app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template('formalunos.html')

@app.route('/buscar', methods=['GET'])
def campo_busca():
    #se for via metodo get, use isso
    cbusca = request.values.get('buscar')

    #se for via post, use isso
    buscar = request.form.get('buscar')

    print(buscar)
    return 'ok'

app.run()