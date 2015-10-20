# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

computers = Blueprint('computers', __name__, url_prefix='/products/computers')


# Landing
@computers.route('/')
def computer_landing_en():
    return render_template('/computers/computers_landing_en.html', title='COMPUTERS | OPTO Logic TECHNOLOGY')


# Details
@computers.route('/<int:computer_id>/details')
def computers_details(computers_id):
    return render_template('/computers/computers_details.html', computers_id=computers_id)

# computer/industrial_pcs
@computers.route('/industrial_pcs')
def industrial_pcs():
    return render_template('/computers/industrial_pcs.html', title='INDUSTRIAL PCs | OPTO Logic TECHNOLOGY')

# computer/monitors
@computers.route('/monitors')
def monitors():
    return render_template('/computers/monitors.html', title='MONITORS | OPTO Logic TECHNOLOGY')

# computer/som_system_on_module
@computers.route('/som_system_on_module')
def som_system_on_module():
    return render_template('/computers/som_system_on_module.html', title='SOM SYSTEM ON MODULE | OPTO Logic TECHNOLOGY')



