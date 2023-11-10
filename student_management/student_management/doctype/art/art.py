# Copyright (c) 2023, student and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe import _

def execute(filters):
    data = get_data(filters)
    columns = get_columns()

    return columns, data

def get_columns():
    return [
        {"label": _("Doc"), "fieldname": "doc", "fieldtype": "Data","width": 100},
        {"label": _("Date of Birth"), "fieldname": "date_of_birth", "fieldtype": "Date", "width": 100},
        {"label": _("Age"), "fieldname": "age", "fieldtype": "Data", "width": 100},
    ]

def get_data(filters):
    # Query the data from your doctype, including the Date of Birth
    data = frappe.db.sql("""
        SELECT name, date_of_birth FROM `tabYour DocType`
        WHERE ...  # Add your filters here
    """, as_dict=True)

    # Calculate age and add it to the data
    for record in data:
        if record.date_of_birth:
            today = frappe.utils.nowdate()
            dob = record.date_of_birth
            age = frappe.utils.getdate(today).year - frappe.utils.getdate(dob).year
            record.age = age

    return data
