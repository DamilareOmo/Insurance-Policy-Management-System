"""
policyholder.py

Defines the Policyholder class used to represent and manage
individuals enrolled in the insurance company's policies.
"""

from datetime import date


class Policyholder:
    """Represents a single policyholder and their account status."""

    def __init__(self, member_id, name, email, phone):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.status = "Active"          # Active, Suspended
        self.registered_on = date.today()
        self.product = None             # Product currently subscribed to
        self.payment_history = []       # List of Payment objects

    def register(self):
        """Mark the policyholder as active (used for new sign-ups)."""
        self.status = "Active"
        print(f"[REGISTERED] {self.name} (ID: {self.member_id}) is now Active.")

    def suspend(self):
        """Suspend the policyholder, e.g., due to non-payment."""
        if self.status == "Suspended":
            print(f"[INFO] {self.name} is already suspended.")
            return
        self.status = "Suspended"
        print(f"[SUSPENDED] {self.name} (ID: {self.member_id}) has been suspended.")

    def reactivate(self):
        """Reactivate a previously suspended policyholder."""
        if self.status == "Active":
            print(f"[INFO] {self.name} is already active.")
            return
        self.status = "Active"
        print(f"[REACTIVATED] {self.name} (ID: {self.member_id}) is now Active again.")

    def assign_product(self, product):
        """Attach an insurance product to this policyholder."""
        self.product = product
        print(f"[PRODUCT ASSIGNED] {self.name} subscribed to '{product.name}'.")

    def add_payment(self, payment):
        """Record a payment made by this policyholder."""
        self.payment_history.append(payment)

    def display_details(self):
        """Print a summary of the policyholder's account."""
        print("-" * 50)
        print(f"Policyholder ID : {self.member_id}")
        print(f"Name            : {self.name}")
        print(f"Email           : {self.email}")
        print(f"Phone           : {self.phone}")
        print(f"Status          : {self.status}")
        print(f"Registered On   : {self.registered_on}")
        print(f"Product         : {self.product.name if self.product else 'None'}")
        print("Payment History :")
        if not self.payment_history:
            print("    No payments made yet.")
        else:
            for p in self.payment_history:
                print(f"    {p}")
        print("-" * 50)

    def __str__(self):
        return f"Policyholder({self.member_id}, {self.name}, {self.status})"
