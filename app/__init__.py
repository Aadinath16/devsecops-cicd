from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Simple configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-dev-key-for-local-only')

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app