from flask import Flask

from .views.client_view import client_bp
from .views.user_view import user_bp

app = Flask(__name__)
app.config.from_object('admin_dashboard.config')

app.register_blueprint(client_bp, url_prefix='/clients')
app.register_blueprint(user_bp, url_prefix='/users')
