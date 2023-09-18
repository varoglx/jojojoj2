from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

from wtforms import SelectField

class UsuarioSucursalForm(FlaskForm):
    usuario_id = SelectField('Usuario', coerce=int, validators=[DataRequired()])
    sucursal_id = SelectField('ID de Sucursal', validators=[DataRequired()])
    submit = SubmitField('Asociar')

