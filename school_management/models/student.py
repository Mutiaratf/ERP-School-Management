# Mandatory
from odoo import api, models, fields

class Siswa(models.Model):
  _name = 'school_management.student' 
  _description = 'model Murid' 
  _rec_name = 'student_name'

  nis_id = fields.Char(string="NIS")
  student_name = fields.Char(string="Nama Siswa", required=True)
  gender = fields.Selection([
      ('p', 'Perempuan'),
      ('l', 'Laki - Laki')
  ], default=False, string='Jenis Kelamin', required=True)
  date_of_birth = fields.Date(string="Tanggal Lahir", required=True)
  level = fields.Many2one(comodel_name='school_management.level',string='Tingkat', required=True)
  major = fields.Many2one(comodel_name='school_management.major',string='Jurusan', required=True)
  absensi_ids = fields.One2many(comodel_name='school_management.absensi', inverse_name='student_ids')

