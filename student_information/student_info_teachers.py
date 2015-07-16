from openerp.osv import orm,fields

class student_info_teachers(orm.Model):
    _name="student.info.teachers"
    _columns={
        'name':fields.char('Teachers',size=30),
        'address':fields.char('Address',size=30),
        'address1':fields.char(size=30),
        'city':fields.char(size=30),
        'pin':fields.char(size=30),
        'country_id':fields.many2one('res.country'),
        'room_id1':fields.many2one("student.info.classroom")
        }