from admin import Admin
from passengerinfo import PassengerRegistration
from ticketshow import TicketShow

def run():
    print("Welcome To Ezhil Bus Travel System")
    ad = Admin()
    
    while True:
        print("\n1: Admin Register\n2: Admin Login\n3: Exit")
        ch = input("Choose: ")
        
        if ch == '1':
            ad.adminRegistration()
        elif ch == '2':
            if ad.adminlogin():
                while True:
                    print("\n1: New Booking\n2: Show Ticket\n3: Logout")
                    sub_ch = input("Choose: ")
                    if sub_ch == '1':
                        p = PassengerRegistration()
                        p.getpassengerinfo()
                        p.saveinfo()
                    elif sub_ch == '2':
                        t = TicketShow()
                        t.ticketshow()
                    else:
                        break
        elif ch == '3':
            break

if __name__ == "__main__":
    run()