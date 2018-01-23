# -*- coding: utf-8 -*-
"""
@author: Ahmet Turk
"""

LEFT = 1
FRONT = 2
RIGHT = 3
BEHIND = 4

# Data type return from the robot sensor 
# indicates left, front and right sides of robot
# True means there is a way, False means there is a wall
class SensorData():
    def __init__(self, left, front, right):
      self.left = left
      self.front = front
      self.right = right
    
# Data type for each element of the maze
# indicates left, front, right and behind sides of the place
# True means there is a way, False means there is a wall
class MazeElement():
    def __init__(self, left, front, right, behind):
      self.left = left
      self.front = front
      self.right = right
      self.behind = behind

# This maze simulates the original one
# It consists of 64 elements, 8x8 square 
class Maze():
    def __init__(self):        
        # robot_position is the current position of the robot
        # it is between 0 to 63, 0 is left upper corner, 63 is right lower corner
        self.robot_position = 63
        
        # robot's orientation, reference frame is the maze
        self.orientation = FRONT
        
        self.mazeList = []
        self.mazeList.append(MazeElement(False, False, True, True))
        self.mazeList.append(MazeElement(True, False, True, False))
        self.mazeList.append(MazeElement(True, False, True, False))
        self.mazeList.append(MazeElement(True, False, True, False))
        self.mazeList.append(MazeElement(True, False, True, True))
        self.mazeList.append(MazeElement(True, False, False, True))
        self.mazeList.append(MazeElement(False, False, True, True))
        self.mazeList.append(MazeElement(True, False, False, True))
        
        self.mazeList.append(MazeElement(False, True, False, True))
        self.mazeList.append(MazeElement(False, False, True, True))
        self.mazeList.append(MazeElement(True, False, False, True))
        self.mazeList.append(MazeElement(False, False, True, True))
        self.mazeList.append(MazeElement(True, True, False, False))
        self.mazeList.append(MazeElement(False, True, True, False))
        self.mazeList.append(MazeElement(True, True, False, False))
        self.mazeList.append(MazeElement(False, True, False, True))
        
        self.mazeList.append(MazeElement(False, True, True, False))
        self.mazeList.append(MazeElement(True, True, False, False))
        self.mazeList.append(MazeElement(False, True, False, True))
        self.mazeList.append(MazeElement(False, True, True, False))
        self.mazeList.append(MazeElement(True, False, True, False))
        self.mazeList.append(MazeElement(True, False, True, False))
        self.mazeList.append(MazeElement(True, False, False, True))
        self.mazeList.append(MazeElement(False, True, False, True))
        
        self.mazeList.append(MazeElement(True, False, False, True))
        self.mazeList.append(MazeElement(False, False, True, True))
        self.mazeList.append(MazeElement(True, True, True, False))
        self.mazeList.append(MazeElement(True, False, True, False))
        self.mazeList.append(MazeElement(True, False, False, True))
        self.mazeList.append(MazeElement(False, False, True, True))
        self.mazeList.append(MazeElement(True, True, False, False))
        self.mazeList.append(MazeElement(False, True, False, True))
        
        self.mazeList.append(MazeElement(False, True, False, True))
        self.mazeList.append(MazeElement(False, False, True, True))
        self.mazeList.append(MazeElement(True, False, True, False))
        self.mazeList.append(MazeElement(True, False, False, True))
        self.mazeList.append(MazeElement(False, True, False, True))
        self.mazeList.append(MazeElement(False, True, False, True))
        self.mazeList.append(MazeElement(False, False, False, True))
        self.mazeList.append(MazeElement(False, True, False, True))
        
        self.mazeList.append(MazeElement(False, True, True, False))
        self.mazeList.append(MazeElement(True, True, False, False))
        self.mazeList.append(MazeElement(False, False, False, True))
        self.mazeList.append(MazeElement(False, True, False, True))
        self.mazeList.append(MazeElement(False, True, False, False))
        self.mazeList.append(MazeElement(False, True, False, True))
        self.mazeList.append(MazeElement(False, True, True, False))
        self.mazeList.append(MazeElement(True, True, False, True))
        
        self.mazeList.append(MazeElement(False, False, True, True))
        self.mazeList.append(MazeElement(True, False, True, False))
        self.mazeList.append(MazeElement(True, True, False, False))
        self.mazeList.append(MazeElement(False, True, True, False))
        self.mazeList.append(MazeElement(True, False, False, True))
        self.mazeList.append(MazeElement(False, True, True, False))
        self.mazeList.append(MazeElement(True, False, False, True))
        self.mazeList.append(MazeElement(False, True, False, True))
        
        self.mazeList.append(MazeElement(False, True, True, False))
        self.mazeList.append(MazeElement(True, False, True, False))
        self.mazeList.append(MazeElement(True, False, True, False))
        self.mazeList.append(MazeElement(True, False, True, False))
        self.mazeList.append(MazeElement(True, True, True, False))
        self.mazeList.append(MazeElement(True, False, True, False))
        self.mazeList.append(MazeElement(True, True, False, False))
        self.mazeList.append(MazeElement(False, True, False, False))
        
    # moves robot in the maze according to the input whose reference frame is robot
    def moveRobot(self, input):
        # firstly change the orientation of the robot
        if input == LEFT:
            if self.orientation == LEFT:
                self.orientation = BEHIND
            else:
                self.orientation -= 1
        elif input == RIGHT:
            if self.orientation == BEHIND:
                self.orientation = LEFT
            else:
                self.orientation += 1
        elif input == BEHIND:
            if self.orientation == LEFT:
                self.orientation = RIGHT
            elif self.orientation == FRONT:
                self.orientation = BEHIND
            elif self.orientation == RIGHT:
                self.orientation = LEFT
            else:
                self.orientation = FRONT
                
        # then move the robot forward according to orientation
        if self.orientation == LEFT:
            self.robot_position -= 1
        elif self.orientation == FRONT:
            self.robot_position -= 8
        elif self.orientation == RIGHT:
            self.robot_position += 1
        else:
            self.robot_position += 8
    
    # this function returns SensorData of the robot, reference frame is the robot
    def giveSensorData(self):
        if self.orientation == LEFT:
            cell = self.mazeList[self.robot_position]
            return SensorData(cell.behind, cell.left, cell.front)
        elif self.orientation == FRONT:
            cell = self.mazeList[self.robot_position]
            return SensorData(cell.left, cell.front, cell.right)
        elif self.orientation == RIGHT:
            cell = self.mazeList[self.robot_position]
            return SensorData(cell.front, cell.right, cell.behind)
        else:
            cell = self.mazeList[self.robot_position]
            return SensorData(cell.right, cell.behind, cell.left)
    
