class Config:
    # Настройки базы данных
    # Параметры подключения к PostgreSQL
    DB_HOST = 'localhost'
    DB_PORT = 1111
    DB_NAME = 'mydatabase'
    DB_USER = 'myuser'
    DB_PASSWORD = 'mypass'

    # Настройки для Telegram API
    TELEGRAM_API_ID = '21445636'  # from my.telegram.org
    TELEGRAM_API_HASH = 'ff95622c4327079e5e9f029b43c0f1ab'  # from my.telegram.org
    TELEGRAM_SESSION_NAME = 'your_session_name'

    # Настройки для Celery
    CELERY_BROKER_URL = 'pyamqp://guest@localhost//'
    CELERY_RESULT_BACKEND = 'rpc://'

    SESSION_NAME = "mysession"
    API_ID = "21445636"
    API_HASH = "ff95622c4327079e5e9f029b43c0f1ab"

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False