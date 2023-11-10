# Copyright (c) 2023, student and contributors
# For license information, please see license.txt
from frappe.model.document import Document
from datetime import datetime

# class LibraryMember(Document):
#     # This method will run every time the form is loaded or refreshed
#     def validate(self):
#         self.full_name = f'{self.first_name} {self.last_name or ""}'

#         # Calculate the age and set the value in the age field
#         if self.dob:
#             dob_str = self.dob.strftime('%Y-%m-%d')  # Convert datetime.date to string
#             dob = datetime.strptime(dob_str, '%Y-%m-%d')
#             today = datetime.now()
#             age = today.year - dob.year

#             # Check if the birthdate for this year has not occurred yet
#             if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
#                 age -= 1  # Adjust the age if the birthdate for this year has not occurred yet

#             self.set("age", age)

import re
import frappe

class LibraryMember(Document):
    # This method will run every time the form is loaded or refreshed
    def validate(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'

        # Email validation
        if self.email_address and not self.validate_email(self.email_address):
            frappe.throw("Invalid email address")

        if self.last_name is None or self.last_name == '':
            frappe.throw("Please fill Last Name field")


        if self.first_name is None or self.first_name == '':
            frappe.throw("Please fill first Name field")

        # Phone validation
        if self.phone:
            if not self.validate_phone(self.phone):
                frappe.throw("Invalid phone number. Please enter exactly 10 digits.")

        # Calculate the age and set the value in the age field
        if self.dob:
            dob = datetime.strptime(self.dob, '%Y-%m-%d')
            today = datetime.now()

            age = today.year - dob.year

            # Check if the birthdate for this year has not occurred yet
            if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
                age -= 1  # Adjust the age if the birthdate for this year has not occurred yet

            self.set("age", age)

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    def validate_phone(self, phone):
        return len(phone) == 10 and phone.isdigit()
