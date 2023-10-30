{
    "name": "School Management (SM)",
    "version": "16.0.1.0.0",
    "author": "Mutiara Tari Fadilah",
    "category": "Extra Tools",
    "license": "LGPL-3",
    "depends": ["contacts"],
    "data": [
        'security/ir.model.access.csv',
        'views/admin/level_admin.xml',
        'views/admin/major_admin.xml',
        'views/admin/build_admin.xml',
        'views/admin/teacher_admin.xml',
        'views/admin/subject_admin.xml',
        'views/admin/student_admin.xml',
        'views/admin/room_class_admin.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'icon': 'school_management,static/description/icon.png'
}
