from odoo import models, fields

class Instructor(models.Model):
    _name = 'escuela.instructor'
    _description = 'Instructor'

    name = fields.Char(string='Nombre', required=True)
    surname = fields.Char(string='Apellidos', required=True)
    department = fields.Char(string='Department')
    course_ids = fields.One2many('escuela.course', 'instructor_id', string='Cursos')