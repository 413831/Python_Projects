from flask import Flask, render_template, request, url_for
from flask_migrate import Migrate
from werkzeug.utils import redirect

from database import db
from forms import PersonaForm
from models import Persona

app = Flask(__name__)

# * Configuración de la bd
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'sap_flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
# Se desactiva el tracking para mejorar performance (opcional)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# * Inicialización del objeto db de sqlalchemy
db.init_app(app)

# EXTENSIONES

# * configurar flask-migrate
migrate = Migrate()
migrate.init_app(app, db)
# flask db init
# flask db migrate **
# flask db upgrade **
# flask db stamp head ** Con cada actualización del modelo deben ejecutarse de nuevo

# * configuración de flask-wtf
app.config['SECRET_KEY'] = 'Mi llave secreta'

# RUTAS
@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    # Listado de personas
    # personas = Persona.query.all()
    personas = Persona.query.order_by('id')
    total_personas = Persona.query.count()
    app.logger.debug(f'Listado Personas: {personas}')
    app.logger.debug(f'Total Personas: {total_personas}')
    return render_template('index.html', personas=personas, total_personas=total_personas)


@app.route('/ver/<int:id>')
def ver_detalle(id):
    # Recuperamo la persona según el id proporcionado
    # persona = Persona.query.get(id)
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Ver persona: {persona}')
    return render_template('detalle.html', persona=persona)


@app.route('/agregar', methods=['GET','POST'])
def agregar():
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            app.logger.debug(f'Persona a insertar:{persona}')
            # Insertamos el nuevo registro
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregar.html', forma=personaForm)


@app.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    # Recuperamos el objeto Persona a editar
    # Se mantiene la referencia a la base de datos
    persona = Persona.query.get_or_404(id)
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            app.logger.debug(f'Persona para actualizar:{persona}')
            # Insertamos el nuevo registro
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html', forma = personaForm)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Persona a elininar: {persona}')
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))

