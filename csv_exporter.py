"""
csv_exporter.py

Handles exporting policyholders, products, and payments to CSV files
using Python's built-in csv module — no external libraries needed.
"""

import csv
from datetime import datetime


class CSVExporter:
    """Exports system data (policyholders, products, payments) to CSV files."""

    @staticmethod
    def _timestamp():
        """Return a filename-safe timestamp string."""
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    @staticmethod
    def export_policyholders(policyholders, filename=None):
        """
        Export a list of Policyholder objects to a CSV file.

        Args:
            policyholders: list of Policyholder instances
            filename: optional custom filename; auto-generated if not provided
        """
        filename = filename or f"policyholders_{CSVExporter._timestamp()}.csv"
        headers = ["Member ID", "Name", "Email", "Phone",
                   "Status", "Registered On", "Product"]

        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for ph in policyholders:
                writer.writerow({
                    "Member ID":     ph.member_id,
                    "Name":          ph.name,
                    "Email":         ph.email,
                    "Phone":         ph.phone,
                    "Status":        ph.status,
                    "Registered On": ph.registered_on,
                    "Product":       ph.product.name if ph.product else "None",
                })

        print(f"[EXPORT] Policyholders exported to '{filename}'.")
        return filename

    @staticmethod
    def export_products(products, filename=None):
        """
        Export a list of Product objects to a CSV file.

        Args:
            products: list of Product instances
            filename: optional custom filename; auto-generated if not provided
        """
        filename = filename or f"products_{CSVExporter._timestamp()}.csv"
        headers = ["Product ID", "Name", "Premium ($/month)",
                   "Coverage Details", "Status"]

        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for pr in products:
                writer.writerow({
                    "Product ID":         pr.product_id,
                    "Name":               pr.name,
                    "Premium ($/month)":  f"{pr.premium:.2f}",
                    "Coverage Details":   pr.coverage_details,
                    "Status":             pr.status,
                })

        print(f"[EXPORT] Products exported to '{filename}'.")
        return filename

    @staticmethod
    def export_payments(policyholders, filename=None):
        """
        Export all payment records (across all policyholders) to a CSV file.

        Args:
            policyholders: list of Policyholder instances (payments pulled from each)
            filename: optional custom filename; auto-generated if not provided
        """
        filename = filename or f"payments_{CSVExporter._timestamp()}.csv"
        headers = ["Payment ID", "Policyholder ID", "Policyholder Name",
                   "Product", "Amount Due ($)", "Amount Paid ($)",
                   "Status", "Date Paid"]

        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for ph in policyholders:
                for pmt in ph.payment_history:
                    writer.writerow({
                        "Payment ID":         pmt.payment_id,
                        "Policyholder ID":    ph.member_id,
                        "Policyholder Name":  ph.name,
                        "Product":            pmt.product.name,
                        "Amount Due ($)":     f"{pmt.amount_due:.2f}",
                        "Amount Paid ($)":    f"{pmt.amount_paid:.2f}",
                        "Status":             pmt.status,
                        "Date Paid":          pmt.date_paid if pmt.date_paid else "N/A",
                    })

        print(f"[EXPORT] Payments exported to '{filename}'.")
        return filename
