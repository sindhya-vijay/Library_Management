// Copyright (c) 2023, student and contributors
// For license information, please see license.txt

frappe.ui.form.on('art', {
    // refresh: function(frm) {
    //     // Add a button to calculate the age manually
    //     frm.add_custom_button(__('total'), function() {
    //         dop(frm);
    //     });
    },

    // date_of_birth: function(frm) {
    //     calculate_age(frm);
    // }
// });

// function dop(frm) {
//     var dop = frm.doc.date_of_birth;
//     if (dop) {
//         // Calculate the age
//         var today = frappe.datetime.get_today();
//         var birthDate = frappe.datetime.obj_to_str(dop);
//         var total = today.year - birthDate.year - (today.month < birthDate.month || (today.month === birthDate.month && today.day < birthDate.day) ? 1 : 0);

//         // Set the age field with the calculated age
//         frm.set_value('total', total);
//     }
// }