from openerp.osv import orm, fields
from datetime import date
from datetime import datetime

class student_info_student(orm.Model):
    _name = "student.info.student"
    _rec_name="name"
    _columns = {
        'name':fields.char("Name", size=30, required=True),
        'age':fields.integer(),
        'fname':fields.char("Father Name", size=30),
        'mname':fields.char(size=30),
        'dob':fields.date(),
        'a_class':fields.char(),
        'a_class_date':fields.date("Join Date"),
        'c_class_date':fields.date("AStart Date"),
        'c_class':fields.char(),
        'address':fields.char(),
        'street':fields.char(),
        'state':fields.char(),
        'pincode':fields.char(),
        'country':fields.many2one("res.country"),
        'l_line':fields.char(size=12),
        'c_no':fields.char(size=13),
        's_img':fields.binary(),
        'room_id':fields.many2one('student.info.classroom'),
        'ref':fields.reference('Refered By', [('res.partner', 'Partner')], size=20),
        'state':fields.selection([('draft','draft'),('trashed','trashed')],string="Status"),
        'unique_test' : fields.char('Uniques Test'),
        'check_test' : fields.char('Check Test'),
        'not_null_test' : fields.char('Not null test', required="1"),
        'method_test' : fields.char('method test'),
    }
    
    _sql_constraints = [
         ('unique_test', 'UNIQUE(unique_test)', 'Unique error'),
         ('check_test', 'CHECK(check_test IS NOT NULL)', 'Check error'),
    ]
    
    def test_test(self, cr, uid, ids, context=None):
        if True:
            return True
        return False

    _constraints = [
        (test_test, 'Test', ['method_test']),
    ]
    
    def search_stud(self, cr, uid, ids, dob, context=None):
            a = datetime.strptime(dob , '%Y-%m-%d')
            b = date.today().year
            c = a.year
            f = b - c
            return {'value':{'age':f}}
        
    def orm_test(self, cr, uid, ids, context=None):
        a= self.search(cr,uid,[],context=context)
        res={}
        for b in self .browse(cr,uid,ids,context=None):
            c = b.name
        print c 
        print "OK"
        return res
    
class res_partner(orm.Model):
    _inherit = 'res.partner'
    
    _columns = {
        'ptype':fields.selection([('a', 'Internet Baanking'), ('b', 'Credit Card Purchase'), ('c', 'COD')], string="Payment Type")
    }
    
class sale_order(orm.Model):
    _inherit = "sale.order"
    
    _columns = {
        'ptype':fields.selection([('a', 'Internet Baanking'), ('b', 'Credit Card Purchase'), ('c', 'COD')], string="Payment Type")
    }
    
    def onchange_partner_id(self, cr, uid, ids, partner_id, context=None):
        res = super(sale_order, self).onchange_partner_id(cr, uid, ids, partner_id, context=context)
        if partner_id:
            result = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context)
            res['value']['ptype'] = result.ptype
        else:
            result = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context)
            res['value']['ptype'] = False
            
        print res
        print "OK"
        
        return res
    

    
    
    
    
    
    
