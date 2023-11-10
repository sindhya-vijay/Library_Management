# Copyright (c) 2023, student and contributors
# For license information, please see license.txt

import frappe
import re
from frappe.model.document import Document

class clientsidescripting(Document):
    def validate(self):
        if self.email and not self.validate_email(self.email):
            frappe.throw("Invalid email address")

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)
