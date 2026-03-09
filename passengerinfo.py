from database_helper import db_connect

class PassengerRegistration:
    def __init__(self):
        self.db = db_connect()
        self.data = {}

    def getpassengerinfo(self):
        self.data['name'] = input("Enter Passenger Name: ")
        self.data['count'] = int(input("Number of Passengers: "))
        self.data['source'] = input("Departure Location: ")
        self.data['dest'] = input("Destination Location: ")
        self.data['date'] = input("Date (DD-MM-YYYY): ")
        self.data['seat'] = input("Seat Number: ")
        bt = int(input("1: AC BUS\n2: NON AC BUS\nChoose Type: "))
        self.data['type'] = "AC BUS" if bt == 1 else "NON AC BUS"
        self.data['fare'] = self.data['count'] * (500 if bt == 1 else 300)

    def saveinfo(self):
        query = """INSERT INTO passengers 
                   (name, no_of_passengers, departure, destination, travel_date, seat_no, bus_type, fare) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        params = (self.data['name'], self.data['count'], self.data['source'], 
                  self.data['dest'], self.data['date'], self.data['seat'], 
                  self.data['type'], self.data['fare'])
        self.db.execute_query(query, params)
        print("Booking Saved Successfully!")