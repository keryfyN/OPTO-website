# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

custom_displays = Blueprint('custom_displays', __name__, url_prefix='/products/displays/custom_displays')

# Landing
@custom_displays.route('/')
def custom_displays_landing_en():
    #print(request.accept_languages)
    return render_template('/custom_displays/custom_displays_landing_en.html' , title='CUSTOM DISPLAYS | OPTO Logic TECHNOLOGY')

# Details
@custom_displays.route('/<int:custom_displays_id>/details')
def custom_displays_details(custom_displays_id):
    return render_template('/custom_displays/custom_displays_details.html', title='CUSTOM DISPLAYS | OPTO Logic TECHNOLOGY' , epaper_id=epaper_id)

