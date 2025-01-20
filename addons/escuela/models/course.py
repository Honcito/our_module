# -*- coding: utf-8 -*-
from odoo import models, fields
 
class Course(models.Model):
    _name = 'custom.course'
    _description = 'Course'

    name = fields.Char(string='Nombre', required=True)
    surname = fields.Text(string='Descripcion')
    schedule = fields.Datetime(string='Horario')
    instructor_id = fields.Many2one('custom.instructor', string='Instructor')
    student_ids = fields.Many2many('custom.student', string='Estudiantes')