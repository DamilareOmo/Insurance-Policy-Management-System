# Insurance Policy Management System

A simple Python console application that simulates an insurance company's
policy management system. It manages **policyholders**, **products**, and
**payments** through three independent classes, each defined in its own file.

## Project Structure

```
policy_system/
├── policyholder.py       # Policyholder class: register, suspend, reactivate
├── product.py            # Product class: create, update, suspend/reactivate
├── payment.py            # Payment class: process payments, reminders, penalties
├── main.py               # Demonstration script that ties everything together
├── policy_system.ipynb   # Demonstration script that ties everything together
└── README.md             # This file
```

## Requirements

- Python 3.8 or higher (no external libraries needed — uses only the
  Python standard library).

## How to Run

1. Make sure Python 3 is installed:
   ```
   python3 --version
   ```
2. Unzip the project (if you received it as a zip file) and `cd` into the
   project folder:
   ```
   cd policy_system
   ```
3. Run the demonstration script:
   ```
   python3 main.py
   ```

The script will:
- Create two insurance products (Health Plan and Auto Plan).
- Register two policyholders and assign each a product.
- Process full and partial payments.
- Demonstrate sending a payment reminder.
- Demonstrate applying a late-payment penalty.
- Demonstrate suspending and reactivating a policyholder.
- Demonstrate suspending a product.
- Display the final account details for both policyholders, including
  their full payment history.

## Class Overview

### `Policyholder` (policyholder.py)
| Method | Description |
|---|---|
| `register()` | Marks the policyholder as Active. |
| `suspend()` | Suspends the policyholder's account. |
| `reactivate()` | Reactivates a suspended policyholder. |
| `assign_product(product)` | Subscribes the policyholder to a product. |
| `add_payment(payment)` | Records a payment in the policyholder's history. |
| `display_details()` | Prints a full summary of the policyholder's account. |

### `Product` (product.py)
| Method | Description |
|---|---|
| `update(...)` | Updates the product's name, premium, and/or coverage. |
| `suspend()` | Suspends/removes the product from being offered. |
| `reactivate()` | Reactivates a suspended product. |
| `display_details()` | Prints a summary of the product. |

### `Payment` (payment.py)
| Method | Description |
|---|---|
| `process_payment(amount)` | Records a payment (full or partial) toward the amount due. |
| `send_reminder()` | Sends a reminder if the payment is still pending. |
| `apply_penalty()` | Applies a 5% late penalty to an unpaid/overdue payment. |

## Sample Output (excerpt)

```
--- Registering Policyholders ---
[REGISTERED] Amaka Obi (ID: M001) is now Active.
[REGISTERED] John Mensah (ID: M002) is now Active.
[PRODUCT ASSIGNED] Amaka Obi subscribed to 'Family Health Plan'.
[PRODUCT ASSIGNED] John Mensah subscribed to 'Comprehensive Auto Plan'.

--- Processing Payments ---
[PAYMENT PROCESSED] Amaka Obi paid $150.00 for 'Family Health Plan'. Status: Paid.
[PARTIAL PAYMENT] John Mensah paid $50.00. Remaining balance: $45.00.
[REMINDER] Dear John Mensah, your payment of $45.00 for 'Comprehensive Auto Plan' is due.
[PAYMENT PROCESSED] John Mensah paid $45.00 for 'Comprehensive Auto Plan'. Status: Paid.
```

## Notes

- This is a console-based demo with in-memory data only (no database).
  Data does not persist between runs.
- The penalty rate is set at 5% of the outstanding balance and can be
  changed via the `Payment.PENALTY_RATE` class attribute.
- All code follows standard Python conventions (PEP 8 naming, docstrings,
  and inline comments) for readability and maintainability.

## Author

Sodiq Omoniyi | Software Engineer | Milestone 1 - Insurance Policy Management System.
