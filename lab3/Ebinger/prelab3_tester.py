from pre_lab3 import Robot

ROSbot = Robot(23, False, "A3")
new_loc = "C5"

print(f"The robot started at {ROSbot.loc}")

if ROSbot.status == True:
    print("The robot is online")
elif ROSbot.status == False:
    print("The robot is offline")

ROSbot.moveBot(new_loc)
print(f"The robot has moved to {new_loc}")
ROSbot.changeStatus()

if ROSbot.status == True:
    print("The robot is online")
elif ROSbot.status == False:
    print("The robot is offline")