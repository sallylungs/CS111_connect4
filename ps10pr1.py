# ps10pr1.py
# Sally Leung

class Board:
    """ board class """

    def __init__(self, height, width):
        """constructor for board object"""
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string
        
        # add one row of slots at a time
        for row n range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.

        # for hyphens:
        num_hyphens = (self.width*2) + 1
        s += num_hyphens*'-'
        s += '\n'

        # for the numbers corresponding to the position of the columns
        position = 0
        s += ' '
        for col in range(self.width):
            s += str(position) + ' '
            if position <= 8:
                position += 1
            else:
                position = 0
        
        return s

    def add_checker(self, checker, col):
        """ accepts two inputs: checker (one char string that is either
            the 'X' or 'O' checker) and col (an integer that corresponds
            to the index of the column where the checker is to be
            added). """
        
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        if self.slots[-1][col] == ' ':
            self.slots[-1][col] = checker
            
        else:
            for row in range(self.height):
                slot = self.slots[row][col]
                if slot != ' ':
                    self.slots[row-1][col] = checker
                    break

    def reset(self):
        """ resets the board object, setting all slots to contain
            a space character """
        new_board = Board(self.height, self.width)
        self.height = new_board.height
        self.width = new_board.width
        self.slots = new_board.slots

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns True if you can place a checker in col on the
            board, False otherwise"""
        if col < 0 or col > self.width-1:
            return False
        for row in range(self.height):
            slot = self.slots[row][col]
            if slot == ' ':
                return True
        return False

    def is_full(self):
        """ returns True if board object is completely full, False
            otherwise """
        for col in range(self.width):
            if self.can_add_to(col):
                return False
        return True

    def remove_checker(self,col):
        """ removes the top checker from column col of the board;
            if column is empty, method should do nothing """
        for row in range(self.height):
            slot = self.slots[row][col]
            if slot != ' ':
                self.slots[row][col] = ' '
                break

    def is_win_for(self,checker):
        """ returns True if there are 4 consecutive slots containing
            checker on the board; False otherwise """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker):
            return True
        if self.is_vertical_win(checker):
            return True
        if self.is_down_diagonal_win(checker):
            return True
        if self.is_up_diagonal_win(checker):
            return True
        else:
            return False

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ checks for a vertical win for the specified checker """
        for col in range(self.width):
            for row in range(self.height-3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """ checks for an upward slope (left to right) diagonal win for the specified checker """
        for row in range(3,self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ checks for a downward slope (right to left) diagonal win for the specified checker"""
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True
        return False

