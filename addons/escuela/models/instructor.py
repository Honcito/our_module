from odoo import models, fields, api

class Instructor(models.Model):
    _name = 'escuela.instructor'
    _description = 'Instructor'

    name = fields.Char(string='Nombre', required=True)
    surname = fields.Char(string='Apellidos', required=True)
    department = fields.Char(string='Departamento')
    foto = fields.Binary(string='Foto')
    course_ids = fields.One2many('escuela.course', 'instructor_id', string='Cursos')
    course_names = fields.Char(string='Nombres de Cursos', compute='_compute_course_names')
    
    #Método para recuperar el nombre del curso y poder añadirlo a la lista de profesores
    @api.depends('course_ids')
    def _compute_course_names(self):
        for instructor in self:
            instructor.course_names = ', '.join(instructor.course_ids.mapped('name'))
