from robot import *


direction_list = ["NORTH", "SOUTH", "EAST", "WEST"]

class InputError(Exception):
    pass


if __name__ == "__main__":
    def place_the_robot():
        global x , y , f
        x_input , y_input , f_input = input("Place the robot by entering X , Y , F: ").split(',')
        x = int(x_input)
        y = int(y_input)
        f = f_input.upper()
    
try:
    place_the_robot()
    myRobot = ToyRobot()
    myRobot.place(x, y, f)

    while x in range(5) and y in range(5) and f in direction_list:
        
            command = input("Choose a command from:\nPLACE, MOVE, LEFT, RIGHT, REPORT: ")
            if command.upper() == "PLACE":
                place_the_robot()
                myRobot.place(x, y, f)     
            elif command.upper() == "MOVE":
                myRobot.move()
            elif command.upper() == "LEFT":
                myRobot.left()
            elif command.upper() == "RIGHT":
                myRobot.right()
            elif command.upper() == "REPORT":
                print(myRobot.report())
            else:
                print("WARNING: Please enter a valid command.")
            continue

except InputError:
    print("Invalid input")

except ValueError:
    print("Invalid input")