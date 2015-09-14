# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
# from .models import Lcd

lcd = Blueprint('lcd', __name__, url_prefix='/lcd')


# Landing
@lcd.route('/')
def lcd_landing():
    return render_template('main_pages/products/displays/graphic_lcd/graphic_lcd_landing_en.html')



# Details
@lcd.route('/<int:lcd_id>/details')
def lcd_details(lcd_id):
    # lcd = Lcd.get_by_id(lcd_id)
    return render_template('lcd/lcd_details.html', lcd_id=lcd_id)


# List
@lcd.route('/list')
def lcd_list():
    return render_template('lcd/lcd_list.html')


# Advanced search
@lcd.route('/search')
def advanced_search():
    return render_template('lcd/cd_advanced_search.html')
