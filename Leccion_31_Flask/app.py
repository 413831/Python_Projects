from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)

app.secret_key = 'Mi llave secreta'

# ** NOTAS DE CONFIGURACIÓN **
# export FLASK_APP=app.py
# export FLASK_EVN=development
# nota: en Windows se reemplaza export por set

# http://localhost:5000/
@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario ya ha hecho login {session["username"]}'
    # app.logger.info(f'Entramos al path {request.path}')
    return 'No ha hecho login'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Omitimos validación de usuario y password
        # agregar el usuario a la sesión
        session['username'] = request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre.upper()}'

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es: {edad + 5}'

@app.route('/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre='Juan'))

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404

# REST Representational state transfer
@app.route('/api/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_json(nombre):
    valores = {'nombre': nombre, 'metodo_http': request.method}
    return jsonify(valores)






