from odoo import api, models, fields

class RoomClass(models.Model):
    _name = 'school_management.room_class' 
    _description = 'model Ruangan Kelas' 
    _rec_name = 'major'

    room_id = fields.Char(string='Nomor Ruangan') 
    level = fields.Many2one(comodel_name='school_management.level',string='Tingkat')
    major = fields.Many2one(comodel_name='school_management.major',string='Jurusan')
    subject_name = fields.Many2one(comodel_name='school_management.subject', string='Mata Pelajaran')
    teacher_name = fields.Many2one(comodel_name='school_management.teacher',string='Nama Guru')
    lesson_time = fields.Float(string="Jam Pembelajaran", default=1.0)
    build = fields.Many2one(comodel_name='school_management.build',string='Gedung')
    absensi_ids = fields.One2many(comodel_name='school_management.absensi', inverse_name='class_id')
    status = fields.Selection([
        ('rancangan', 'Rancangan'),
        ('selesai', 'Selesai')
    ], default="rancangan", string='Status', tracking=True)

        # Notif Pedding
    def rancangan_button(self):
        self.status = 'rancangan'

    def selesai_button(self):
        self.status = 'selesai'

class Absensi(models.Model):
    _name = 'school_management.absensi' 
    _description = 'model Ruangan Kelas' 
    _rec_name = 'class_id'

    class_id = fields.Many2one('school_management.room_class')
    nis_id = fields.Char(string="NIS")
    student_name = fields.Many2one(comodel_name='school_management.student', string="Nama Siswa")
    state = fields.Selection([
        ('hadir', 'Hadir'),
        ('alfa', 'Alfa'),
        ('sakit', 'Sakit'),
        ('izin', 'Izin'),
    ], string="Keterangan", default=False, required=True)
    student_ids = fields.One2many(comodel_name='school_management.student', inverse_name='absensi_ids')

    @api.onchange('student_name')
    def set_student(self):
        self.nis_id = self.student_name.nis_id
