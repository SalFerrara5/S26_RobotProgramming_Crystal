from Lab3_prelab import Robot

def main():
    robot_id = input("Enter robot ID: ")
    bot = Robot(robot_id)

    while True:
        print("\nCurrent Robot State:")
        print(bot)

        print("\nChoose an action:")
        print("1 - Move robot")
        print("2 - Toggle online/offline status")
        print("3 - Quit")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            new_location = input("Enter new location (e.g., A3): ")
            bot.moveBot(new_location)
            print("Robot moved.")

        elif choice == "2":
            bot.changeStatus()
            print("Robot status toggled.")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
