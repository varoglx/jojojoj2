from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.sucursal.models import Sucursal
from app.sucursal.forms import SucursalForm
from app.db import db

sucursalBP = Blueprint('sucursal', __name__)

@sucursalBP.route('/registrar_sucursal', methods=['GET', 'POST'])
def registrar_sucursal():
    form = SucursalForm()
    if form.validate_on_submit():
        sucursal = Sucursal(nombre_sucursal=form.nombre_sucursal.data)
        db.session.add(sucursal)
        db.session.commit()
        flash('Sucursal registrada con éxito!', 'success')
        return redirect(url_for('sucursal.listar_sucursales'))
    return render_template('sucursal/registrar_sucursal.html', form=form)

@sucursalBP.route('/sucursales')
def listar_sucursales():
    sucursales = Sucursal.query.all()
    return render_template('sucursal/listar_sucursales.html', sucursales=sucursales)

# Puedes continuar con otras operaciones CRUD como editar y eliminar.
