class Policyholder:
    def __init__(self, policyholder_id, name, contact, status="active"):
        self.policyholder_id = policyholder_id
        self.name = name
        self.contact = contact
        self.status = status

    def register(self):
        self.status = "active"
        return f"Policyholder {self.name} registered successfully."

    def suspend(self):
        if self.status == "active":
            self.status = "suspended"
            return f"Policyholder {self.name} suspended."
        return "Already suspended or terminated."

    def reactivate(self):
        if self.status == "suspended":
            self.status = "active"
            return f"Policyholder {self.name} reactivated."
        return "Cannot reactivate: Policyholder is not suspended."

    def __str__(self):
        return f"ID: {self.policyholder_id}, Name: {self.name}, Status: {self.status}"