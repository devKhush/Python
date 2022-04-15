class Train:

    def __init__(self, name: str, seats: int, fare: int) -> None:
        self.name = name
        self.numOfSeats = seats
        self.fare = fare

    def bookTicket(self) -> None:
        if self.numOfSeats <= 0:
            print(f'No seats available in {self.name}')
            return
        self.numOfSeats -= 1
        print(f'Your seat booked successfully in {self.name}')
        print(f'Please pay Rs. {self.fare}\n')

    def getSeatNumberStatus(self, toPrint: bool) -> int:
        if toPrint:
            print('*'*50)
            print(f'Name of Train is {self.name}')
            print(f'Number of available seats: {self.numOfSeats}')
            print('*'*50)
        return self.numOfSeats

    def getFareInformation(self) -> None:
        print(f'Fare of travel in {self.name} train is Rs. {self.fare}')


# parameters can be passes in any order by this
saptKranti = Train(name='Sapt Kranti Express: 12557', fare=500, seats=1)

saptKranti.getFareInformation()
saptKranti.getSeatNumberStatus(True)
print()

saptKranti.bookTicket()
saptKranti.getFareInformation()
saptKranti.getSeatNumberStatus(True)
print()

saptKranti.bookTicket()
