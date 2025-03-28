from payment import Payment

class Booking:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def confirm_booking(self):
        if self.room.book_room():
            print(f"Room {self.room.room_number} has been booked.")
            payment = Payment(self.room.price, "Credit Card")
            payment.process_payment()
        else:
            print(f"Room {self.room.room_number} is not available.")
    
    def cancel_booking(self):
        self.room.release_room()
        print(f"Booking for Room {self.room.room_number} has been cancelled.")
    
    def __str__(self):
        return f"Booking for {self.guest.name} in Room {self.room.room_number} from {self.check_in_date} to {self.check_out_date}"
