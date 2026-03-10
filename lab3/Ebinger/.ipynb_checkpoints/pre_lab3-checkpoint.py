class Robot:
    
    def __init__(self, ID_number, status, location):
        self.ID = ID_number
        self.status = status
        self.loc = location
        
    def moveBot(self, Target_position):
        if type(Target_position) != str:
            print("Target position must be a cell number in the form of a string!")
        else:
            self.loc = Target_position
        
    def changeStatus(self):
        self.status = not self.status
