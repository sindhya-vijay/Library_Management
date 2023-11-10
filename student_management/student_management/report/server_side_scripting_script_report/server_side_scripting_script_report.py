import frappe
from frappe import _, msgprint

def execute(filters=None):
    print("Executing report with filters:", filters)
    if not filters:
        filters = {}

    columns, data = [], []
    columns = ge_columns()
    cs_data = get_cs_data(filters)

    if not cs_data:
        msgprint(_('No records found'))
        return columns, cs_data

    data = []
    for d in cs_data:
        row = frappe._dict({
            'first_name': d.first_name,
            'dob': d.dob,
            'age': d.age
        })
        data.append(row)

    return columns, data

def ge_columns():
    return [
        {
            'fieldname': 'first_name',
            'label': _('Name'),
            'fieldtype': 'Date',
            'width': '120'
        },
        {
            'fieldname': 'dob',
            'label': _('DOB'),
            'fieldtype': 'Date',
            'width': '120'
        },
        {
            'fieldname': 'age',
            'label': _('Age'),
            'fieldtype': 'Data',
            'width': '120'
        },
    ]

def get_cs_data(filters):
    conditions = get_conditions(filters)
    print("Filter conditions:", conditions)
    data = frappe.get_all(
        doctype='Server Side Scripting',
        fields=['first_name', 'dob', 'age'],
        filters=conditions,
        order_by='first_name desc'
    )
    return data

def get_conditions(filters):
    conditions = {}
    for key, value in filters.items():
        if filters.get(key):
            conditions[key] = value

    return conditions