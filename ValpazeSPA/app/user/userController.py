from flask import Blueprint,render_template,url_for,redirect,flash,jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash
from app.user.models import Usuarios
from app.user.forms import RegisterForm,LoginForm
from app.db import db
from app import login_manager   
from flask_login import login_user,current_user,login_required,logout_user
from flask import session
from app import app

@login_manager.user_loader
def load_user(user_id):
    
    return Usuarios.query.get(user_id)

usuarioBP = Blueprint('user',__name__)
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = Usuarios(email=form.email.data, username=form.username.data, nombre=form.nombre.data, apellido=form.apellido.data)
        user.password = generate_password_hash(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Usuario registrado con éxito!', 'success')
        return redirect(url_for('user.login'))  # O la ruta que desees después de registrar
    return render_template('user/register.html', form=form)


@usuarioBP.route('/', methods=['GET', 'POST'])
def login():
    


    form = LoginForm()
    if form.validate_on_submit():#valida el formulario 
        user = Usuarios.query.filter_by(username=form.username.data).first()#consulta si esta el usuario

        
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('register'))
                
        else:
            flash('Usuario o contraseña incorrectos.', 'error')
            return redirect(url_for('login'))  



    return render_template('user/login.html', form=form)

@usuarioBP.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@usuarioBP.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('user/dashboard.html')


@usuarioBP.route('/perfil')
def perfil():
    return render_template('user/dashboard.html')





