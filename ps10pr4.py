#
# ps10pr4.py  (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps10pr3 import *

class AIPlayer(Player):
    """ AIPlayer class that inherits from Player class """

    def __init__(self, checker, tiebreak, lookahead):
        """ Constructor for AIPlayer, takes checker, tiebreak, lookahead as attributes"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ representation of AIPlayer. Returns a string that will indicate the
            checker, tiebreaking strategy, and lookahead """
        s = 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s

    def max_score_column(self, scores):
        """ Takes a list, scores, containing a score for each column on the board
            and returns the index of the column w the max score. If there's multiple
            columns w the max score, the method should use the AIPlayer's tiebreak
            strategy """
        maximum = max(scores)
        max_indices = []
        for index in range(len(scores)):
            if scores[index] == maximum:
                max_indices += [index]
        if self.tiebreak == 'LEFT':
            return max_indices[0]
        if self.tiebreak == 'RIGHT':
            return max_indices[-1]
        if self.tiebreak == 'RANDOM':
            return random.choice(max_indices)

    def scores_for(self, board):
        """ takes board (a Board object) and determines the called AIplayer's
            scores for the columns in board; returns a list containing one score
            for each column """
        scores = [10] * board.width
        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(board)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 50:
                    scores[col] = 50
                board.remove_checker(col)
        return scores

    def next_move(self, board):
        """ returns AIPlayer's judgment of its best possible move """
        scores = self.scores_for(board)
        col = self.max_score_column(scores)
        self.num_moves += 1
        return col
                

