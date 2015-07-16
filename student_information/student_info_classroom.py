from openerp.osv import orm,fields

class student_info_classroom(orm.Model):
    _name="student.info.classroom"
    _rec_name="name"
    _columns={
        'name':fields.char('Class Room',size=30),
        'student_id':fields.one2many('student.info.student','room_id','List of Students'),
        'teachers_id':fields.many2many('student.info.teachers','student_info_teachers_teacher_id','teachers_id','room_id1','Teachers'),
    }
    
