from flask_sqlalchemy import SQLAlchemy

# Crea la instancia de SQLAlchemy
db = SQLAlchemy()
from app.sucursal.models import Sucursal
from app.user.models import Usuarios
# Configura la base de datos usando la instancia db
def configure_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/alv'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

# Otras configuraciones de la base de datos, como modelos y vínculos, pueden ir aquí
