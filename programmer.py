class Train:
    totalSeats =300
    def __init__(self, name ,fare ,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print(f"the name of the train is : {self.name}")
        print(f"the number of seats available is : {self.seats}")
        
    def fareInfo(self):
        print(f"the fare of this train is : {self.fare}")

    def bookTicket(self,x):
        if (self.seats>0):
           
            x=self.totalSeats + 1 - self.seats
            print(f"your ticket is booked . your seat number is : {x} ")
            self.seats=self.seats-1
        else :
            print("no seats are available")

harry=Train("rajdhani express",500,300)
harry.getStatus()
harry.fareInfo()
harry.bookTicket()

alka1=Train("rajdhani express",500,300)
alka1.getStatus()
alka1.fareInfo()
alka1.bookTicket()

alka2=Train("rajdhani express",500,300)
alka2.getStatus()
alka2.fareInfo()
alka2.bookTicket()

alka3=Train("rajdhani express",500,300)
alka3.getStatus()
alka3.fareInfo()
alka3.bookTicket()

alka4=Train("rajdhani express",500,300)
alka4.getStatus()
alka4.fareInfo()
alka4.bookTicket()