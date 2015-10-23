# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from .models import Tft, TftSize, TftResolution, TftPort

tft = Blueprint('tfts', __name__, url_prefix='/products/displays/tfts')

# Landing
@tft.route('/', defaults=dict(tft_size_link='All', tft_resolution_link='All'))
@tft.route('/<tft_size_link>/<tft_resolution_link>')
def tft_landing_en(tft_size_link, tft_resolution_link):
    # tft
    #
    # todo les clefs de tri size/resolution/port

    global size_count_dic_item
    tft_list_all = Tft.query.all()
    tft_list_prod = Tft.query.filter_by(tft_in_production=True)
    tft_list_old = Tft.query.filter_by(tft_in_production=False)
    tft_list_prod_count = Tft.query.filter_by(tft_in_production=True).count()
    tft_list_old_count = Tft.query.filter_by(tft_in_production=False).count()
    tft_list_all_count = tft_list_prod_count + tft_list_old_count

    # Size tft list and quantity ##################################################
    # #############################################################################

    # todo filtre en fct de la requete pour le lien actif

    size_list = TftSize.query.all()
    size_count_list = []

    # first position in the list of dictionaries
    size_count_dic_all_item = dict([('size', 'All'), ('qty', tft_list_all_count), ('active', True), ('url', '')])
    size_count_list.append(size_count_dic_all_item)

    # next positions in the list of dictionaries
    for size_item in size_list:
        qty = len(size_item.tfts)
        size_count_dic_item = dict([('size', str(size_item.size_inch)), ('qty', qty), ('active', False),
                             ('url', str(size_item.size_inch))])
        size_count_list.append(size_count_dic_item)

    # Scan to activate the link
    for size_count_item in size_count_list:
        size_count_item['active'] = size_count_item['size'] == tft_size_link

    # #############################################################################
    # END tft_size list and quantity ##############################################


    # Resolution tft list and quantity ############################################
    # #############################################################################

    # todo filtre en fct de la requete pour le lien actif

    resolution_list = TftResolution.query.all()
    resolution_count_list = []

    # first position in the list of dictionaries
    url_txt_all = '{0}/{1}'.format(tft_size_link, tft_resolution_link)
    resolution_count_dic_all_item = dict([('resolution', 'All'), ('qty', tft_list_all_count), ('active', True), ('url', url_txt_all)])
    resolution_count_list.append(resolution_count_dic_all_item)
    print(resolution_count_list)

    # next positions in the list of dictionaries
    for resolution_item in resolution_list:
        qty = len(resolution_item.tfts)
        resolution_txt = '{0}x{1} : {2}'.format(str(resolution_item.resolution_x), str(resolution_item.resolution_y), str(resolution_item.resolution_text))
        url_txt = '{0}x{1}'.format(str(resolution_item.resolution_x), str(resolution_item.resolution_y))
        resolution_count_dic_item = dict([('resolution', resolution_txt), ('qty', qty), ('active', False),
                             ('url', url_txt)])
        resolution_count_list.append(resolution_count_dic_item)

    # Scan to activate the link
    for resolution_count_item in resolution_count_list:
        resolution_count_item['active'] = resolution_count_item['url'] == tft_resolution_link
    print(resolution_count_list)
    print(tft_resolution_link)
    # #############################################################################
    # END tft_size list and quantity ##############################################



    # tft_resolution
    tft_list_reso = TftResolution.query.all()
    tft_list_reso_x = TftResolution.resolution_x
    tft_list_reso_y = TftResolution.resolution_y
    tft_list_title = TftResolution.resolution_text

    # tft_port
    tft_list_port = TftPort.query.all()

    return render_template('/tfts/tft_displays_landing_en.html', title='TFT | OPTO Logic TECHNOLOGY',
                           size_count_list=size_count_list,
                           resolution_count_list=resolution_count_list,

                           tft_list_all=tft_list_all,
                           tft_list_prod=tft_list_prod,
                           tft_list_old=tft_list_old,
                           tft_list_all_count=tft_list_all_count,
                           tft_list_prod_count=tft_list_prod_count,
                           tft_list_old_count=tft_list_old_count,
                           tft_list_title=tft_list_title,
                           tft_list_port=tft_list_port
                           )


# Details
@tft.route('/<int:tft_id>/details')
def tft_details(tft_id):
    return render_template('/tfts/tft_displays_details.html', tft_id=tft_id)
