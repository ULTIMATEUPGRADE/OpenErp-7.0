from openerp.osv import orm, fields

class student_Ginfo_student(orm.Model):
    _name = "student.ginfo.student"
    _rec_name = "student_id"
    _inherits = {"student.info.student":"student_id"}
    
#     def _total_marks(self,cr,uid,ids,field_name=None,args=None,context=None):
#         res={}
#         for record in self.browse(cr, uid, ids, context=context):
#             if record.id not in res:
#                 res.update({record.id: {}})
#             res[record.id]['total']=(record.maths)+(record.physics)+(record.chem)
#         return res
    
    def calculate_volume(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
#             print record.id
#             print record.maths+record.chem+record.physics
            if record.id not in res:
                res.update({record.id: {}})
            res[record.id]['total'] = record.maths + record.chem + record.physics
            res[record.id]['average'] = res[record.id]['total'] / 3
        return res
    
    def _printtt(self, cr, uid, ids, field_names, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            a = record.n_present
            res[record.id] = (float(a) / 30) * 100
        return res
    def _print_rev(self, cr, uid, id, name, value, args, context=None):
        return self.write(cr, uid, [id], {'n_present':value and (value * 30) / 100})
    
    def _search_volume(self, cr, uid, obj, name, args, context=None):
        argoptr=args[0][1]
        argopnd=str(args[0][2])
#         res = {}
#         return_ids = []
#         search_ids = self.search(cr, uid, [],context=context)
#         for record in self.browse(cr, uid, search_ids, context=context):
#             if record.total == argopnd:
#                 return_ids.append(record.id)
#                 
#         return [('id','in',return_ids)]
        cr.execute('select id from student_ginfo_student where maths+chem+physics'+argoptr+''+argopnd)
        res= cr.fetchall()
        print res,args
        return [('id', 'in', [x[0] for x in res])]
    
    def std_select(self,cr,uid,ids,context=None):
        res={}
        for a in self.browse(cr,uid,ids,context=context):
            b = a.s_std
            
            print b
        return True
#  domain=[('c_class','ilike',)           
    
    _columns = {
        's_std':fields.selection([(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)],string="Class"),
        'student_id':fields.many2one("student.info.student", "Student Name", required=True, ondelete="cascade"),
        'ex_age':fields.related('student_id','age',type='integer',string="Age"),
        'height':fields.char("Height"),
        'weight':fields.char("Weight"),
        'maths':fields.integer('Maths'),
        'physics':fields.integer('Physics'),
        'chem':fields.integer('Chemistry'),
        'total':fields.function(calculate_volume, fnct_search=_search_volume, string="Total Marks", multi="calculate_mpc"),
        'average':fields.function(calculate_volume, fnct_search=_search_volume, string="Average", multi="calculate_mpc"),
        'n_present':fields.integer(string="Present"),
        't_percent':fields.function(_printtt, string="Total_percentage", fnct_inv=_print_rev, type='float', 
                                    store={
                                            'student.ginfo.student': (lambda self, cr, uid, ids, c={}: ids, ['n_present'], 20),
                                            },)
    }
    
    _defaults={
        'height':'160'
               }
    
    
