# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

tft = Blueprint('tfts', __name__, url_prefix='/products/displays/tfts')

# Landing
@tft.route('/')
def tft_landing_en():
    #print(request.accept_languages)
    return render_template('/tfts/tft_displays_landing_en.html' , title='TFT | OPTO Logic TECHNOLOGY')

# Details
@tft.route('/<int:tft_id>/details')
def tft_details(tft_id):
    return render_template('/tfts/tft_displays_details.html', tft_id=tft_id)

