# Copyright (c) 2023, student and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe import _

class ServerSideScripting(Document):
#     @frappe.whitelist()
#     def frm_call(self,msg):
#         import time
#             time.sleep(10)
#             frappe.msgprint(msg)
#             self.mob
#         return "Hi this message from frm_call"







        def validate(self):
            self.get_document()
            for row in self.get("family_members"):
                frappe.msgprint(_("{0}. The family member is '{1}' and relation is '{2}'").format(row.idx, row.name1, row.relation))


    # -------------------------get_document------------------------------



        def get_document(self):
            doc = frappe.get_doc('client side scripting', self.client_side_doc)
            frappe.msgprint(_("The first name is {0} and Age is {1}").format(doc.first_name,doc.age))

            for row in doc.get("family_members"):
                frappe.msgprint(_("{0}. The family member name is '{1}' and relation is '{2}'").format(row.idx, row.name1, row.relation))
        # frappe.new_doc(doctype)



    # ------------------------ create new document------------------------

    #         def validate(self):
    #             self.new_document()

    #         def new_document(self):
    #             doc=frappe.new_doc('client side scripting')
    #             doc.first_name = 'jake'
    #             doc.last_name = 'jay'
    #             doc.age = 14


    #             doc.insert()

    # # -------------------------delete document------------------------
    # frappe.delete_doc(doctype,name) 
        # def validate(self):
        #     frappe.delete_doc('client side scripting', 'PR0012')




    # -------------------------------doc.insert()-----------------------------------

        # def validate(self):
        #     self.new_document()

        # def new_document(self):
        #     doc = frappe.new_doc('client side scripting')
        #     doc.forst_name ='Bally'
        #     doc.age =13
        #     doc.insert()


    # ------------------------------DOC.DB_SET()------------------------------------

        # def validate(self):
        #     self.db_set_document()

        # def db_set_document(self):
        #     doc = frappe.get_doc('client side scripting', 'PR0012')
        #     doc.db_set('age',45)


    # ----------------------db.get_list()-------------------------------------------------

        # def validate(self):
        #     self.get_list()

        # def get_list(self):
        #     doc = frappe.db.get_list('client side scripting',
        #             filters={
        #                 'enable':1
        #             },
        #             fields=['first_name','age']

            
        #     )

        #     for d in doc:
        #         frappe.msgprint(_("The parent first name is {0} and age is {1}").format(d.first_name, d.age))


        #------------------------- get_value() and set_value()----------------------------------------------

            # def validate(self):
            #     self.get_value()
            # def get_value(self):
            #     first_name, age= frappe.db.get_value('client side scripting','PR0012', ['first_name','age'])
            #     frappe.msgprint(_("The parent First name is {0} and age is {1}").format(first_name,age))



            # ---------------------set_value()-----------------------------------
                    #  def validate(self):
                    #     self.set_value()
                    #  def set_value(self):
                    #     frappe.db.set_value('client side scripting','PR0012', 'age', 25)
                    #     first_name, age= frappe.db.get_value('client side scripting','PR0012', ['first_name','age'])
                    #     frappe.msgprint(_("The parent First name is {0} and age is {1}").format(first_name,age))

            # -----------------------------------exists() and count()---------------------------------


            # def validate(self):
            #     if frappe.db.exists('client side scripting','PR0018'):
            #         frappe.msgprint(_("The Document is exists in database"))
            #     else:
            #         frappe.msgprint(_("The Document does not exists in database"))



            # def  validate(self):
            #     doc_count = frappe.db.count('client side scripting',{'enable':1})
            #     frappe.msgprint(_("The enable document count is {0}").format(doc_count))


            # -------------------------------------SQL QUERIES------------------------------------------------


            # def validate(self):
            #     self.sql()

            # def sql(self):
            #     data = frappe.db.sql("""
            #         SELECT 
            #             first_name,
            #             age
            #         FROM 
            #             `tabclient side scripting`
            #         WHERE
            #             enable = 1
            #     """, as_dict=1)
            #     for d in data:
            #         # frappe.msgprint(_("The parent First name is {0} and age is {1}").format(d.first_name, d.age))
            #         frappe.msgprint(_("Saved"))