# Data type to hold movements happened in the maze
# left, front, right is True if there is a way
# canGoLeft, canGoFront, canGoRight is True if robot has never gone that way
# goneTo is the way where robot has gone to
# count is the number of possibilities for choosing a way
class Move():
    def __init__(self, left, front, right):
        self.left = left
        self.front = front
        self.right = right
        self.canGoLeft = False
        self.canGoFront = False
        self.canGoRight = False
        self.goneTo = 0
        self.count = 0
        if left:
            self.canGoLeft = True
            self.count += 1
        if front:
            self.canGoFront = True
            self.count += 1
        if right:
            self.canGoRight = True 
            self.count += 1

# Algorithm that solves the maze
# solvingList is a stack holds every movement from beginning
# goBack becomes True when robot faces a dead end
class MazeSolver():
    def __init__(self):
        self.solvingList = []
        self.goBack = False
        
    # This function takes sensorData and then returns a way
    def chooseWay(self, sensorData):
        if self.goBack == False:
            move = Move(sensorData.left, sensorData.front, sensorData.right)        
            
            if move.left and move.canGoLeft:
                move.goneTo = LEFT
                move.canGoLeft = False
                move.count -= 1
                self.solvingList.append(move)
                return move.goneTo
            elif move.front and move.canGoFront:
                move.goneTo = FRONT
                move.canGoFront = False
                move.count -= 1
                self.solvingList.append(move)
                return move.goneTo
            elif move.right and move.canGoRight:
                move.goneTo = RIGHT
                move.canGoRight = False
                move.count -= 1
                self.solvingList.append(move)
                return move.goneTo
            else:
                self.goBack = True
                return BEHIND
                
        # else goBack is True
        else:
            preMove = self.solvingList.pop()
            if preMove.count == 0:
                # Still there is not another way to go, so go back
                self.goBack = True
                if preMove.goneTo == LEFT:
                    return RIGHT
                elif preMove.goneTo == FRONT:
                    return FRONT
                elif preMove.goneTo == RIGHT:
                    return LEFT
            else:
                # Another way is found, try that one
                self.goBack = False
                preGoneTo = preMove.goneTo
                if preMove.left and preMove.canGoLeft:
                    preMove.goneTo = LEFT
                    preMove.canGoLeft = False
                    preMove.count -= 1
                    self.solvingList.append(preMove)
                    if preGoneTo == FRONT:
                        return RIGHT
                    else:
                        return FRONT
                elif preMove.front and preMove.canGoFront:
                    preMove.goneTo = FRONT
                    preMove.canGoFront = False
                    preMove.count -= 1
                    self.solvingList.append(preMove)
                    if preGoneTo == LEFT:
                        return LEFT
                    else:
                        return RIGHT
                elif preMove.right and preMove.canGoRight:
                    preMove.goneTo = RIGHT
                    preMove.canGoRight = False
                    preMove.count -= 1
                    self.solvingList.append(preMove)
                    if preGoneTo == LEFT:
                        return FRONT
                    else:
                        return LEFT
                
        
def main():
    maze = Maze()
    mazeSolver = MazeSolver()

    print("1 = LEFT, 2 = FRONT, 3 = RIGHT, 4 = BEHIND")

    userInput = 1

    while userInput == 1:
        sensorData = maze.giveSensorData()
        chosenWay = mazeSolver.chooseWay(sensorData)
        maze.moveRobot(chosenWay)
        if chosenWay == LEFT:
            print("LEFT")
        elif chosenWay == FRONT:
            print("FRONT")
        elif chosenWay == RIGHT:
            print("RIGHT")
        elif chosenWay == BEHIND:
            print("BEHIND")
        userInput = input("1 yaz ")
  
if __name__== "__main__":
    main()
