# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

thermal_printers = Blueprint('thermal_printers', __name__, url_prefix='/products/thermal_printers')


# Landing
@thermal_printers.route('/')
def thermal_printers_landing_en():
    return render_template('/thermal_printers/mechanism_printers.html_landing_en.html', title='Thermal Printers | OPTO Logic TECHNOLOGY')

# mechanism_printers
@thermal_printers.route('/mechanism_printers')
def mechanism_printers():
    return render_template('/thermal_printers/mechanism_printers.html', title='Mechanism Printers | OPTO Logic TECHNOLOGY')

# mobile_printers
@thermal_printers.route('/mobile_printers')
def mobile_printers():
    return render_template('/thermal_printers/mobile_printers.html', title='Mobile Printers | OPTO Logic TECHNOLOGY')

# panel_printers
@thermal_printers.route('/panel_printers')
def panel_printers():
    return render_template('/thermal_printers/panel_printers.html', title='Panel Printers | OPTO Logic TECHNOLOGY')

# pos_printers
@thermal_printers.route('/pos_printers')
def pos_printers():
    return render_template('/thermal_printers/pos_printers.html', title='POS Printers | OPTO Logic TECHNOLOGY')


# Details
@thermal_printers.route('/<int:thermal_printers_id>/details')
def thermal_printers_details(thermal_printers_id):
    return render_template('/thermal_printers/thermal_printers_details.html', tft_id=tft_id)
