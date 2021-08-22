# Toy Robot Simulator

## USING THE APP

- Clone the repository.
- Run `python app.py` in CLI
- A message will appear : `Place the robot by entering X , Y , F:`
- X , Y are coordinates of the place it will accept values [0-4] inclusive.
- F is the faceing direction of the robot it will accept values : NORTH , SOUTH , WEST , EAST.
- Example of a valid input will be: `1,1,SOUTH`
- If the user enter invalid input the console will show the message `invalid input` and the app will be terminated.
- After entering the robot place , user will have the option to run one of the commands: PLACE, MOVE, LEFT, RIGHT, REPORT.
- **PLACE** : will asks to enter the coordinates and facing direction: X , Y , F
- **MOVE** : will move the robot unit forward in the direction it is currently facing.
- **LEFT** and **RIGHT** will rotate the robot 90 degrees in the specified direction without changing the position of the robot.
- **REPORT** will announce the X,Y and F of the robot.

## TEST CASES

1. Case(1): Invalid X coordinate  
![alt test_1](https://github.com/harmardir/toy_robot/blob/main/test_images/test_1.JPG)
3. Case(2): Invalid Y coordinate  
![alt test_2](https://github.com/harmardir/toy_robot/blob/main/test_images/test_2.JPG)
5. Case(3): Invalid F (direction)
![alt test_3](https://github.com/harmardir/toy_robot/blob/main/test_images/test_3.JPG)
7. Case(4): Prevent the robot to fall out of the table from NORTH
![alt test_4](https://github.com/harmardir/toy_robot/blob/main/test_images/test_4.JPG)
9. Case(5): Prevent the robot to fall out of the table from SOUTH
![alt test_5](https://github.com/harmardir/toy_robot/blob/main/test_images/test_5.JPG)
11. Case(6): Prevent the robot to fall out of the table from EAST
![alt test_6](https://github.com/harmardir/toy_robot/blob/main/test_images/test_6.JPG)
13. Case(7): Prevent the robot to fall out of the table from WEST
![alt test_7](https://github.com/harmardir/toy_robot/blob/main/test_images/test_7.JPG)
15. Case(8): Invalid movement option  
![alt test_8](https://github.com/harmardir/toy_robot/blob/main/test_images/test_8.JPG)
17. Case(9): Valid input  
![alt test_9](https://github.com/harmardir/toy_robot/blob/main/test_images/test_9.JPG)

