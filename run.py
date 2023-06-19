
""""The main app of my flask proyect"""
from flask import Flask
from app.routes.routes import blueprint

app = Flask('run',template_folder='app/views')  
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)

