from datetime import datetime, timedelta

class Payment:
    def __init__(self, payment_id, policyholder_id, amount, due_date):
        self.payment_id = payment_id
        self.policyholder_id = policyholder_id
        self.amount = amount
        self.due_date = due_date
        self.paid = False

    def process_payment(self):
        self.paid = True
        return f"Payment of ${self.amount} processed."

    def check_late_payment(self):
        if datetime.now() > self.due_date and not self.paid:
            penalty = self.amount * 0.1
            return f"Late payment! Penalty: ${penalty}"
        return "No late payment detected."

    def send_reminder(self):
        if not self.paid:
            if datetime.now() >= (self.due_date - timedelta(days=3)):
                self.reminder_sent = True
                return f"REMINDER: Payment of ${self.amount} is due."
            elif datetime.now() > self.due_date:
                return f"URGENT: Payment overdue! {self.check_late_payment()}"
        return "No reminder needed (payment already processed)."

    def __str__(self):
        return f"Payment ID: {self.payment_id}, Amount: ${self.amount}, Due: {self.due_date}, Paid: {self.paid}"