
from odoo import models, fields, api

class MyWizard(models.TransientModel):
    _name = 'my.wizard'
    _description = 'My Wizard'

    name = fields.Char(string="Wizard Name")
