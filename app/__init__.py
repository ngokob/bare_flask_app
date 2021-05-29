# Main Imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


# Instantiate the FLask app
app = Flask(__name__)


# Configurations
app.config['ENV'] = 'development'
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "development":
    app.config.from_object("config.DevelopmentConfig")
else:
    app.config.from_object("config.TestingConfig")


db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# HTTP error handler
@app.errorhandler(404)
def not_found(e):
	return render_template("404.html")


# Import modules using blueprint handler
from app.mod_auth import auth_bp
from app.mod_blog import blog_bp


# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(blog_bp, url_prefix='/blog')


# Create the database
db.create_all()
