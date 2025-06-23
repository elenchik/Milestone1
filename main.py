from policyholder import Policyholder
from product import Product
from payment import Payment
from datetime import datetime, timedelta

health_insurance = Product("P1", "Health Insurance", 200)
car_insurance = Product("P2", "Car Insurance", 150)

policyholder1 = Policyholder("PH1", "John Doe", "John@example.com")
policyholder2 = Policyholder("PH2", "Jane Doe", "Jane@example.com")

past_due_date = datetime.now() - timedelta(days=5)  # overdue payment
upcoming_due_date = datetime.now() + timedelta(days=2)  # due in 2 days (reminder should trigger)
future_due_date = datetime.now() + timedelta(days=30)  # due in 30 days (no reminder yet)

payment1 = Payment("P1", "PH1", 200, past_due_date)  # overdue
payment2 = Payment("P2", "PH2", 150, upcoming_due_date)  # due soon
payment3 = Payment("P3", "PH1", 100, future_due_date)  # future payment

# testing reminders
print("Payment Reminders")
print(payment1.send_reminder())
print(payment2.send_reminder())
print(payment3.send_reminder())

# processing one payment
payment2.process_payment()
print("\nAfter processing payment2:")
print(payment2.send_reminder())