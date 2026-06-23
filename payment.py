"""
payment.py

Defines the Payment class used to represent and manage payments
made by policyholders, including reminders and late penalties.
"""

from datetime import date


class Payment:
    """Represents a single payment transaction tied to a policyholder."""

    PENALTY_RATE = 0.05  # 5% penalty applied on late payments

    def __init__(self, payment_id, policyholder, product, amount_due):
        self.payment_id = payment_id
        self.policyholder = policyholder
        self.product = product
        self.amount_due = amount_due
        self.amount_paid = 0.0
        self.status = "Pending"     # Pending, Paid, Late
        self.date_paid = None

    def process_payment(self, amount):
        """Process a payment for the policyholder's product."""
        self.amount_paid += amount
        self.date_paid = date.today()

        if self.amount_paid >= self.amount_due:
            self.status = "Paid"
            print(f"[PAYMENT PROCESSED] {self.policyholder.name} paid "
                  f"${amount:.2f} for '{self.product.name}'. Status: Paid.")
        else:
            self.status = "Pending"
            remaining = self.amount_due - self.amount_paid
            print(f"[PARTIAL PAYMENT] {self.policyholder.name} paid ${amount:.2f}. "
                  f"Remaining balance: ${remaining:.2f}.")

        if self not in self.policyholder.payment_history:
            self.policyholder.add_payment(self)

    def send_reminder(self):
        """Send a payment reminder if payment is still pending."""
        if self.status == "Paid":
            print(f"[INFO] No reminder needed - {self.policyholder.name} has already paid.")
            return
        print(f"[REMINDER] Dear {self.policyholder.name}, your payment of "
              f"${self.amount_due - self.amount_paid:.2f} for '{self.product.name}' is due.")

    def apply_penalty(self):
        """Apply a late penalty to an unpaid/overdue payment."""
        if self.status == "Paid":
            print(f"[INFO] No penalty applied - {self.policyholder.name} has already paid.")
            return
        penalty = self.amount_due * self.PENALTY_RATE
        self.amount_due += penalty
        self.status = "Late"
        print(f"[PENALTY APPLIED] {self.policyholder.name} incurred a late penalty of "
              f"${penalty:.2f}. New amount due: ${self.amount_due:.2f}.")

    def __str__(self):
        paid_on = self.date_paid if self.date_paid else "N/A"
        return (f"Payment(ID={self.payment_id}, Product={self.product.name}, "
                f"Due=${self.amount_due:.2f}, Paid=${self.amount_paid:.2f}, "
                f"Status={self.status}, Date={paid_on})")
