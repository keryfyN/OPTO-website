# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

epaper = Blueprint('epaper', __name__, url_prefix='/products/displays/epaper')

# Landing
@epaper.route('/')
def epaper_landing_en():
    #print(request.accept_languages)
    return render_template('/epaper/epaper_displays_landing_en.html' , title='EPAPER | OPTO Logic TECHNOLOGY')

# Details
@epaper.route('/<int:epaper_id>/details')
def epaper_details(epaper_id):
    return render_template('/epaper/epaper_details.html', title='EPAPER | OPTO Logic TECHNOLOGY' , epaper_id=epaper_id)

