frappe.ready(function() {
    frappe.web_form.on('enable', (Field, value) => {
        frappe.msgprint('Hi user');
    });

    // frappe.web_form.on('load', () => {
    //     frappe.msgprint('Please fill in all values');
    // });

	

	frappe.web_form.on('dob', (Field, value) => {
		console.log('Date of Birth changed:', value);
		if (value) {
			dob = new Date(value);
			var today = new Date();
			var age = Math.floor((today - dob) / (365.25 * 24 * 60 * 60 * 1000));
			frappe.web_form.set_value('age', age); // Assuming 'age' is the fieldname for the age field
		}
		

	
	});
	


});
