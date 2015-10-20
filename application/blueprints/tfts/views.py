# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from .models import Tft

tft = Blueprint('tfts', __name__, url_prefix='/products/displays/tfts')


# Landing
@tft.route('/')
def tft_landing_en():
    tft_list_all = Tft.query.all()
    tft_list_prod = Tft.query.filter_by(tft_in_production=True)
    tft_list_old = Tft.query.filter_by(tft_in_production=False)
    tft_list_prod_count = Tft.query.filter_by(tft_in_production=True).count()
    tft_list_old_count = Tft.query.filter_by(tft_in_production=False).count()
    tft_list_all_count = tft_list_prod_count + tft_list_old_count
    return render_template('/tfts/tft_displays_landing_en.html', title='TFT | OPTO Logic TECHNOLOGY',
                           tft_list_all=tft_list_all,
                           tft_list_prod=tft_list_prod,
                           tft_list_old=tft_list_old,
                           tft_list_all_count=tft_list_all_count,
                           tft_list_prod_count=tft_list_prod_count,
                           tft_list_old_count=tft_list_old_count
                           )


# Details
@tft.route('/<int:tft_id>/details')
def tft_details(tft_id):
    return render_template('/tfts/tft_displays_details.html', tft_id=tft_id)
