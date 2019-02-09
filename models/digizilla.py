from odoo import models, fields, api


class digizilla(models.Model):
    _name = 'digizilla.digizilla'
    _inherit = ['mail.thread']

    name = fields.Char(string='Name', required=True, track_visibility="always")
    join_date = fields.Date(track_visibility="always")
    country = fields.Char(track_visibility="always")
    gender = fields.Selection([('Male', 'Male'), ('Female', 'Female')], default='Male', track_visibility="always")
    related_customer = fields.Many2many('res.partner', domain="[('customer','=',True)]", track_visibility="always")
    company = fields.Many2one('res.partner', domain="[('is_company','=',True)]", track_visibility="always")
    notes = fields.Text(track_visibility="always")
    notebook = fields.Char(track_visibility="always")
