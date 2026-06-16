from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Simple configuration
    app.config['SECRET_KEY'] = 'dev-sec-ops-poc-local-key'

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app