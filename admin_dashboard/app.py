from flask import Flask

from .views.client_view import client_bp

app = Flask(__name__)
app.config.from_object('admin_dashboard.config')

app.register_blueprint(client_bp, url_prefix='/clients')
