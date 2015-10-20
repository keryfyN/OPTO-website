# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

others = Blueprint('others', __name__, url_prefix='/products/others')

# Landing
@others.route('/')
def others_landing_en():
    #print(request.accept_languages)
    return render_template('/others/others_landing_en.html' , title='OTHERS | OPTO Logic TECHNOLOGY')

# Details
@others.route('/<int:others_id>/details')
def others_details(oled_id):
    return render_template('/others/others_details.html', title='OTHERS | OPTO Logic TECHNOLOGY', oled_id=oled_id)

