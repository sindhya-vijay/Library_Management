// Copyright (c) 2023, student and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Library Membership Report"] = {
    "filters": [
        {
            "fieldname": "library_member",
            "label": __("Library Member"),
            "fieldtype": "Link",
            "options": "Library Member",
            "reqd": 0
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
