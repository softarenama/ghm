
from odoo import http

class MyController(http.Controller):
    @http.route('/my_model', auth='public')
    def index(self, **kw):
        return "Hello from My Controller"
