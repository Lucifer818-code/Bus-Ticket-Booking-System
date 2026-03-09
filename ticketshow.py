from database_helper import db_connect

class TicketShow:
    def __init__(self):
        self.db = db_connect()

    def ticketshow(self):
        tid = input("Enter Your Booking Id: ")
        query = "SELECT * FROM passengers WHERE id = %s"
        result = self.db.execute_query(query, (tid,))
        
        if result:
            sh = result[0]
            print("\n" + "-"*40)
            print(f"        EZHIL BUS TRAVEL - TICKET")
            print("-"*40)
            print(f"Passenger: {sh['name']} | ID: {sh['id']}")
            print(f"Route: {sh['departure']} -> {sh['destination']}")
            print(f"Date: {sh['travel_date']} | Seats: {sh['seat_no']}")
            print(f"Type: {sh['bus_type']} | Fare: {sh['fare']}")
            print("-"*40)
        else:
            print("Booking ID not found!")