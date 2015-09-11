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

@app.route('/contact/')
def contact():
    print(request.accept_languages)
    # Version en
    return render_template('main_pages/contact/contact_en.html', title='Contact | OPTO Logic TECHNOLOGY')

@app.route('/lcd/')
def lcd():
    print(request.accept_languages)
    # Version en
    return render_template('main_pages/products/displays/graphic_lcd/graphic_lcd_landing_en.html', title='Graphic LCD | OPTO Logic TECHNOLOGY')
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

