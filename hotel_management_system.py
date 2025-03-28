from guest import Guest
from room import Room
from booking import Booking
from payment import Payment
from service import Service

class HotelManagementSystem:
    def __init__(self):
        self.guests = []
        self.rooms = [Room(101, "Single", 100), Room(102, "Double", 150), Room(103, "Suite", 250)]
        self.bookings = []
        self.services = []

    def create_guest_account(self):
        name = input("Enter guest name: ")
        email = input("Enter guest email: ")
        contact = input("Enter guest contact number: ")
        loyalty_status = input("Enter loyalty status (e.g., Silver, Gold, Platinum): ")
        guest = Guest(name, email, contact, loyalty_status)
        self.guests.append(guest)
        print(f"Guest account created for {name}.")

    def search_rooms(self):
        room_type = input("Enter room type to search (Single, Double, Suite): ")
        available_rooms = [room for room in self.rooms if room.room_type == room_type and room.availability]
        if available_rooms:
            print("Available rooms:")
            for room in available_rooms:
                print(f"Room {room.room_number}, Price per night: {room.price}")
        else:
            print("No available rooms found for the specified type.")

    def book_room(self):
        guest_name = input("Enter guest name for booking: ")
        guest = next((g for g in self.guests if g.name == guest_name), None)
        if guest:
            room_number = int(input("Enter room number to book: "))
            room = next((r for r in self.rooms if r.room_number == room_number), None)
            if room and room.availability:
                check_in_date = input("Enter check-in date: ")
                check_out_date = input("Enter check-out date: ")
                booking = Booking(guest, room, check_in_date, check_out_date)
                booking.confirm_booking()
                self.bookings.append(booking)
            else:
                print("Room is not available.")
        else:
            print("Guest not found.")

    def process_payment(self):
        booking_id = int(input("Enter booking ID to process payment: "))
        booking = self.bookings[booking_id - 1] if 0 < booking_id <= len(self.bookings) else None
        if booking:
            payment_method = input("Enter payment method (Credit Card, Debit Card, Mobile Wallet): ")
            payment = Payment(booking.room.price, payment_method)
            payment.process_payment()
        else:
            print("Booking not found.")

    def request_service(self):
        guest_name = input("Enter guest name for service request: ")
        guest = next((g for g in self.guests if g.name == guest_name), None)
        if guest:
            service_name = input("Enter service requested (e.g., Room Service, Housekeeping): ")
            service = Service(service_name, guest)
            service.request_service()
            self.services.append(service)
        else:
            print("Guest not found.")

    def main_menu(self):
        while True:
            print("\n--- Royal Stay Hotel Management System ---")
            print("1. Create Guest Account")
            print("2. Search Available Rooms")
            print("3. Book Room")
            print("4. Process Payment")
            print("5. Request Service")
            print("6. Exit")
            choice = input("Choose an operation (1-6): ")

            if choice == '1':
                self.create_guest_account()
            elif choice == '2':
                self.search_rooms()
            elif choice == '3':
                self.book_room()
            elif choice == '4':
                self.process_payment()
            elif choice == '5':
                self.request_service()
            elif choice == '6':
                print("Exiting system...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    hotel_system = HotelManagementSystem()
    hotel_system.main_menu()
