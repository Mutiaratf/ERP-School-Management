# Mandatory
from odoo import api, models, fields

class Build(models.Model):
  _name = 'school_management.build' 
  _description = 'model Gedung' 
  _rec_name = 'build'

  build = fields.Selection([
    ('gedung_umum', 'Gedung Umum'),
    ('gedung_jurusan', 'Gedung Jurusan')
], default=False, string='Gedung')