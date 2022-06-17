import os.path


DATABASE_FILE_PATH = os.path.join(os.getcwd(), 'table.db')
FIXTURE_BASE_DIR = 'fixtures'


class Config:
    # Настройки ORM.
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_FILE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JSON_AS_ASCII = False
    # REST_JSON = {'ensure_ascii': False, 'indent': 2}

    # Фикстуры.
    USER_ROLES_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'user_roles.join')
    USERS_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'users.json')
    ORDERS_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'orders.json')
    OFFERS_FIXTURE_PATH = os.path.join(FIXTURE_BASE_DIR, 'offers.json')
