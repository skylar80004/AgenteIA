# AI Agent


#Matrix
# 0 is free
# 1 is blocked
# 2 is the agent

# Directions
# North = 1
# NorthEast = 2
# East = 3
# SouthEast = 4
# South = 5
# SouthWest = 6
# West = 7
# NorthWest = 8

import random

global rows
global columns
global matrix
global blockedChar
global agentChar
global cellSeparator


rows,columns = 10 , 10
matrix = [[0 for x in range(rows)] for y in range(columns)]

#Agent properties
agentRow = 5
agentCol = 5
blockedChar = "X"
agentChar = "O"
cellSeparator = "_"

# TODO: VALIDATION OF MOVEMENT inside each movement function

def validateNorth():

    global agentRow
    global agentCol
    
    try:
        checkedCell = matrix[agentRow-1][agentCol]
        checkedRow = agentRow -1
        if ((checkedRow) >= 0) and (checkedCell == 0):
            return True
        else:
            return False
    except IndexError as e:
        return False
    
def validateNorthWest():
    global agentRow
    global agentCol
    checkedCell = matrix[agentRow-1][agentCol-1]
    checkedRow = agentRow-1
    checkedCol = agentCol-1
    if ((checkedCell == 0 ) and (checkedRow >= 0) and(checkedCol >= 0)):
        return True
    else:
        return False
   
# Movements
def moveNorth():
    
    global agentRow
    if(validateNorth()):
        matrix[agentRow][agentCol] = 0
        agentRow -= 1
        matrix[agentRow][agentCol] = 2

def moveWest():    
    global agentRow
    global agentCol
    
    matrix[agentRow][agentCol] = 0
    agentCol -= 1
    matrix[agentRow][agentCol] = 2

def moveSouth():
    global agentRow
    global agentCol
    matrix[agentRow][agentCol] = 0
    agentRow += 1
    matrix[agentRow][agentCol] = 2

def moveEast():
    global agentRow
    global agentCol
    matrix[agentRow][agentCol] = 0
    agentCol += 1
    matrix[agentRow][agentCol] = 2


def moveNorthWest():

    global agentRow
    global agentCol
    
    matrix[agentRow][agentCol] = 0
    agentRow -= 1
    agentCol -= 1
    matrix[agentRow][agentCol] = 2

def moveSouthWest():

    global agentRow
    global agentCol
    
    matrix[agentRow][agentCol] = 0
    agentRow += 1
    agentCol -= 1
    matrix[agentRow][agentCol] = 2
    
def moveSouthEast():

    global agentRow
    global agentCol
    
    matrix[agentRow][agentCol] = 0
    agentRow += 1
    agentCol += 1
    matrix[agentRow][agentCol] = 2

def moveNorthEast():

    global agentRow
    global agentCol
    
    matrix[agentRow][agentCol] = 0
    agentRow -= 1
    agentCol += 1
    matrix[agentRow][agentCol] = 2

possibleMoves = {1 : moveNorth,
                 2 : moveNorthEast,
                 3 : moveEast,
                 4 : moveSouthEast,
                 5 : moveSouth,
                 6 : moveSouthWest,
                 7 : moveWest,
                 8 : moveNorthWest}


#Validate the given direction
# North = 1, NorthEast = 2, East = 3, SouthEast = 4, South = 5, SouthWest = 6, West = 7 NorthWest = 8
def validateDirection(direction):
    #TODO validate the direction
    return True    

# Move automatically
def randomMovement():
    # North = 1, NorthEast = 2, East = 3, SouthEast = 4, South = 5, SouthWest = 6, West = 7 NorthWest = 8
    randomDirection = random.randint(1,8)
    direction = randomDirection

    validDirection = False

    #Random search a valid direction
    while(not validDirection):        
        validDirection = validateDirection(direction)
        direction= randomDirection

    #Move the agent
    possibleMoves[direction]()
    
            
    
def placeAgent(row,column):

    global agentRow
    global agentCol
    
    agentRow = row
    agentCol = column
    matrix[row][column] = 2
    
def printMatrix():
    print("")
    print("")
    for i in range(rows):
        print("|", end = '')
        for j in range(columns):
            cell = matrix[i][j]
            if(cell == 0):
                print(" ", end = '') 
                print(cellSeparator, end = '')
                print(" ", end = '') 
            elif(cell == 1):
                print(" ", end = '') 
                print(blockedChar, end = '')
                print(" ", end = '') 
            else:
                print(" ", end = '') 
                print(agentChar, end = '')
                print(" ", end = '') 
        print("|", end = '')
        print("")

#The agents move to random directions
def randomPath():
    placeAgent(2,6)
    while(True):
        randomMovement()
        printMatrix()

def test():
    matrix[0][0] = 1
    matrix[0][1] = 1
    matrix[0][2] = 1
    matrix[0][3] = 1
    matrix[0][4] = 1

    matrix[3][0] = 1
    matrix[3][1] = 1
    matrix[3][2] = 1
    matrix[3][3] = 1
    matrix[3][4] = 1

    matrix[0][0] = 1
    matrix[1][0] = 1
    matrix[2][0] = 1
    matrix[3][0] = 1

    matrix[0][8] = 1
    matrix[1][8] = 1
    matrix[2][8] = 1
    matrix[3][8] = 1

    #Agent
    placeAgent(2,6)
    printMatrix()
    
    moveSouth()
    printMatrix()
    
    moveSouthEast()
    printMatrix()
    
    moveSouthWest()
    printMatrix()
    
    moveNorthWest()
    printMatrix()
    
    moveWest()
    printMatrix()
    
    moveEast()
    printMatrix()
    
    moveNorthEast()
    printMatrix()
    
    moveNorth()
    printMatrix()
   

    

