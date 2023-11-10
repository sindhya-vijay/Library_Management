// Copyright (c) 2023, student and contributors
// For license information, please see license.txt


frappe.ui.form.on('Library Member', {
    refresh: function(frm) {
        frm.add_custom_button('Create Membership', () => {
            frappe.new_doc('Library Membership', {
                library_member: frm.doc.name
            })
        })
        frm.add_custom_button('Create Transaction', () => {
            frappe.new_doc('Library Transaction', {
                library_member: frm.doc.name
            })
        })
    }
});
frappe.ui.form.on('Library Member', {
    dob: function(frm) {
        if (frm.doc.dob) {
            var dob = new Date(frm.doc.dob);
            var today = new Date();
            var age = today.getFullYear() - dob.getFullYear();
            frm.set_value('age', age);
        } else {
            frm.set_value('age', '');
        }
    }
});