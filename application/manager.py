from application import app
from flask import render_template, request

from application.models import *


@app.route('/')
@app.route('/index/')
def index():
    # Version FR
    if request.accept_languages[0][0] == 'fr-CH' or request.accept_languages[0][0] == 'fr-FR' or \
                    request.accept_languages[0][0] == 'fr':
        return render_template('main_pages/index_fr.html', title='OPTO Logic TECHNOLOGY')
    # Version DE
    if request.accept_languages[0][0] == 'de':
        return render_template('main_pages/index_de.html', title='OPTO Logic TECHNOLOGY')
    # Version IT
    if request.accept_languages[0][0] == 'it':
        return render_template('main_pages/index_it.html', title='OPTO Logic TECHNOLOGY')

    # DEFAULT Version EN
    return render_template('main_pages/index_en.html', title='OPTO Logic TECHNOLOGY')



@app.route('/produits/')
@app.route('/produkte/')
@app.route('/prodotti/')
@app.route('/products/')
def products():
    # Version FR
    if request.path == '/produits/':
        return render_template('main_pages/products/products_fr.html', title='Produits | OPTO Logic TECHNOLOGY')
    # Version DE
    elif request.path == '/produkte/':
        return render_template('main_pages/products/products_de.html', title='Produkte | OPTO Logic TECHNOLOGY')
    # Version IT
    elif request.path == '/prodotti/':
        return render_template('main_pages/products/products_it.html', title='Prodotti | OPTO Logic TECHNOLOGY')

    # DEFAULT Version EN
    return render_template('main_pages/products/products_en.html', title='Products | OPTO Logic TECHNOLOGY')


@app.route('/loesungen/')
@app.route('/solutioni/')
@app.route('/solutions/')
def solutions():
    print(request.accept_languages)
    # Version en
    return render_template('main_pages/solutions/solutions_en.html', title='Solutions | OPTO Logic TECHNOLOGY')

@app.route('/partners/')
def partners():
    print(request.accept_languages)
    # Version en
    return render_template('main_pages/partners/partners_en.html', title='Partners | OPTO Logic TECHNOLOGY')

@app.route('/company/')
def company():
    print(request.accept_languages)
    # Version en
    return render_template('main_pages/company/company_en.html', title='Company | OPTO Logic TECHNOLOGY')

@app.route('/support/')
def support():
    print(request.accept_languages)
    # Version en
    return render_template('main_pages/support/support_en.html', title='Support | OPTO Logic TECHNOLOGY')


@app.route('/displays/')
def displays():
    print(request.accept_languages)
    # Version en
    #return render_template('main_pages/products', title='TFT | OPTO Logic TECHNOLOGY')
    return render_template('/main_pages/products/displays/displays_landing_en.html' , title='Displays | OPTO Logic TECHNOLOGY')


@app.route('/tft/')
def tft():
    print(request.accept_languages)
    # Version en
    #return render_template('main_pages/products', title='TFT | OPTO Logic TECHNOLOGY')
    return render_template('/main_pages/products/displays/tft/tft_displays_landing_en.html' , title='TFT | OPTO Logic TECHNOLOGY')


@app.route('/contact/')
def contact():
    print(request.accept_languages)
    # Version en
    return render_template('/main_pages/contact/contact_en.html', title='Contact | OPTO Logic TECHNOLOGY')

@app.route('/lcd_graphic/')
def lcd_graphic():
    print(request.accept_languages)
    # Version en
    return render_template('/main_pages/products/displays/lcd/lcd_graphic_landing_en.html', title='LCD Graphic | OPTO Logic TECHNOLOGY')

@app.route('/lcd_segment/')
def lcd_segment():
    print(request.accept_languages)
    # Version en
    return render_template('/main_pages/products/displays/lcd/lcd_segment_landing_en.html', title='LCD Segment | OPTO Logic TECHNOLOGY')

@app.route('/test/')
def test():
    print(request.accept_languages)
    # Version en
    return render_template('main_pages/test/test.html', title='Test | OPTO Logic TECHNOLOGY')
@app.route('/test2/')
def test2():
    print(request.accept_languages)
    # Version en
    return render_template('main_pages/test/test2.html', title='Test2 | OPTO Logic TECHNOLOGY')

@app.route('/oled/')
def oled():
    print(request.accept_languages)
    # Version en
    return render_template('/main_pages/products/displays/oled/oled_landing_en.html' , title='OLED | OPTO Logic TECHNOLOGY')

@app.route('/epaper/')
def epaper():
    print(request.accept_languages)
    # Version en
    return render_template('/main_pages/products/displays/epaper/epaper_landing_en.html' , title='ePAPER | OPTO Logic TECHNOLOGY')

@app.route('/custom_displays/')
def custom_displays():
    print(request.accept_languages)
    # Version en
    return render_template('/main_pages/products/displays/custom_displays/custom_displays_landing_en.html' , title='Custom Displays | OPTO Logic TECHNOLOGY')

@app.route('/touch_panels/')
def touch_panels():
    print(request.accept_languages)
    # Version en
    return render_template('/main_pages/products/touch_panels/touch_panels_landing_en.html' , title='Touch Panels | OPTO Logic TECHNOLOGY')

@app.route('/computers/')
def computers():
    print(request.accept_languages)
    # Version en
    return render_template('/main_pages/products/computers/computers_landing_en.html' , title='Computers | OPTO Logic TECHNOLOGY')

@app.route('/others/')
def others():
    print(request.accept_languages)
    # Version en
    return render_template('/main_pages/products/others/others_landing_en.html' , title='Others | OPTO Logic TECHNOLOGY')

@app.route('/pcap/')
def pcap():
    print(request.accept_languages)
    # Version en
    return render_template('/main_pages/products/touch_panels/pcap_landing_en.html' , title='PCAP | OPTO Logic TECHNOLOGY')

@app.route('/rtp/')
def rtp():
    print(request.accept_languages)
    # Version en
    return render_template('/main_pages/products/touch_panels/rtp_landing_en.html' , title='RTP | OPTO Logic TECHNOLOGY')


