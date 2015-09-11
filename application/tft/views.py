# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
# from .models import Tft

tft = Blueprint('tft', __name__, url_prefix='/products/tft_')


# Landing
@tft.route('/')
def tft_landing():
    return render_template('/templates/main_pages/products/displays/tft_displays/prod_tft_displays_landing_en.html')


# Details
@tft.route('/<int:tft_id>/details')
def tft_details(tft_id):
    # tft_ = Tft.get_by_id(tft_id)
    return render_template('tft_details.html', tft_id=tft_id)


# List
@tft.route('/list')
def tft_list():
    return render_template('tft_list.html')


# Advanced search
@tft.route("/tft_advanced_search")
def tft_advanced_search():
    return render_template('tft_advanced_search.html')
