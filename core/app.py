import logging.config

from flask import Flask
from werkzeug import find_modules, import_string

from core.conf import settings
from core.ext import login_manager, db, session_interface


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)

    configure_blueprints(app, 'apps')
    configure_extensions(app)
    logging.config.dictConfig(app.config['LOGGING'])
    return app


def configure_blueprints(app, root):
    for name in find_modules(root, include_packages=True, recursive=True):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)


def configure_extensions(app):
    @login_manager.user_loader
    def load_user(user_id):
        """Loads the user. Required by the `login` extension."""
        raise NotImplementedError('missing load_user logic')

    @login_manager.unauthorized_handler
    def unauthorized():
        raise NotImplementedError('missing unauthorized_handler')

    db.init_app(app)
    login_manager.init_app(app)

    app.session_interface = session_interface
