# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from .models import Tft, TftSize, TftResolution, TftPort

tft = Blueprint('tfts', __name__, url_prefix='/products/displays/tfts')


# Landing
@tft.route('/')
def tft_landing_en():
    # tft
    tft_list_all = Tft.query.all()
    tft_list_prod = Tft.query.filter_by(tft_in_production=True)
    tft_list_old = Tft.query.filter_by(tft_in_production=False)
    tft_list_prod_count = Tft.query.filter_by(tft_in_production=True).count()
    tft_list_old_count = Tft.query.filter_by(tft_in_production=False).count()
    tft_list_all_count = tft_list_prod_count + tft_list_old_count

    # tft_size
    tft_list_size = TftSize.query.all()
    tft_list_size_count = []
    tft_list_size_count.append(len(tft_list_size))

    for tft_list_size_one in tft_list_size:

        tft_list_size_count.append(len(tft_list_size_one.tfts))



    # tft_resolution
    tft_list_reso = TftResolution.query.all()
    tft_list_reso_x = TftResolution.resolution_x
    tft_list_reso_y = TftResolution.resolution_y
    tft_list_title = TftResolution.resolution_text
    # tft_port
    tft_list_port = TftPort.query.all()

    return render_template('/tfts/tft_displays_landing_en.html', title='TFT | OPTO Logic TECHNOLOGY',
                           tft_list_all=tft_list_all,
                           tft_list_prod=tft_list_prod,
                           tft_list_old=tft_list_old,
                           tft_list_all_count=tft_list_all_count,
                           tft_list_prod_count=tft_list_prod_count,
                           tft_list_old_count=tft_list_old_count,
                           tft_list_size=tft_list_size,
                           tft_list_reso_x=tft_list_reso_x,
                           tft_list_reso_y=tft_list_reso_y,
                           tft_list_title=tft_list_title,
                           tft_list_reso=tft_list_reso,
                           tft_list_port=tft_list_port,
                           tft_list_size_count=tft_list_size_count
                           )


# Details
@tft.route('/<int:tft_id>/details')
def tft_details(tft_id):
    return render_template('/tfts/tft_displays_details.html', tft_id=tft_id)
