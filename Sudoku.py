my_sudoku = [[3,0,6,5,0,8,4,0,0],
             [5,2,0,0,0,0,0,0,0],
             [0,8,7,0,0,0,0,3,1],
             [0,0,3,0,1,0,0,8,0],
             [0,0,0,8,6,3,0,0,5],
             [0,5,0,0,9,0,6,0,0],
             [1,3,0,0,0,0,2,5,0],
             [0,0,0,0,0,0,0,7,4],
             [0,0,5,2,0,6,3,0,0]]

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def print_my_sudoku(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('------------------------------------')
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end =" ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ", end =" ")

def find_empty(board):
    empty_list = [] 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None

def valid(board,num,pos):
    
    #Check rows
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        
    #Check colummns
    for j in range(len(board)):
        if board[j][pos[1]] == num and pos[0] != j:
            return False
        
    #Check columns
    box_x = pos[0] // 3
    box_y = pos[1] // 3
    for y_pos in range(box_y*3, box_y*3 + 3):
        for x_pos in range(box_x*3, box_x*3 + 3): 
            if board[x_pos][y_pos] == num and (x_pos,y_pos) != pos:
                return False
    return True

print_my_sudoku(my_sudoku)
solve(my_sudoku)

if find_empty(my_sudoku):
    print('\nThe sudoku is imposible to solve\n')
else:
    print("\nYour solved sudoku:\n")
    print_my_sudoku(my_sudoku)    
