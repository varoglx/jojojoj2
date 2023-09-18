from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SucursalForm(FlaskForm):
    nombre_sucursal = StringField('Nombre de la Sucursal', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('Registrar')
