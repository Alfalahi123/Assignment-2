class Guest:
    def __init__(self, name, email, contact, loyalty_status):
        self.name = name
        self.email = email
        self.contact = contact
        self.loyalty_status = loyalty_status
        self.points = 0  # Default points for loyalty

    def add_points(self, points):
        self.points += points

    def redeem_points(self, points):
        if points <= self.points:
            self.points -= points
            return points
        else:
            print("Not enough points.")
            return 0

    def get_points(self):
        return self.points

    def __str__(self):
        return f"{self.name} ({self.email}) - Loyalty: {self.loyalty_status}, Points: {self.points}"
