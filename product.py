"""
product.py

Defines the Product class used to represent insurance policy
products offered by the company (e.g., Health, Auto, Life plans).
"""


class Product:
    """Represents an insurance product/plan offered to policyholders."""

    def __init__(self, product_id, name, premium, coverage_details):
        self.product_id = product_id
        self.name = name
        self.premium = premium                  # Monthly premium amount
        self.coverage_details = coverage_details
        self.status = "Active"                   # Active, Suspended/Removed

    def update(self, name=None, premium=None, coverage_details=None):
        """Update one or more attributes of the product."""
        if name is not None:
            self.name = name
        if premium is not None:
            self.premium = premium
        if coverage_details is not None:
            self.coverage_details = coverage_details
        print(f"[PRODUCT UPDATED] '{self.name}' (ID: {self.product_id}) details updated.")

    def suspend(self):
        """Suspend/remove this product from being offered."""
        self.status = "Suspended"
        print(f"[PRODUCT SUSPENDED] '{self.name}' (ID: {self.product_id}) is no longer offered.")

    def reactivate(self):
        """Reactivate a suspended product."""
        self.status = "Active"
        print(f"[PRODUCT REACTIVATED] '{self.name}' (ID: {self.product_id}) is now offered again.")

    def display_details(self):
        """Print a summary of the product."""
        print("-" * 50)
        print(f"Product ID   : {self.product_id}")
        print(f"Name         : {self.name}")
        print(f"Premium      : ${self.premium:.2f}/month")
        print(f"Coverage     : {self.coverage_details}")
        print(f"Status       : {self.status}")
        print("-" * 50)

    def __str__(self):
        return f"Product({self.product_id}, {self.name}, ${self.premium:.2f}, {self.status})"
