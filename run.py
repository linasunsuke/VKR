import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Создание экземпляра Flask
app = Flask(__name__)
app.config.from_object(Config)

# Инициализация базы данных
db = SQLAlchemy(app)

# Проверка подключения к базе данных с использованием контекста приложения
with app.app_context():
    try:
        db.engine.connect()
        print("Database connected successfully!")
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        sys.exit(1)

# Регистрация Blueprint'ов
from account_management_service.routes import account_management_bp
from subscription_service.routes import subscription_bp
from interaction_service.routes import interaction_bp
from auth_service.routes import auth_bp

app.register_blueprint(account_management_bp, url_prefix='/accounts')
app.register_blueprint(subscription_bp, url_prefix='/subscriptions')
app.register_blueprint(interaction_bp, url_prefix='/interactions')
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

@app.route('/')
def index():
    return 'Welcome to the Multi-Account Administration System'