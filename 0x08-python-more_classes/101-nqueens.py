#!/usr/bin/python3
''' Program to solve N Queen Problem using
backtracking
Original solution thanks to geeksforgeeks.org
'''
if __name__ == "__main__":

    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(-1)
    try:
        size_n = int(sys.argv[1])
    except:
        print("N must be a number")
        exit(-1)
    if size_n < 4:
        print("N must be at least 4")
        exit(-1)

    def printSolution(board):
        """Prints the solution with the specified format
        """
        listing = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]:
                    listing.append([i, j])
        print(listing)

    def isSafe(board, row, col):
        """A utility function to check if a queen can
        be placed on board[row][col]. Note that this
        function is called when col queens are
        already placed in columns from 0 to col -1.
        So we need to check only left side for
        attacking queens
        """

        """ Check this row on left side """
        for i in range(col):
            if (board[row][i]):
                return False

        """ Check upper diagonal on left side  """
        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1

        """ Check lower diagonal on left side  """
        i = row
        j = col
        while j >= 0 and i < size_n:
            if board[i][j]:
                return False
            i = i + 1
            j = j - 1

        return True

    ''' A recursive utility function to solve N
    Queen problem '''
    def solveNQUtil(board, col):

        ''' base case: If all queens are placed
        then return true '''
        if col == size_n:
            printSolution(board)
            return True

        ''' Consider this column and try placing
        this queen in all rows one by one '''
        res = False
        for i in range(size_n):

            ''' Check if queen can be placed on
            board[i][col] '''
            if (isSafe(board, i, col)):

                """ Place this queen in board[i][col] """
                board[i][col] = 1

                """ Make result true if any placement
                is possible  """
                res = solveNQUtil(board, col + 1) or res

                """ If placing queen in board[i][col]
                doesn't lead to a solution, then
                remove queen from board[i][col] """
                board[i][col] = 0
                """ BACKTRACK  """

            """ if queen can not be place in any row in
            this column col then return false """
        return res

    def solveNQ():
        """ This function solves the N Queen problem using
        Backtracking. It mainly uses solveNQUtil() to
        solve the problem. It returns false if queens
        cannot be placed, otherwise return true and
        prints placement of queens in the form of 1s.
        Please note that there may be more than one
        solutions, this function prints one of the
        feasible solutions."""

        board = [[0 for j in range(27)]
                 for i in range(27)]

        solveNQUtil(board, 0)
        return

    """ Code execution """
    solveNQ()
