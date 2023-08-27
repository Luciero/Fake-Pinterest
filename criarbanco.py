from fakepinterest import database, app
from fakepinterest.models import Usuario, Posts

with app.app_context():
    database.create_all()
