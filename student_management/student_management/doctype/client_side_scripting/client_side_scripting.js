// Copyright (c) 2023, student and contributors
// For license information, please see license.txt

frappe.ui.form.on('client side scripting', {
	
    // refresh: function(frm){
        // frappe.msgprint("Hello Sindhya")
        // frappe.throw("This is an error")
    

    // onload: function(frm){
        // frappe.msgprint("Hello from onload event")


        // validate: function(frm){
        //     frappe.throw("Validate event")


        // }
        // before_save: function(frm){
        //     frappe.throw("Before save event")

        // }
        // after_save: function(frm){
        //     frappe.throw("After save event")

        // }
        // enable: function(frm){
        //     frappe.msgprint("Enable field event")

        // },
        // age: function(frm){
        //     frappe.msgprint("Age Field eevent")

        // }
        // family_members_on_form_rendered: function(){
        //     frappe.msgprint("Hello this is from family member child table")

        // }
        // before_submit: function(frm){
        //     frappe.throw("before_save event")

        // }
        // on_submit: function(frm){
        //     frappe.msgprint("on_submit event")

        // }
        // before_cancel: function(frm){
        //     frappe.throw("before_cancel event")
        
        // }
        // after_cancel: function(frm){
        //     frappe.msgprint("after_cancel event")
        // }
        

        // frm.doc.first_name
        // after_save: function(frm){
        //     frappe.msgprint(__("The full name is '{0}'",
        //         [frm.doc.first_name+" "+frm.doc.last_name]))

        //     for (let row of frm.doc.family_members){
        //         frappe.msgprint(__("{0}. The family member name is '{1}' and relation is '{2}'"
        //             [row.idx,row.name1,row.relation]))
        //     }



        // }
        validate: function(frm) {
			if (!frm.doc.dob) {
				frappe.msgprint("DOB is required.");
				frappe.validated = false;
			}
            if (!frm.doc.age) {
				frappe.msgprint("age is required.");
				frappe.validated = false;
			}
            

		}

        // --------------------------------set_value----------------------
            // validate: function(frm){
            //     frm.set_value('full_name', frm.doc.first_name +" "+ frm.doc.last_name)
           
                
            //     let row = frm.add_child('family_members',{
            //         name1: 'Deepak',
            //         relation: 'Father',
            //         age: 40
            //     })
        
        
        
            // }
         
        // --------------------------------------- Client Side Scripting || set_value & add_child || set_df_property || add_custom_button--------------------

            //     enable: function(frm){
            //     //     frm.set_df_property('first_name','reqd',1)
            //     // 

            //     frm.set_df_property('last_name','read_only',1)
            //     frm.toggle_reqd('age',true)
            // }
        // ---------------------------------------------------------------------------------------------------------------------------------------------------

        //--------------------------- Add custom button-------------------------------------------------------------------------------------------------------



        // refresh: function(frm){

        //     frm.add_custom_button('click me',()=>{
                
        //         frappe.msgprint(__('you clicked me!!'));

        //     })



        // //     frm.add_custom_button('click me1',()=>{
        // //         frappe.msgprint(__('you clicked 1'));
        // //     }, 'click me')

        // //     frm.add_custom_button('click me2',()=>{
        // //         frappe.msgprint(__('you clicked 2'));
        // //     }, 'click me')
        // }
    
    });

        
        
