from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class UsuarioSucursalForm(FlaskForm):
    usuario_id = IntegerField('ID de Usuario', validators=[DataRequired()])
    sucursal_id = IntegerField('ID de Sucursal', validators=[DataRequired()])
    submit = SubmitField('Asociar')
