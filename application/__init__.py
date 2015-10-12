from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from .blueprints.tfts import tft
from .blueprints.lcd import lcd
from .blueprints.oled import oled
from .blueprints.epaper import epaper
from .blueprints.custom_displays import custom_displays
from .frontend import frontend


# Create the app and configuration
# Read the configuration file
app = Flask(__name__)
app.config.from_object('application.default_settings')
app.config.from_envvar('PRODUCTION_SETTINGS', silent=True)


# Register the following plugins(blueprints)
app.register_blueprint(frontend)
app.register_blueprint(tft)
app.register_blueprint(lcd)
app.register_blueprint(oled)
app.register_blueprint(epaper)
app.register_blueprint(custom_displays)


# Connect to database with sqlalchemy.
db = SQLAlchemy(app)

# Connect utility
#toolbar = DebugToolbarExtension(app)


# 404 page not found "route"
@app.errorhandler(404)
def not_found(error):
    title = "404 Page not found"
    return render_template('404.html', title=title), 404


# 500 server error "route"
@app.errorhandler(500)
def server_error(error):
    title = "500 Server Error"
    db.session.rollback()
    return render_template('500.html', title=title), 500


