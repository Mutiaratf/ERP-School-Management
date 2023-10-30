# Mandatory
from odoo import api, models, fields

class Student(models.Model):
  _name = 'school_management.subject' 
  _description = 'model Mata Pelajaran' 
  _rec_name = 'subject_name'


  subject_type = fields.Selection([
      ('u', 'Umum'),
      ('j', 'Jurusan'),
  ], default=False, string='Tipe Mata Pelajaran')
  subject_name = fields.Char(string="Nama Mata Pelajaran")



