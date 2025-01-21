from odoo import models, fields, api

class Student(models.Model):
    _name = 'escuela.student'
    _description = 'Student'

    name = fields.Char(string='Nombre', required=True)
    surname = fields.Char(string='Apellidos', required=True)
    phone = fields.Char(string='Telefono')
    email = fields.Char(string='Email')
    foto = fields.Binary(string='Foto')
    course_ids = fields.Many2many('escuela.course', string='Cursos')

