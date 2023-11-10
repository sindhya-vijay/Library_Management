// Copyright (c) 2023, student and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["server side scripting script report"] = {
	"filters": [
		{
			"fieldname": "name",
			"label":__("Server Side Scripting"),
			"filedtype": "Link",
			"options": "Server Side Scripting"
		},

		{
			"fieldname": "dob",
			"label":__("Server Side Scripting"),
			"filedtype": "Date"
		},
		{
			"fieldname": "age",
			"label":__("Server Side Scripting"),
			"filedtype": "Data"
		}

	],
	"onload": function(report) {
        // Set a default filter value or perform any other actions when the report loads
        // Example: report.set_filter_value("library_member", "LM00001");
    },
    "formatter": function(value, row, column, data, default_formatter) {
        // Customize the formatting of specific columns if needed
        // Example: if (column.fieldname === "paid") { return value ? _("Yes") : _("No"); }
        return default_formatter(value, row, column, data);
    }
};
	
