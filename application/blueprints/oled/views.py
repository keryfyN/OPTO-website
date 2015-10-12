# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

oled = Blueprint('oled', __name__, url_prefix='/products/displays/oled')

# Landing
@oled.route('/')
def oled_landing_en():
    #print(request.accept_languages)
    return render_template('/oled/oled_landing_en.html' , title='OLED | OPTO Logic TECHNOLOGY')

# Details
@oled.route('/<int:oled_id>/details')
def oled_details(oled_id):
    return render_template('/tfts/tft_displays_details.html', title='OLED | OPTO Logic TECHNOLOGY', oled_id=oled_id)

