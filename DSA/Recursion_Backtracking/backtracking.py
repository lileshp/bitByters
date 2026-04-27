'''
Backtracking
    Backtracking is an algorithmic technique used to solve problems recursively by trying different possible solutions and eliminating those that fail to meet the problem's constraints.
    It is particularly useful for combinatorial and constraint satisfaction problems.

    Backtracking is a depth-first search (DFS) based approach where we build a solution incementally.

Key concepts:
    1. Decision Space: all possible choices that can be made at a given step.
    2. Constraints: conditions that a valid solution must satisfy.
    3. Pruning: Eliminating invalid choices to optimize the search.
    4. Backtracking step: if a choice leads to failure, undo the decision and try another.

Categories/Types:
    basis on the nature of constraints and solution structure:
    1. Decision Problems
        We determine if a valid solution exist.
        N-queen,
    2. Optimization Problems
        We find the best possible solution among valid ones.
        Find the shortest path in the maze.
    3. Enumeration Problems
        we list all valid solutions
        generate all permutations of the given string

How it works:
    follows a systematic trai-and-error approach:
        1. Choose: Select an option from available choices 
        2. Explore: Proceed with the choice and recursively solve the problem.
        3. Backtrack: if the choice violates constraints, undo it and try another option.

Determining Backtracking problems:
    A problem can be solved using backtracking if:
        It has a recursive structure (can be divide into smaller subproblems)
        The problem requires generating all solutions and eliminating invalid ones.
        The problem invloves constraints that guide the decision-making process.



Recursion vs Backtracking

Feature         ||          Recursion                   ||      Backtracking
==========================================================================================
Definition      ||   Function calls itself              ||  uses recursion with pruning
Purpose         || solve problems with subproblems      ||  solve constraints based problems
Eploration      || Explore all paths                    ||  Prunes invalid paths early
Efficiency      ||  May lead to redundant computation   || Eliminates unnecessary computations
Example         || Fibonacci sequence                   ||  N-Queens problem
=============================================================================================


Application of Backtracking:
1. Constraint satisfication problems (CSPs):
    Sudoku Solver
2. Decision Making
    N-Queens
3. Combination problems
    generating all subset of a set/sequence
4. Game based:
    chess, Maze
5. AI and optimatization:
    Decision-making in AI Application/Algorithm


'''
#Common Backtracking problems

# N-Queens Problem
# Problem Statement: Place N queens on an N×N chessboard such that no two queens attack each other.
def is_safe(board, row, col, N):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, N):
    if row == N:
        print(board)
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_n_queens(board, row + 1, N)

N = 4
solve_n_queens([-1] * N, 0, N)


#########################################################

# Sudoku Solver
# Problem Statement: Fill a 9×9 grid following Sudoku rules.

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or \
           board[row - row % 3 + i // 3][col - col % 3 + i % 3] == num:
            return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

if solve_sudoku(board):
    print_board(board)
else:
    print("No solution exists")

#########################################################


# Word Search (Backtracking in a Grid)
# Problem Statement: Find if a word exists in a grid by moving in 4 directions.

def exist(board, word):
    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[index]:
            return False
        
        temp, board[r][c] = board[r][c], "#"
        found = dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or \
                dfs(r, c + 1, index + 1) or dfs(r, c - 1, index + 1)
        board[r][c] = temp
        return found

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
    return False


board = [
    ['A','B','C','D','E','F','G','H','I','J'],
    ['K','L','M','N','O','P','Q','R','S','T'],
    ['U','V','W','X','Y','Z','A','B','C','D'],
    ['E','F','G','H','I','J','K','L','M','N'],
    ['O','P','Q','R','S','T','U','V','W','X'],
    ['Y','Z','A','B','C','D','E','F','G','H'],
    ['I','J','K','L','M','N','O','P','Q','R'],
    ['S','T','U','V','W','X','Y','Z','A','B'],
    ['C','D','E','F','G','H','I','J','K','L'],
    ['M','N','O','P','Q','R','S','T','U','V']
]

words = [
    "ABCDE",       
    "KPU",         
    "XYZAB",       
    "AFKP",        
    "HELLO",       
    "QRSTUVW",     
    "AZBY",        
]

import copy

for word in words:
    board_copy = copy.deepcopy(board)
    print(f"Searching: {word}")
    print("Result:", exist(board_copy, word))
    print("-" * 30)



'''
-> Backtracking is a powerful technique for solving combinatorial and constraint-based problems.
-> It uses recursive depth-first search (DFS) with pruning to eliminate unnecessary computations.
-> Compared to normal recursion, backtracking eliminates invalid solutions early, making it more efficient.
-> It is widely used in problems like N-Queens, Sudoku, Graph Traversal, and AI Optimization.
'''