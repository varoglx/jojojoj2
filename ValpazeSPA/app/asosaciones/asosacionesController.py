from flask import Blueprint,render_template,url_for,redirect,flash,jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
from app.user.models import Usuarios
from app.user.forms import RegisterForm,LoginForm
from app.db import db
from app import login_manager   
from flask_login import login_user,current_user,login_required,logout_user
from flask import session
from app import app
from app.user.models import Usuarios
from app.sucursal.models import Sucursal
from app.asosaciones.forms import UsuarioSucursalForm
from app.asosaciones.models import usuario_sucursal

asosacionesBP = Blueprint('asosaciones',__name__)
from app import db
from app.user.models import Usuarios
from app.sucursal.models import Sucursal  # Asumiendo que tienes un modelo llamado Sucursal

@asosacionesBP.route('/asociar', methods=['GET', 'POST'])
def asociar_usuario_sucursal():
    form = UsuarioSucursalForm()

    if form.validate_on_submit():
        usuario_id = form.usuario_id.data
        sucursal_id = form.sucursal_id.data

        # Verificar que el usuario y la sucursal existen
        usuario = Usuarios.query.get(usuario_id)
        sucursal = Sucursal.query.get(sucursal_id)

        if not usuario or not sucursal:
            flash('Usuario o Sucursal no válido.', 'danger')
            return redirect(url_for('user.dashboard'))

        # Comprobar si ya existe la asociación
        asociacion_existente = db.session.query(usuario_sucursal).filter_by(usuario_id=usuario_id, sucursal_id=sucursal_id).first()
        if asociacion_existente:
            flash('Esta asociación ya existe.', 'info')
            return redirect(url_for('user.dashboard'))

        # Crear la nueva asociación
        nueva_asociacion = usuario_sucursal(usuario_id=usuario_id, sucursal_id=sucursal_id)
        db.session.add(nueva_asociacion)
        db.session.commit()

        flash('Asociación creada con éxito!', 'success')
        return redirect(url_for('asociar'))

    return render_template('asosaciones/usuario_sucursal.html', form=form)


@asosacionesBP.route('/desasociar', methods=['POST'])
def desasociar_usuario_sucursal():
    usuario_id = request.json.get('usuario_id')
    sucursal_id = request.json.get('sucursal_id')
    
    usuario = Usuarios.query.get(usuario_id)
    sucursal = Sucursal.query.get(sucursal_id)

    if not usuario or not sucursal:
        return jsonify({'error': 'Usuario o Sucursal no encontrados'}), 404

    if sucursal not in usuario.sucursales:
        return jsonify({'error': 'Asociación no encontrada'}), 404

    usuario.sucursales.remove(sucursal)
    db.session.commit()

    return jsonify({'message': 'Asociación eliminada con éxito'}), 200



