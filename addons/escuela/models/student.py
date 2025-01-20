from odoo import models, fields

class Student(models, Model):
    _name = 'custom.student'
    _description = 'Student'

    name = fields.Char(string='Nombre', required=True)
    surname = fields.Char(string='Apellidos', required=True)
    phone = fields.Char(string='Telefono')
    email = fields.Char(string='Email')
    course_ids = fields.Many2many('custom.course', string='Cursos')
