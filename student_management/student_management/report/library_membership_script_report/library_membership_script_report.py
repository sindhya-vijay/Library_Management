# Copyright (c) 2023, student and contributors
# For license information, please see license.txt

import frappe
from collections import defaultdict

def execute(filters=None):
    columns = [
        {"label": "Library Member", "fieldname": "library_member", "fieldtype": "Link", "options": "Library Member", "reqd": 0},
        {"label": "Full Name", "fieldname": "full_name", "fieldtype": "Data", "read_only": 1},
        {"label": "From Date", "fieldname": "from_date", "fieldtype": "Date"},
        {"label": "To Date", "fieldname": "to_date", "fieldtype": "Date"},
        {"label": "Paid", "fieldname": "paid", "fieldtype": "Check"},
    ]

    data = get_library_membership_data(filters)
   
    # Generate the pie chart data
    chart = get_chart_data(data)

    return columns, data, None, chart

def get_library_membership_data(filters):
    # Construct a query to fetch the required data, including "Full Name"
    query = """
        SELECT
            `library_member`,
            `from_date`,
            `to_date`,
            `paid`
        FROM
            `tabLibrary Membership`
    """

    if filters.get("library_member"):
        query += f" WHERE `library_member` = '{filters.get('library_member')}'"

    data = frappe.db.sql(query, as_dict=1)

    # Fetch the "Full Name" separately for each library member
    for row in data:
        library_member = row.get("library_member")
        if library_member:
            full_name = frappe.get_value("Library Member", library_member, "full_name")
            row["full_name"] = full_name

    return data
# def get_library_membership_data(filters):
#     # Construct a query to fetch the required data
#     query = """
#         SELECT
#             `library_member`,
#             `from_date`,
#             `to_date`,
#             `paid`
#         FROM
#             `tabLibrary Membership`
#     """

#     if filters.get("library_member"):
#         query += f" WHERE `library_member` = '{filters.get('library_member')}'"

#     data = frappe.db.sql(query, as_dict=1)

#     # Create a dictionary to aggregate data by library member
#     member_data = defaultdict(lambda: {
#         "library_member": None,
#         "full_name": None,
#         "from_date": None,
#         "to_date": None,
#         "paid": None,
#     })

#     for row in data:
#         library_member = row.get("library_member")
#         full_name = frappe.get_value("Library Member", library_member, "full_name")
#         if member_data[library_member]["from_date"] is None or row["from_date"] < member_data[library_member]["from_date"]:
#             member_data[library_member]["from_date"] = row["from_date"]
#         if member_data[library_member]["to_date"] is None or row["to_date"] > member_data[library_member]["to_date"]:
#             member_data[library_member]["to_date"] = row["to_date"]
#         member_data[library_member]["library_member"] = library_member
#         member_data[library_member]["full_name"] = full_name
#         member_data[library_member]["paid"] = row.get("paid")

#     # Convert the aggregated data to a list of dictionaries
#     consolidated_data = list(member_data.values())

#     return consolidated_data

def get_chart_data(data):
    # Initialize counters for the different date conditions
    blue_count = 0
    pink_count = 0
    red_count = 0

    for row in data:
        from_date = row.get("from_date")
        if from_date:
            # Check the date condition and update counts
            if from_date.month == 11:  # November
                blue_count += 1
            elif from_date.month == 10:  # October
                pink_count += 1
            else:
                red_count += 1

    chart = {
        "data": {
            "labels": ["November (Blue)", "October (Pink)", "Other Months (Red)"],
            "datasets": [
                {
                    "name": "Membership by Month",
                    "values": [blue_count, pink_count, red_count],
                    "colors": ["blue", "pink", "red"],
                }
            ]
        },
        "type": "pie",
        "height": 300,
    }

    return chart

