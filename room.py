class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.availability = True  # Room is available by default

    def book_room(self):
        if self.availability:
            self.availability = False
            return True
        return False

    def release_room(self):
        self.availability = True

    def __str__(self):
        return f"Room {self.room_number}, Type: {self.room_type}, Price: {self.price}, Available: {self.availability}"
