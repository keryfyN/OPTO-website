# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

touch_panels = Blueprint('touch_panels', __name__, url_prefix='/products/touch_panels')


# landing
@touch_panels.route('/')
def touch_panels_landing():
    return render_template('/touch_panels/touch_panels_landing_en.html', title='Touch Panels | OPTO Logic TECHNOLOGY')


# pcap
@touch_panels.route('/pcap')
def touch_panels_pcap():
    return render_template('/touch_panels/touch_panels_pcap_en.html', title='Touch Panels PCAP | OPTO Logic TECHNOLOGY')


# rtp
@touch_panels.route('/rtp')
def touch_panels_rtp():
    return render_template('/touch_panels/touch_panels_rtp_en.html', title='Touch Panels RTP | OPTO Logic TECHNOLOGY')


# Details
'''@touch_panels.route('/<int:touch_panels_id>/touch_panels_details')
def touch_panels_details(touch_panels_id):
    return render_template('/touch_panels/touch_panels_details.html',
                           title='Touch Panels Details | OPTO Logic TECHNOLOGY', lcd_id=touch_panels_id)'''
