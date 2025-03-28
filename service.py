class Service:
    def __init__(self, service_name, guest):
        self.service_name = service_name
        self.guest = guest

    def request_service(self):
        print(f"Service '{self.service_name}' requested by {self.guest.name}.")
        self.complete_service()

    def complete_service(self):
        print(f"Service '{self.service_name}' for {self.guest.name} completed.")
