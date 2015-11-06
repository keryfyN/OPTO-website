# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from .models import Tft, TftSize, TftResolution, TftPort

tft = Blueprint('tfts', __name__, url_prefix='/products/displays/tfts')

# Landing
@tft.route('/', defaults=dict(tft_size_link='All', tft_resolution_link='All', tft_port_link='All'))
@tft.route('/<tft_size_link>/<tft_resolution_link>/<tft_port_link>')
def tft_landing_en(tft_size_link, tft_resolution_link, tft_port_link):
    # tft

    #variable
    global size_count_dic_item
    global tft_list_all_count
    global tft_list_prod_count
    global tft_list_old_count

    # ##########
    if tft_size_link == 'All' and tft_resolution_link == 'All' and tft_port_link == 'All':
        print('0-0-0')
        tft_list_all = Tft.query.all()
        tft_list_prod = Tft.query.filter_by(tft_in_production=True)
        tft_list_old = Tft.query.filter_by(tft_in_production=False)

        tft_list_prod_count = Tft.query.filter_by(tft_in_production=True).count()
        tft_list_old_count = Tft.query.filter_by(tft_in_production=False).count()
        tft_list_all_count = tft_list_prod_count + tft_list_old_count

    elif tft_size_link == 'All' and tft_resolution_link == 'All' and not tft_port_link == 'All':
        # Filter by port ########################
        print('0-0-1')
        # List all tfts with this port_type for example LVDS
        tft_list_all = Tft.query.filter(Tft.tfts.any(TftPort.port_type==tft_port_link)).all()
        tft_list_all_count = len(tft_list_all)
        # List all tfts with this port_type for example LVDS and in production
        tft_list_prod = Tft.query.filter_by(tft_in_production=True).filter(Tft.tfts.any(TftPort.port_type==tft_port_link)).all()
        tft_list_prod_count = len(tft_list_prod)
        # List all tfts with this port_type for example LVDS and not in production
        tft_list_old = Tft.query.filter_by(tft_in_production=False).filter(Tft.tfts.any(TftPort.port_type==tft_port_link)).all()
        tft_list_old_count = len(tft_list_old)

    elif tft_size_link == 'All' and not tft_resolution_link == 'All' and tft_port_link == 'All':
        print('0-1-0')
        reso_xy = tft_resolution_link.split('x')
        tft_resolution = TftResolution.query.filter_by(resolution_x=reso_xy[0], resolution_y=reso_xy[1]).first()
        tft_list_all = Tft.query.filter_by(tft_resolution_id=tft_resolution.id)
        tft_list_prod = Tft.query.filter_by(tft_resolution_id=tft_resolution.id, tft_in_production=True)
        tft_list_old = Tft.query.filter_by(tft_resolution_id=tft_resolution.id, tft_in_production=False)

        tft_list_prod_count = Tft.query.filter_by(tft_resolution_id=tft_resolution.id, tft_in_production=True).count()
        tft_list_old_count = Tft.query.filter_by(tft_resolution_id=tft_resolution.id, tft_in_production=False).count()
        tft_list_all_count = tft_list_prod_count + tft_list_old_count

    elif tft_size_link == 'All' and not tft_resolution_link == 'All' and not tft_port_link == 'All':
        # Filter by port AND RESOLUTION ########################
        print('0-1-1')

        reso_xy = tft_resolution_link.split('x')
        tft_resolution = TftResolution.query.filter_by(resolution_x=reso_xy[0], resolution_y=reso_xy[1]).first()

        # List all tfts with this port_type AND RESOLUTION for example LVDS AND 1024X768
        tft_list_all = Tft.query.filter_by(tft_resolution_id=tft_resolution.id).filter(Tft.tfts.any(TftPort.port_type==tft_port_link)).all()
        tft_list_all_count = len(tft_list_all)
        # lIKE UPPER BUT WITH in production
        tft_list_prod = Tft.query.filter_by(tft_resolution_id=tft_resolution.id, tft_in_production=True).filter(Tft.tfts.any(TftPort.port_type==tft_port_link)).all()
        tft_list_prod_count = len(tft_list_prod)
        # lIKE UPPER BUT WITH NOT in production
        tft_list_old = Tft.query.filter_by(tft_resolution_id=tft_resolution.id, tft_in_production=False).filter(Tft.tfts.any(TftPort.port_type==tft_port_link)).all()
        tft_list_old_count = len(tft_list_old)

    elif not tft_size_link == 'All' and tft_resolution_link == 'All' and tft_port_link == 'All':
        print('1-0-0')
        size_conv = float(tft_size_link)
        tft_size = TftSize.query.filter_by(size_inch=size_conv).first()
        tft_list_all = Tft.query.filter_by(tft_size_id=tft_size.id)
        tft_list_prod = Tft.query.filter_by(tft_size_id=tft_size.id, tft_in_production=True)
        tft_list_old = Tft.query.filter_by(tft_size_id=tft_size.id, tft_in_production=False)

        tft_list_prod_count = Tft.query.filter_by(tft_size_id=tft_size.id, tft_in_production=True).count()
        tft_list_old_count = Tft.query.filter_by(tft_size_id=tft_size.id, tft_in_production=False).count()
        tft_list_all_count = tft_list_prod_count + tft_list_old_count

    elif not tft_size_link == 'All' and tft_resolution_link == 'All' and not tft_port_link == 'All':
        print('1-0-1')

        size_conv = float(tft_size_link)
        tft_size = TftSize.query.filter_by(size_inch=size_conv).first()

        # List all tfts with this port_type for example 5.7 AND LVDS
        tft_list_all = Tft.query.filter_by(tft_size_id=tft_size.id).filter(Tft.tfts.any(TftPort.port_type==tft_port_link)).all()
        tft_list_all_count = len(tft_list_all)
        # lIKE UPPER BUT WITH in production
        tft_list_prod = Tft.query.filter_by(tft_in_production=True, tft_size_id=tft_size.id ).filter(Tft.tfts.any(TftPort.port_type==tft_port_link)).all()
        tft_list_prod_count = len(tft_list_prod)
        # lIKE UPPER BUT WITH NOT in production
        tft_list_old = Tft.query.filter_by(tft_in_production=False, tft_size_id=tft_size.id).filter(Tft.tfts.any(TftPort.port_type==tft_port_link)).all()
        tft_list_old_count = len(tft_list_old)




    elif not tft_size_link == 'All' and not tft_resolution_link == 'All' and tft_port_link == 'All':
        print('1-1-0')
        size_conv = float(tft_size_link)
        tft_size = TftSize.query.filter_by(size_inch=size_conv).first()

        reso_xy = tft_resolution_link.split('x')
        tft_resolution = TftResolution.query.filter_by(resolution_x=reso_xy[0], resolution_y=reso_xy[1]).first()
        tft_list_all = Tft.query.filter_by(tft_resolution_id=tft_resolution.id, tft_size_id=tft_size.id)
        tft_list_prod = Tft.query.filter_by(tft_resolution_id=tft_resolution.id, tft_size_id=tft_size.id,
                                            tft_in_production=True)
        tft_list_old = Tft.query.filter_by(tft_resolution_id=tft_resolution.id, tft_size_id=tft_size.id,
                                           tft_in_production=False)

        tft_list_prod_count = Tft.query.filter_by(tft_resolution_id=tft_resolution.id, tft_size_id=tft_size.id,
                                                  tft_in_production=True).count()
        tft_list_old_count = Tft.query.filter_by(tft_resolution_id=tft_resolution.id, tft_size_id=tft_size.id,
                                                 tft_in_production=False).count()
        tft_list_all_count = tft_list_prod_count + tft_list_old_count

    elif not tft_size_link == 'All' and not tft_resolution_link == 'All' and not tft_port_link == 'All':
        print('1-1-1')

        size_conv = float(tft_size_link)
        tft_size = TftSize.query.filter_by(size_inch=size_conv).first()
        reso_xy = tft_resolution_link.split('x')
        tft_resolution = TftResolution.query.filter_by(resolution_x=reso_xy[0], resolution_y=reso_xy[1]).first()

        # List all tfts with this port_type, size AND RESOLUTION for example 5.7 LVDS AND 1024X768
        tft_list_all = Tft.query.filter_by(tft_resolution_id=tft_resolution.id).filter_by( tft_size_id=tft_size.id).filter(Tft.tfts.any(TftPort.port_type==tft_port_link)).all()
        tft_list_all_count = len(tft_list_all)
        # lIKE UPPER BUT WITH in production
        tft_list_prod = Tft.query.filter_by(tft_resolution_id=tft_resolution.id, tft_in_production=True, tft_size_id=tft_size.id ).filter(Tft.tfts.any(TftPort.port_type==tft_port_link)).all()
        tft_list_prod_count = len(tft_list_prod)
        # lIKE UPPER BUT WITH NOT in production
        tft_list_old = Tft.query.filter_by(tft_resolution_id=tft_resolution.id, tft_in_production=False, tft_size_id=tft_size.id).filter(Tft.tfts.any(TftPort.port_type==tft_port_link)).all()
        tft_list_old_count = len(tft_list_old)


    # ############## dont touch below!!!

    # Size tft list and quantity ##################################################
    # #############################################################################

    size_list = TftSize.query.all()
    size_count_list = []


    # first position in the list of dictionaries
    url = 'All/{0}/{1}'.format(tft_resolution_link, tft_port_link)
    size_count_dic_all_item = dict([('size', 'All'), ('active', True), ('url', url)])
    size_count_list.append(size_count_dic_all_item)

    # next positions in the list of dictionaries
    for size_item in size_list:
        url = '{0}/{1}/{2}'.format(str(size_item.size_inch), tft_resolution_link, tft_port_link)
        size_count_dic_item = dict([('size', str(size_item.size_inch)), ('active', False), ('url', url)])
        size_count_list.append(size_count_dic_item)

    # Scan to activate the link
    for size_count_item in size_count_list:
        size_count_item['active'] = size_count_item['size'] == tft_size_link

    # #############################################################################
    # END Size tft list and quantity ##############################################


    # Resolution tft list and quantity ############################################
    # #############################################################################

    resolution_list = TftResolution.query.all()
    resolution_count_list = []

    # first position in the list of dictionaries
    url = '{0}/All/{1}'.format(tft_size_link, tft_port_link)
    shortcut_url = 'All'
    resolution_count_dic_all_item = dict([('resolution', 'All'), ('active', True),
                                          ('url', url), ('shortcut_url', shortcut_url)])
    resolution_count_list.append(resolution_count_dic_all_item)

    # next positions in the list of dictionaries
    for resolution_item in resolution_list:
        qty = len(resolution_item.tfts)
        resolution_txt = '{0}x{1} : {2}'.format(str(resolution_item.resolution_x), str(resolution_item.resolution_y),
                                                str(resolution_item.resolution_text))
        url_txt = '{0}x{1}'.format(str(resolution_item.resolution_x), str(resolution_item.resolution_y))
        url = '{0}/{1}/{2}'.format(tft_size_link, url_txt, tft_port_link)
        resolution_count_dic_item = dict([('resolution', resolution_txt), ('active', False),
                                          ('url', url), ('shortcut_url', url_txt)])
        resolution_count_list.append(resolution_count_dic_item)

    # Scan to activate the link
    for resolution_count_item in resolution_count_list:
        resolution_count_item['active'] = resolution_count_item['shortcut_url'] == tft_resolution_link

    # #############################################################################
    # END Resolution tft list and quantity ########################################

    # Port tft list and quantity ##################################################
    # #############################################################################

    port_list = TftPort.query.all()
    port_count_list = []

    # first position in the list of dictionaries
    url = '{0}/{1}/All'.format(tft_size_link, tft_resolution_link)
    port_count_dic_all_item = dict([('port', 'All'), ('active', True), ('url', url)])
    port_count_list.append(port_count_dic_all_item)

    # next positions in the list of dictionaries
    for port_item in port_list:
        qty = 5 # len(port_item.tfts)
        url = '{0}/{1}/{2}'.format(tft_size_link, tft_resolution_link, port_item.port_type)
        port_count_dic_item = dict([('port', port_item.port_type), ('active', False), ('url', url)])
        port_count_list.append(port_count_dic_item)

    # Scan to activate the link
    for port_count_item in port_count_list:
        port_count_item['active'] = port_count_item['port'] == tft_port_link

    # #############################################################################
    # END Port tft list and quantity ##############################################

    # print(resolution_count_list)
    # print('----------------------')
    # print(port_count_list)


    return render_template('/tfts/tft_displays_landing_en.html', title='TFT | OPTO Logic TECHNOLOGY',
                           size_count_list=size_count_list,
                           resolution_count_list=resolution_count_list,
                           port_count_list=port_count_list,

                           tft_list_all=tft_list_all,
                           tft_list_prod=tft_list_prod,
                           tft_list_old=tft_list_old,

                           tft_list_all_count=tft_list_all_count,
                           tft_list_prod_count=tft_list_prod_count,
                           tft_list_old_count=tft_list_old_count)


# Details
@tft.route('/<int:tft_id>/details')
def tft_details(tft_id=1):
    tft_details = Tft.query.filter_by(id=tft_id).first()
    return render_template('/tfts/tft_displays_details.html', tft_details=tft_details)
