from flask import Flask

from .views import client_bp, user_bp, address_bp

app = Flask(__name__)
app.config.from_object('admin_dashboard.config')

app.register_blueprint(client_bp, url_prefix='/clients')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(address_bp, url_prefix='/addresses')
