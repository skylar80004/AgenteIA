# AI Agent


#Matrix
# 0 is free
# 1 is blocked
# 2 is the agent

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

# Movements
def moveNorth():
    
    global agentRow
    if(validateNorth()):
        matrix[agentRow][agentCol] = 0
        agentRow -= 1
        matrix[agentRow][agentCol] = 2

def moveNorthWest():

    global agentRow
    global agentCol
    
    matrix[agentRow][agentCol] = 0
    agentRow -= 1
    agentCol -= 1
    matrix[agentRow][agentCol] = 2

def moveEast():
    global agentRow
    global agentCol
    matrix[agentRow][agentCol] = 0
    agentCol -= 1
    matrix[agentRow][agentCol] = 2

def moveSouth():
    global agentRow
    global agentCol
    matrix[agentRow][agentCol] = 0
    agentRow -= 1
    matrix[agentRow][agentCol] = 2
    
    
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
    moveNorth()
    moveNorth()
    moveNorth()
    moveNorth()
    moveNorth()
    moveNorth()
    moveNorth()
    moveNorth()
    moveNorth()
    
    printMatrix()



test()
    

