from flask import Flask, render_template, request, redirect
import json
import funciones
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

'''

@app.route('/login', methods=['POST'])
def post():
    data = 'username: '+request.form['username']+' | Password: '+request.form['password']+' | Date: '+str(datetime.datetime.now())
    funciones.agregar(data)
    return redirect('/user')


@app.route('/user')
def user():
    data = None
    data = funciones.leer()
    data = data.split('\n')
    if data == None:
        data = 'No hay Registros :('
    return render_template('panel.html', data = data)

'''

if __name__ == '__main__':
    app.run(debug=True,port=3000)