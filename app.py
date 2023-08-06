import logging
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_injector import FlaskInjector
from injector import inject
from config import Config
from database import db
from security.controllers.user_controller import user_bp
from security.controllers.user_token_controller import user_token_bp
from security.data_access.user_data_manager_ABC import UserDataManagerABC
from security.data_access.user_token_data_manager_ABC import UserTokenDataManagerABC
from security.services.user_service import UserService
from security.services.user_token_service import UserTokenService
from task_management.data_access.task_data_manager_ABC import TaskDataManagerABC
from task_management.services.task_service import TaskService
from task_management.controllers.task_controller import task_bp
from security.services.encyption.encryption_service_ABC import EncryptionServiceABC

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.TASKMANAGEMENT_DB_URI
app.config['SQLALCHEMY_BINDS'] = {
    'task_db': Config.SECURITY_DB_URI,
}
db.init_app(app)
migrate = Migrate(app, db)

# Register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(user_token_bp)
app.register_blueprint(task_bp)

logging.basicConfig(level=logging.ERROR)


@app.errorhandler(Exception)
def handle_exception(error):
    # Log the exception
    logging.exception("An exception occurred:")
    return jsonify({"error": "An internal server error occurred"}), 500


@inject
def configure(binder):
    from security.data_access_sqlalchemy.user_data_manager import UserDataManager as SQLUserDataManager
    from security.data_access_sqlalchemy.user_token_data_manager import UserTokenDataManager as SQLUserTokenDataManager
    binder.bind(UserDataManagerABC, to=SQLUserDataManager)
    binder.bind(UserService, to=UserService)
    binder.bind(UserTokenDataManagerABC, to=SQLUserTokenDataManager)
    binder.bind(UserTokenService, to=UserTokenService)
    binder.bind(TaskService, to=TaskService)
    from task_management.data_access_sqlalchemy.task_data_manager import TaskDataManager
    binder.bind(TaskDataManagerABC, to=TaskDataManager)
    from security.services.encyption.encryption_service import EncryptionService
    binder.bind(EncryptionServiceABC, to=EncryptionService)


# Configure Flask-Injector
FlaskInjector(app=app, modules=[configure])


if __name__ == '__main__':
    app.run(debug=True)
