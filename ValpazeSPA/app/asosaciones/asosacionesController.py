from flask import Blueprint, render_template, url_for, redirect, flash, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from app.user.models import Usuarios
from app.user.forms import RegisterForm, LoginForm
from app.db import db
from flask_login import login_user, current_user, login_required, logout_user
from app.sucursal.models import Sucursal
from app.asosaciones.forms import UsuarioSucursalForm
from app.asosaciones.models import usuario_sucursal

asosacionesBP = Blueprint('asosaciones', __name__)
def get_sucursal_choices():
    return [(s.id_sucursal, s.nombre_sucursal) for s in Sucursal.query.order_by(Sucursal.nombre_sucursal)]

def get_usuario_choices():
    return [(u.id, u.nombre) for u in Usuarios.query.order_by(Usuarios.nombre)]

@asosacionesBP.route('/asociar', methods=['GET', 'POST'])
def asociar_usuario_sucursal():
    form = UsuarioSucursalForm()

    form.sucursal_id.choices = get_sucursal_choices()
    form.usuario_id.choices = get_usuario_choices()
    if form.validate_on_submit():
        usuario_id = int(form.usuario_id.data)

        sucursal_id = int(form.sucursal_id.data)

        usuario = Usuarios.query.get(usuario_id)
        
        sucursal = Sucursal.query.get(sucursal_id)
        
        if not usuario or not sucursal:
            flash('Usuario o Sucursal no válido.', 'danger')
            return redirect(url_for('user.dashboard'))

        # Aquí revisamos si el usuario ya está asociado con esa sucursal
        if sucursal in usuario.sucursales:
            flash('Esta asociación ya existe.', 'info')
            return redirect(url_for('user.dashboard'))

        # Si no está asociado, lo añadimos
        usuario.sucursales.append(sucursal)
        db.session.commit()

        flash('Asociación creada con éxito!', 'success')
        return redirect(url_for('user.login'))

    return render_template('asosaciones/usuario_sucursal.html', form=form)


