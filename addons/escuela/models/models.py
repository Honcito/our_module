# -*- coding: utf-8 -*-
from odoo import models, fields
 
class profesor(models.Model):
    _name = 'escuela.profesor'
    _description = 'profesor'
    
    name = fields.Char(string='Nombre', required=True)
    surname = fields.Char(string='Apellido', required=True)
    age = fields.Integer(string='Edad')