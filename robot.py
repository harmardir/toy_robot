direction_list = ["NORTH", "SOUTH", "EAST", "WEST"]

class InputEroor(Exception):
    pass

class ToyRobot:
    def __init__(self, x=0, y=0, f="NORTH"):
        self.x = x
        self.y = y
        self.f = f

    def place(self, x_input, y_input, f_input):
        if x_input in range(5) and y_input in range(5) and f_input in direction_list:
            self.x = x_input
            self.y = y_input
            self.f = f_input
        else:
            print("WARNING: Both X and Y coordinates should be between 0 and 4 also F should be one of: NORTH, SOUTH, EAST or WEST")

    def move(self):
        if self.f == "NORTH" and self.y < 4:
            self.y += 1
        elif self.f == "SOUTH" and self.y > 0:
            self.y -= 1
        elif self.f == "EAST" and self.x < 4:
            self.x += 1
        elif self.f == "WEST" and self.x > 0:
            self.x -= 1
        else:
            print("WARNING: This move causes the robot to fall off the table. Please try a different option")

    def left(self):
        if self.f == "NORTH":
            self.f = "WEST"
        elif self.f == "SOUTH":
            self.f = "EAST"
        elif self.f == "EAST":
            self.f = "NORTH"
        else:
            self.f = "SOUTH"

    def right(self):
        if self.f == "NORTH":
            self.f = "EAST"
        elif self.f == "SOUTH":
            self.f = "WEST"
        elif self.f == "EAST":
            self.f = "SOUTH"
        else:
            self.f = "NORTH"

    def report(self):
        return self.x, self.y, self.f