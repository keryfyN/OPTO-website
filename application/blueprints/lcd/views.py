# -*- coding: utf-8 -*-

from flask import Blueprint, render_template


lcd = Blueprint('lcd', __name__, url_prefix='/products/displays/lcd')


# segment
@lcd.route('/segment')
def lcd_segment():
    return render_template('/lcd/lcd_segment_en.html' , title='LCD Segment | OPTO Logic TECHNOLOGY')

# graphic
@lcd.route('/graphic')
def lcd_graphic():
    return render_template('/lcd/lcd_graphic_en.html' , title='LCD Graphic | OPTO Logic TECHNOLOGY')


# Details
@lcd.route('/<int:lcd_id>/lcd_details')
def lcd_details(lcd_id):
    # lcd = Lcd.get_by_id(lcd_id)
    return render_template('/lcd/lcd_details.html', title='LCD Details | OPTO Logic TECHNOLOGY', lcd_id=lcd_id)
