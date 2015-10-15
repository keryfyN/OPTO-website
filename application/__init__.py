# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

from .database import db
from .blueprints.tfts.models import TftSize
from .blueprints.touch_panels.models import TouchPanelSize


# ------------------------------- #
#           App Factory           #
# ------------------------------- #


def create_app():
    app = Flask(__name__)
    app.config.from_object('application.default_settings')

    db.init_app(app)
    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)

    ## ------------------------------- ##
    #     initializing blueprints       #
    ## ------------------------------- ##

    # frontend blueprints
    from .blueprints.frontend import frontend
    app.register_blueprint(frontend)

    # products/displays blueprints
    from .blueprints.tfts import tft
    app.register_blueprint(tft)

    from .blueprints.lcd import lcd
    app.register_blueprint(lcd)

    from .blueprints.oled import oled
    app.register_blueprint(oled)

    from .blueprints.epaper import epaper
    app.register_blueprint(epaper)

    from .blueprints.custom_displays import custom_displays
    app.register_blueprint(custom_displays)

    # products/touch panels blueprints
    from .blueprints.touch_panels import touch_panels
    app.register_blueprint(touch_panels)

    # 404 page not found "route"
    @app.errorhandler(404)
    def not_found():
        title = "404 Page not found"
        return render_template('404.html', title=title), 404

    # 500 server error "route"
    @app.errorhandler(500)
    def server_error():
        title = "500 Server Error"
        db.session.rollback()
        return render_template('500.html', title=title), 500

    return app
