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
    course_names = fields.Char(string='Nombres de los Cursos', compute='_compute_course_names', store=True)
     
    #Método para recuperar el nombre del curso y poder añadirlo a la lista de estudiantes
    @api.depends('course_ids')
    def _compute_course_names(self):
        for student in self:
            student.course_names = ', '.join(student.course_ids.mapped('name'))