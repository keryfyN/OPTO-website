from application import app
from flask import render_template, request

"""
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


@app.route('/products/displays/')
def displays():
    print(request.accept_languages)
    # Version en
    #return render_template('main_pages/products', title='TFT | OPTO Logic TECHNOLOGY')
    return render_template('/main_pages/products/displays/displays_landing_en.html' , title='Displays | OPTO Logic TECHNOLOGY')

"""