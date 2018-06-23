#
# ps10pr3.py  (Problem Set 10, Problem 3)
#
# Playing the game    
#

from ps10pr1 import Board
from ps10pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

def process_move(player, board):
    """ takes parameters player (Player object whose move will be processed) and
        board (Board object for game being played) and should process a single
        move by the player """
    print(player,"'s turn")
    col = player.next_move(board)
    board.add_checker(player.checker, col)
    print()
    print(board)
    print()
    if board.is_win_for(player.checker):
        print(player, 'wins in', player.num_moves, 'moves. \nCongratulations!')
        return True
    if board.is_full():
        print("It's a tie!")
        return True
    return False

class RandomPlayer(Player):
    """ class for RandomPlayer, inherits from Player class """

    def next_move(self, board):
        """ overrides the next_move method inherited from Player. This next_move
            will choose at random the columns in the specified board that are
            not yet full, and return the index of that column"""
        avail_columns = []
        for col in range(board.width):
            if board.can_add_to(col):
                avail_columns += [col]
        choice = random.choice(avail_columns)
        self.num_moves += 1
        return choice
        
