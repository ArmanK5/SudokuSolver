board = [
    [7,8,'_',4,'_','_',1,2,'_'],
    [6,'_','_','_',7,5,'_','_',9],
    ['_','_','_',6,'_',1,'_',7,8],
    ['_','_',7,'_',4,'_',2,6,'_'],
    ['_','_',1,'_',5,'_',9,3,'_'],
    [9,'_',4,'_',6,'_','_','_',5],
    ['_',7,'_',3,'_','_','_',1,2],
    [1,2,'_','_','_',7,4,'_','_'],
    ['_',4,9,2,'_',6,'_','_',7]
]

def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("------------------------") # creating a horizontal divider

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="") # creating a vertical divider

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == '_':
                return (i, j) # row, col