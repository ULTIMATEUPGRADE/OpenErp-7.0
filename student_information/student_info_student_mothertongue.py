from openerp.osv import orm, fields

class student_info_student_mothertongue(orm.Model):
    _name = "student.info.student"
    _inherit="student.info.student"
    _columns = {
        'm_tongue':fields.selection([('T','Tamil'),('E','English'),('F','French')],"Mother Tongue"),
    }
    
    