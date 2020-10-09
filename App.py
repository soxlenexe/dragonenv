from flask import Flask, render_template, request, redirect

app = Flask(__name__)
menu = { 'link': '/', 'title': 'DragonEnv', 'elements': [ { 'sub': False, 'title': 'Inicio', 'link': '/', 'links': [] }, { 'sub': True, 'title': 'Servicios', 'link': '/', 'links': [ { 'link': '/#soft', 'title': 'Software' } ] } ] }


@app.errorhandler(404)
def page_not_found(e):
    context = {
        'menu': menu
    }
    return render_template('404.html',context=context), 404


@app.route('/')
def home():
    context = {
        'menu': menu
    }
    return render_template("index.html", context = context)

if __name__ == '__main__':
    app.run(debug=False,port=3000)