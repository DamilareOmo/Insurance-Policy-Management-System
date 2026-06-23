"""
main.py

Demonstration script for the Insurance Policy Management System.
Creates products, registers policyholders, processes payments,
and showcases the management features of the system.
"""

from policyholder import Policyholder
from product import Product
from payment import Payment
from csv_exporter import CSVExporter


def main():
    print("=" * 60)
    print(" INSURANCE POLICY MANAGEMENT SYSTEM - DEMO")
    print("=" * 60)

    # ---------------------------------------------------------
    # 1. PRODUCT MANAGEMENT
    # ---------------------------------------------------------
    print("\n--- Creating Products ---")
    health_plan = Product(
        product_id="P001",
        name="Family Health Plan",
        premium=150.00,
        coverage_details="Covers hospitalization, outpatient care, and dental."
    )
    auto_plan = Product(
        product_id="P002",
        name="Comprehensive Auto Plan",
        premium=90.00,
        coverage_details="Covers collision, theft, and third-party liability."
    )

    health_plan.display_details()
    auto_plan.display_details()

    print("\n--- Updating a Product ---")
    auto_plan.update(premium=95.00)
    auto_plan.display_details()

    # ---------------------------------------------------------
    # 2. POLICYHOLDER MANAGEMENT
    # ---------------------------------------------------------
    print("\n--- Registering Policyholders ---")
    holder1 = Policyholder("M001", "Amaka Obi", "amaka.obi@example.com", "555-1010")
    holder2 = Policyholder("M002", "John Mensah", "john.mensah@example.com", "555-2020")
    holder1.register()
    holder2.register()

    # Assign products
    holder1.assign_product(health_plan)
    holder2.assign_product(auto_plan)

    # ---------------------------------------------------------
    # 3. PAYMENT MANAGEMENT
    # ---------------------------------------------------------
    print("\n--- Processing Payments ---")
    payment1 = Payment("PMT001", holder1, health_plan, health_plan.premium)
    payment2 = Payment("PMT002", holder2, auto_plan, auto_plan.premium)

    # Holder1 pays in full
    payment1.process_payment(150.00)

    # Holder2 pays partially first, then completes payment
    payment2.process_payment(50.00)
    payment2.send_reminder()
    payment2.process_payment(45.00)

    # ---------------------------------------------------------
    # 4. SUSPEND / REACTIVATE DEMO
    # ---------------------------------------------------------
    print("\n--- Suspension & Reactivation Demo ---")
    holder2.suspend()
    holder2.reactivate()

    # Demonstrate a late payment penalty scenario with a 3rd payment
    print("\n--- Late Payment Penalty Demo ---")
    payment3 = Payment("PMT003", holder1, health_plan, health_plan.premium)
    payment3.send_reminder()
    payment3.apply_penalty()
    payment3.process_payment(157.50)  # pays full amount including penalty

    # ---------------------------------------------------------
    # 5. PRODUCT SUSPENSION DEMO
    # ---------------------------------------------------------
    print("\n--- Suspending a Product ---")
    auto_plan.suspend()
    auto_plan.display_details()

    # ---------------------------------------------------------
    # 6. DISPLAY FINAL ACCOUNT DETAILS
    # ---------------------------------------------------------
    print("\n--- Final Account Details for Policyholders ---")
    holder1.display_details()
    holder2.display_details()

    # ---------------------------------------------------------
    # 7. EXPORT TO CSV
    # ---------------------------------------------------------
    print("\n--- Exporting Data to CSV ---")
    all_policyholders = [holder1, holder2]
    all_products = [health_plan, auto_plan]

    CSVExporter.export_policyholders(all_policyholders)
    CSVExporter.export_products(all_products)
    CSVExporter.export_payments(all_policyholders)


if __name__ == "__main__":
    main()
