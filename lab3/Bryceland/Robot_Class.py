class Robot: #by convention name is CapitalizedWords notation
   
    def __init__(self,ID_number, status = True, location = "A1"):
        #specify attributes of class for initialization
        #may have multiple or no arguments but self must be first
        self.ID_number = ID_number #this is a class attribute (same for all instances)
        self.status = status
        self.location = location
        #the above attributes are unique to each instance

    def moveBot(self, new_location):
        self.location = new_location

    def changeStatus(self):
        self.status = not self.status

    def __str__(self):
        
        if self.status:
            status_str = "Online"
        else:
            status_str = "Offline"
            
        return f"Robot {self.ID_number} | Status: {status_str} | Location: {self.location}"

if __name__ == "__main__":
    r = Robot(10, True, "B2")
    print(r)

    r.moveBot("C3")
    print(r)

    r.changeStatus()
    print(r)



