# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, redirect, url_for
from .forms import ContactForm


frontend = Blueprint('frontend', __name__)

@frontend.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate():
        print('Form subject : %s' %form.subject)
        print('Form name : %s' %form.name)
        print('Form email : %s' %form.email)
        print('Form message : %s' %form.message)
        return redirect(url_for('frontend.index'))
    return render_template('/frontend/contact_en.html', title='Contact | OPTO Logic TECHNOLOGY', form=form)



@frontend.route('/')
@frontend.route('/index/')
def index():
    # Version FR
    if request.accept_languages[0][0] == 'fr-CH' or request.accept_languages[0][0] == 'fr-FR' or \
                    request.accept_languages[0][0] == 'fr':
        return render_template('/frontend/index_fr.html', title='OPTO Logic TECHNOLOGY')

    # Version DE
    if request.accept_languages[0][0] == 'de':
        return render_template('/frontend/index_de.html', title='OPTO Logic TECHNOLOGY')

    # DEFAULT Version EN
    return render_template('/frontend/index_en.html', title='OPTO Logic TECHNOLOGY')


