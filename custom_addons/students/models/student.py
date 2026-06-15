from odoo import fields, models


class StudentStudent(models.Model):
    _name = 'student.student'
    _description = 'Student'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    date_of_birth = fields.Date(string='Date of Birth')
    active = fields.Boolean(default=True)
