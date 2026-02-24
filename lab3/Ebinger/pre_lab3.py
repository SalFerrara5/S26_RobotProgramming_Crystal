class Robot:
    
    def __init__(self, ID_number, status, location):
        self.ID = ID_number
        self.status = status
        self.loc = location
        
    def moveBot(Target_position):
        if type(Target_position) != str:
            print("Target position must be a cell number in the form of a string!")
        else:
            Robot.loc = Target_position
        
    def changeStatus():
        Robot.status = not Robot.status
