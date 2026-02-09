#Q.Can you change the self-parameter inside a class to something else {say "harry"}.
#Try changing self to "slf" or "harry" and see the effects.

#Q. write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under indian Railways.
from random import randint
class Train:
    def __init__(harry,trainNo):
        harry.trainNo = trainNo


    def book(self, fro, to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train no : {self.trainNo} is running no time")
    def getFare(self, fro, to):
        print(f"Ticket fare in tain no : {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t=Train(12399)
t.book("KTM", "MNR")
t.getStatus()
t.book("KTM", "MNR")