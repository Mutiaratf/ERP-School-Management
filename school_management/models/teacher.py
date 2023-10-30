# Mandatory
from odoo import api, models, fields

class Teacher(models.Model):
  _name = 'school_management.teacher' 
  _description = 'model Guru' 
  _rec_name = 'teacher_name'


  teacher_id = fields.Char(string="NIP")
  teacher_name = fields.Char(string="Nama Guru", required=True)
  gender = fields.Selection([
      ('p', 'Perempuan'),
      ('l', 'Laki - laki')
  ], string="Jenis Kelamin", default=False)

  active = fields.Boolean(string="Aktif", default=False)



