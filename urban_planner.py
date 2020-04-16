import datetime

class Building:
    """Create a building
    Building(address, stories)

    Keyword arguments :
    address: string address of building
    stories: number of stories
    

    Methods:
    construct(): sets date_constructed to datetime.now
    purchase(buyer): sets owner = buyer
    printOut(): prints out details of building in a string
    """
    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, buyer):
        self.owner = buyer

    def printOut(self):
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.")    

fiveOhFive = Building("505 West Avenue", 3)
fiveOhFive.purchase("Donald Donaldson")
fiveOhFive.construct()
fiveOhFive.printOut()

fourOhFour = Building("404 East Avenue", 14)
fourOhFour.purchase("Tom Thompson")
fourOhFour.construct()
fourOhFour.printOut()

threeOhThree = Building("303 North Avenue", 9)
threeOhThree.purchase("Bill Billson")
threeOhThree.construct()
threeOhThree.printOut()

twoOhTwo = Building("202 South Avenue", 18)
twoOhTwo.purchase("Chris Christenson")
twoOhTwo.construct()
twoOhTwo.printOut()

oneOhOne = Building("101 West Boulevard", 7)
oneOhOne.purchase("Robert Robertson")
oneOhOne.construct()
oneOhOne.printOut()