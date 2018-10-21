from src.app import create_simple_app
from src.app import create_app

if __name__ == '__main__':
    app = create_app()
    port = app.config["APP_PORT"]
    development_mode = app.config.get("DEVELOPMENT", False)

    print('--- Starting Flask App Server on port {} ---'.format(port))
    app.run(app, port=port, debug=development_mode)

    
