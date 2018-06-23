#
# ps10pr2.py  (Problem Set 10, Problem 2)
#
# A Connect-Four Player class   
#

from ps10pr1 import Board

# write your class below

class Player:
    """ player class """

    def __init__(self,checker):
        """ constructor for a player object """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns a string representing the player object """
        s = 'Player ' + self.checker
        return s

    def opponent_checker(self):
        """ returns a one character string representing the checker
            of the opponent of self """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """ accepts a board object and returns the column where the player
            wants to make the next move; method asks the player to
            input a column # that represents where the player wants to
            place a checker and will ask until a valid number is given"""
        col_num = int(input('Enter a column: '))
        if board.can_add_to(col_num): 
            column = col_num
            self.num_moves += 1
        else:
            print('Try again!')
            column = self.next_move(board)
        return column
        
