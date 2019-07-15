"""
A module containing an implementation of a state for Stonehenge and an
implemenetation of a game for Stonehenge.
"""

from typing import Any
from game_state import GameState
from game import Game

class StonehengeState(GameState):
    """
    The state of a game at a certain point in time.
    """
    
    def __init__(self, is_p1_turn: bool, tup: tuple) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.
        
        @param self 'StonehengeState': this current StonehengeState object
        @param is_p1_turn bool: whether or not it is player one's turn
        @param tup tuple: represents the length of a board, along with the 
                          values of ley lines and moves
                          
        @rtype: None
        """        
        super().__init__(is_p1_turn)
        self.length, self.horiz, self.diag_up, self.diag_down, \
            self.leys = tup[0], tup[1], tup[2], tup[3], tup[4]
        
    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        
        @param self 'StonehengeState': this current StonehengeState object
        
        @rtype: str
        """
        
        if self.length == 1:
            
            board = "\n" + "      " + str(self.leys[1][0]) + "   " + \
                str(self.leys[1][1]) + "\n" + "     " + "/" + "   " + "/" \
                + "\n" + str(self.leys[0][0]) + " - " + str(self.horiz[0][0]) \
                + " - " + str(self.horiz[0][1]) + "\n" + "     " + "\\ /" \
                + " \\ " + "\n" + "  " \
                + str(self.leys[0][1]) + " - " \
                + str(self.horiz[1][0]) + "   " \
                + str(self.leys[2][1]) + "\n" \
                + "       " + "\\ " + "\n" + "        " \
                + str(self.leys[2][0]) \
                + "\n"
            
        elif self.length == 2:
            
            board = "\n" + "        " + str(self.leys[1][0]) + "   " \
                + str(self.leys[1][1]) + "\n" + "       " + "/   /" + "\n" \
                + "  " + str(self.leys[0][0]) + " - " + str(self.horiz[0][0]) \
                + " - " + str(self.horiz[0][1]) + "   " + str(self.leys[1][2]) \
                +  "\n" + "     " + "/ \\ / \\ /" + "\n" \
                + str(self.leys[0][1]) \
                + " - " + str(self.horiz[1][0]) + " - " \
                + str(self.horiz[1][1]) + " - " + str(self.horiz[1][2]) \
                + "\n" + "     \\ / \\ / \\ " + " \n" + "  " \
                + str(self.leys[0][2]) + " - " + str(self.horiz[2][0]) \
                + " - " + str(self.horiz[2][1]) + "   " + str(self.leys[2][2]) \
                + "\n" + "       " + "\\   \\ " + "\n" + "        " \
                + str(self.leys[2][0]) + "   " + str(self.leys[2][1]) + "\n"
            
        elif self.length == 3:
            
            board = "\n" + "          " + str(self.leys[1][0]) + "   " \
                + str(self.leys[1][1]) + "\n         /   /\n" \
                + "    " + str(self.leys[0][0]) + " - " \
                + str(self.horiz[0][0]) + " - " \
                + str(self.horiz[0][1]) + "   " + str(self.leys[1][2]) \
                + "\n       / \\ / \\ /\n  " + str(self.leys[0][1]) + " - " \
                + str(self.horiz[1][0]) + " - " + str(self.horiz[1][1]) \
                + " - " + str(self.horiz[1][2]) + "   " + str(self.leys[1][3]) \
                + "\n     / \\ / \\ / \\ /\n" + str(self.leys[0][2]) + " - " \
                + str(self.horiz[2][0]) + " - " + str(self.horiz[2][1]) \
                + " - " + str(self.horiz[2][2]) + " - " \
                + str(self.horiz[2][3]) + "\n     \\ / \\ / \\ / \\ " \
                +  "\n"  + "  " \
                      + str(self.leys[0][3]) + " - " + str(self.horiz[3][0]) \
                      + " - " + str(self.horiz[3][1]) + " - " \
                      + str(self.horiz[3][2]) + "   " + str(self.leys[2][3]) \
                      + "\n       \\   \\   \\ " + "\n" + "        " \
                      + str(self.leys[2][0]) \
                      + "   " + str(self.leys[2][1]) + "   " \
                      + str(self.leys[2][2]) + "\n"
            
        elif self.length == 4:
             
            board = board = "\n            " \
                + str(self.leys[1][0]) + "   " \
                + str(self.leys[1][1]) \
                + "\n           /   /\n" \
                + "      " + str(self.leys[0][0]) + " - " \
                + str(self.horiz[0][0]) + " - " \
                + str(self.horiz[0][1]) + "   " + str(self.leys[1][2]) \
                + "\n         / \\ / \\ /\n    " \
                + str(self.leys[0][1]) + " - " \
                + str(self.horiz[1][0]) + " - " + str(self.horiz[1][1]) \
                + " - " + str(self.horiz[1][2]) + "   " + str(self.leys[1][3]) \
                + "\n       / \\ / \\ / \\ /\n  " \
                + str(self.leys[0][2]) + " - " \
                + str(self.horiz[2][0]) + " - " + str(self.horiz[2][1]) \
                + " - " + str(self.horiz[2][2]) + " - " \
                + str(self.horiz[2][3]) + "   " + str(self.leys[1][4]) \
                + "\n     / \\ / \\ / \\ / \\ /" + "\n" + str(self.leys[0][3]) \
                + " - " + str(self.horiz[3][0]) + " - " \
                + str(self.horiz[3][1]) + " - " + str(self.horiz[3][2]) \
                + " - " + str(self.horiz[3][3]) + " - " \
                + str(self.horiz[3][4]) + "\n     \\ / \\ / \\ / \\ / \\ \n  " \
                + str(self.leys[0][4]) + " - " + str(self.horiz[4][0]) \
                + " - " + str(self.horiz[4][1]) + " - " \
                + str(self.horiz[4][2]) + " - " + str(self.horiz[4][3]) + \
                "   " + str(self.leys[2][4]) + "\n       \\   \\   \\   \\ \n" \
                + "        " + str(self.leys[2][0]) + "   " \
                + str(self.leys[2][1]) + "   " + str(self.leys[2][2]) \
                + "   " + str(self.leys[2][3]) + "\n"
        
        else:
            
            board = "\n              " + str(self.leys[1][0]) + "   " \
                + str(self.leys[1][1]) + "\n             /   /\n" \
                + "        " + str(self.leys[0][0]) + " - " \
                + str(self.horiz[0][0]) + " - " \
                + str(self.horiz[0][1]) + "   " + str(self.leys[1][2]) \
                + "\n           / \\ / \\ /\n      " + str(self.leys[0][1]) \
                + " - " \
                + str(self.horiz[1][0]) + " - " + str(self.horiz[1][1]) \
                + " - " + str(self.horiz[1][2]) + "   " + str(self.leys[1][3]) \
                + "\n         / \\ / \\ / \\ /\n    " \
                + str(self.leys[0][2]) \
                + " - " \
                + str(self.horiz[2][0]) + " - " + str(self.horiz[2][1]) \
                + " - " + str(self.horiz[2][2]) + " - " \
                + str(self.horiz[2][3]) + "   " + str(self.leys[1][4]) \
                + "\n       / \\ / \\ / \\ / \\ /" \
                + "\n  " + str(self.leys[0][3]) \
                + " - " + str(self.horiz[3][0]) + " - " \
                + str(self.horiz[3][1]) + " - " + str(self.horiz[3][2]) \
                + " - " + str(self.horiz[3][3]) + " - " \
                + str(self.horiz[3][4]) + "   " + str(self.leys[1][5]) \
                + "\n     / \\ / \\ / \\ / \\ / \\ / \n" \
                + str(self.leys[0][4]) \
                + " - " + str(self.horiz[4][0]) + " - " \
                + str(self.horiz[4][1]) + " - " + str(self.horiz[4][2]) \
                + " - " + str(self.horiz[4][3]) + " - " \
                + str(self.horiz[4][4]) + " - " + str(self.horiz[4][5]) + \
                "\n     \\ / \\ / \\ / \\ / \\ / \\ \n  " \
                + str(self.leys[0][5]) \
                + " - " + str(self.horiz[5][0]) + " - " \
                + str(self.horiz[5][1]) + " - " + str(self.horiz[5][2]) \
                + " - " + str(self.horiz[5][3]) + " - " \
                + str(self.horiz[5][4]) + "   " + str(self.leys[2][5]) + "\n" \
                + "       \\   \\   \\   \\   \\ \n        " \
                + str(self.leys[2][0]) + "   " + str(self.leys[2][1]) \
                + "   " + str(self.leys[2][2]) + "   " \
                + str(self.leys[2][3]) + "   " + str(self.leys[2][4]) + "\n"
            
        return board
    
    
    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        
        @param self 'StonehengeState': this current StonehengeState object
        
        @rtype: list
        
        >>> h = [['A', 'B'], ['C']]
        >>> du = [['A'], ['B', 'C']]
        >>> dd = [['A', 'C'], ['B']]
        >>> le = [['@', '@'], ['@', '@'], ['@', '@']]
        >>> l = 1
        >>> s = StonehengeState(True, (l, h, du, dd, le))
        >>> s.get_possible_moves()
        ['A', 'B', 'C']
        """
        possible_moves = []
        
        amount_of_leys = 0
        for outer_list in self.leys:
            for element in outer_list:
                amount_of_leys += 1
                
        p1_count = 0
        p2_count = 0
        for outer_list in self.leys:
            for element in outer_list:
                if element == 1:
                    p1_count += 1
                
                elif element == 2:
                    p2_count += 1
                
                    
        if (p1_count >= (amount_of_leys/2) or p2_count >= (amount_of_leys/2)):
            return []
        
        for outer_list in self.horiz:
            for letter in outer_list:
                if isinstance(letter, str):
                    possible_moves.append(letter)
        
        return possible_moves
    
    def make_move(self, move: Any) -> 'StonehengeState':
        """
        Return the GameState that results from applying move to this GameState.
        
        @param self 'StonehengeState': this current StonehengeState object
        @param move Any: the move that is being made
        
        @rtype: 'StonehengeState'
        
        >>> h = [['A', 'B'], ['C']]
        >>> du = [['A'], ['B', 'C']]
        >>> dd = [['A', 'C'], ['B']]
        >>> le = [['@', '@'], ['@', '@'], ['@', '@']]
        >>> l = 1
        >>> s = StonehengeState(True, (l, h, du, dd, le))
        >>> s.make_move('A').p1_turn
        False
        >>> s.make_move('A').length
        1
        >>> s.make_move('A').horiz
        [[1, 'B'], ['C']]
        >>> s.make_move('A').diag_up
        [[1], ['B', 'C']]
        >>> s.make_move('A').diag_down
        [[1, 'C'], ['B']]
        >>> s.make_move('A').leys
        [[1, '@'], [1, '@'], [1, '@']]
        """ 
        # Name of the current player playing
        
        current_player = self.get_current_player_name()
        
        # Making copies of the current lists/values we have
        
        new_length = self.length
        new_horiz = [outer_list[:] for outer_list in self.horiz]
        new_diag_up = [outer_list[:] for outer_list in self.diag_up]
        new_diag_down = [outer_list[:] for outer_list in self.diag_down]
        new_leys = [outer_list[:] for outer_list in self.leys]
        
        # Iterating through the duplicate horizonal list and changing the 
        # designated letter to an integer
        
        
        for outer_list in new_horiz:
            for i in range(len(outer_list)):
                if outer_list[i] == move:
                    outer_list[i] = 1 if current_player == 'p1' else 2
                
                    
        # Iterating through the newly manipulated duplicate horizontal list and 
        # changing the designated '@' symbol in the diplicate leys list to be
        # an integer if possible
    
        
        for i in range(len(new_horiz)):
            p1_count = 0
            p2_count = 0
            for element in new_horiz[i]:
                if element == 1:
                    p1_count += 1
                        
                elif element == 2:
                    p2_count += 1
                        
            if p1_count >= (len(new_horiz[i])/2):
                if not isinstance(new_leys[0][i], int):
                    new_leys[0][i] = 1
                
            elif p2_count >= (len(new_horiz[i])/2):
                if not isinstance(new_leys[0][i], int):
                    new_leys[0][i] = 2
            
            
        # Iterating through the duplicate diagonal up list and changing the 
        # designated letter to an integer 
        
        for outer_list in new_diag_up:
            for i in range(len(outer_list)):
                if outer_list[i] == move:
                    outer_list[i] = 1 if current_player == 'p1' else 2
        
        
        # Iterating through the newly manipulated duplicate diag up list and 
        # changing the designated '@' symbol in the diplicate leys list to be
        # an integer if possible        
                    
        for i in range(len(new_diag_up)):
            p1_count = 0
            p2_count = 0
            for element in new_diag_up[i]:
                if element == 1:
                    p1_count += 1
                                    
                elif element == 2:
                    p2_count += 1
                                    
            if p1_count >= (len(new_diag_up[i])/2):
                if not isinstance(new_leys[1][i], int):
                    new_leys[1][i] = 1
                            
            elif p2_count >= (len(new_diag_up[i])/2):
                if not isinstance(new_leys[1][i], int):
                    new_leys[1][i] = 2
                
                
        # Iterating through the duplicate diagonal down list and changing the 
        # designated letter to an integer   
        
        for outer_list in new_diag_down:
            for i in range(len(outer_list)):
                if outer_list[i] == move:
                    outer_list[i] = 1 if current_player == 'p1' else 2
                    
        
        # Iterating through the newly manipulated duplicate diag down list and 
        # changing the designated '@' symbol in the diplicate leys list to be
        # an integer if possible
                                
        for i in range(len(new_diag_down)):
            p1_count = 0
            p2_count = 0
            for element in new_diag_down[i]:
                if element == 1:
                    p1_count += 1
                                                
                elif element == 2:
                    p2_count += 1
                                                
            if p1_count >= (len(new_horiz[i])/2):
                if not isinstance(new_leys[2][i], int):
                    new_leys[2][i] = 1
                                        
            elif p2_count >= (len(new_horiz[i])/2):
                if not isinstance(new_leys[2][i], int):
                    new_leys[2][i] = 2
            
        # Create a new StonehengeState object with these new lists as attributes
        # and return it
        
        new_state = StonehengeState(not self.p1_turn, (new_length, new_horiz, \
                                    new_diag_up, new_diag_down, new_leys))
        
        return new_state
    
    def __repr__(self) -> str:
        """
        Return a representation of this state (which can be used for
        equality testing).
        
        @param self 'StonehengeState': this current StonehengeState object
        
        @rtype: str
        """     
        
        repres = "P1's turn: {} \nLength of board: {}\
        \nHorizontal Cell Representation: {}\
        \nDiagonal Up Cell Representation: {} \
        \nDiagonal Down Cell Representation: {} \
        \nLey Line Cell Representation (first outer list:" + \
        " horizontal ley lines, second: diagonal up" \
        + " ley lines, third: diagonal down ley lines):" + \
        " {}"
        
        return repres.format(self.p1_turn, self.length, self.horiz, \
                             self.diag_up, self.diag_down, self.leys)
        
    
    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        
        @param self 'StonehengeState': this current StonehengeState object
        
        @rtype: float
        
        >>> h = [['A', 'B'], ['C']]
        >>> du = [['A'], ['B', 'C']]
        >>> dd = [['A', 'C'], ['B']]
        >>> le = [['@', '@'], ['@', '@'], ['@', '@']]
        >>> l = 1
        >>> s = StonehengeState(True, (l, h, du, dd, le))
        >>> s.rough_outcome()
        1
        """    
        possible_moves = self.get_possible_moves()
        new_lst = []
        
        if possible_moves == []:
            return self.LOSE
        
        lst = []
        for value in possible_moves:
            a = self.make_move(value)
            if a.get_possible_moves() == []:
                lst.append(value)
                    
        if len(lst) >= 1:
            return self.WIN
        
        for value in possible_moves:
            a = self.make_move(value)
            for other_value in a.get_possible_moves():
                b = a.make_move(other_value)
                if b.get_possible_moves() == [] and value not in new_lst:
                    new_lst.append(value)
            
        if new_lst == possible_moves:
            return self.LOSE
                
        return self.DRAW
        
    
class StonehengeGame(Game):
    """
    Abstract class for a game to be played with two players.
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.

        @param p1_starts bool: A boolean representing whether Player 1 is the 
                               first to make a move.
        
        @rtype: None
        """
        length = int(input("Enter the length of your board: "))
        
        if length == 1:
            horiz = [['A', 'B'], ['C']]
            diag_up = [['A'], ['B', 'C']]
            diag_down = [['A', 'C'], ['B']]
            leys = [['@', '@'], ['@', '@'], ['@', '@']]
        
        elif length == 2:
            horiz = [['A', 'B'], ['C', 'D', 'E'], ['F', 'G']]
            diag_up = [['A', 'C'], ['B', 'D', 'F'], ['E', 'G']]
            diag_down = [['C', 'F'], ['A', 'D', 'G'], ['B', 'E']]
            leys = [['@', '@', '@'], ['@', '@', '@'], ['@', '@', '@']]
            
        elif length == 3:
            horiz = [['A', 'B'], ['C', 'D', 'E'], ['F', 'G', 'H', 'I'], \
                     ['J', 'K', 'L']]
            diag_up = [['A', 'C', 'F'], ['B', 'D', 'G', 'J'], ['E', 'H', 'K'], \
                       ['I', 'L']]
            diag_down = [['F', 'J'], ['C', 'G', 'K'], ['A', 'D', 'H', 'L'], \
                         ['B', 'E', 'I']]
            leys = [['@', '@', '@', '@'], ['@', '@', '@', '@'], ['@', '@', \
                                                                 '@', '@']]
        elif length == 4:
            horiz = [['A', 'B'], ['C', 'D', 'E'], ['F', 'G', 'H', 'I'], \
                     ['J', 'K', 'L', 'M', 'N'], ['O', 'P', 'Q', 'R']]
            diag_up = [['A', 'C', 'F', 'J'], ['B', 'D', 'G', 'K', 'O'], \
                       ['E', 'H', 'L', 'P'], ['I', 'M', 'Q'], ['N', 'R']]
            diag_down = [['J', 'O'], ['F', 'K', 'P'], ['C', 'G', 'L', 'Q'], \
                         ['A', 'D', 'H', 'M', 'R'], ['B', 'E', 'I', 'N']]
            leys = [['@', '@', '@', '@', '@'], ['@', '@', '@', '@', '@'], \
                    ['@', '@', '@', '@', '@']]
            
        else:
            horiz = [['A', 'B'], ['C', 'D', 'E'], ['F', 'G', 'H', 'I'], \
                     ['J', 'K', 'L', 'M', 'N'], \
                     ['O', 'P', 'Q', 'R', 'S', 'T'], ['U', 'V', 'W', 'X', 'Y']]
            diag_up = [['A', 'C', 'F', 'J', 'O'], \
                       ['B', 'D', 'G', 'K', 'P', 'U'], \
                       ['E', 'H', 'L', 'Q', 'V'], ['I', 'M', 'R', 'W'], \
                       ['N', 'S', 'X'], ['T', 'Y']]
            diag_down = [['O', 'U'], ['J', 'P', 'V'], ['F', 'K', 'Q', 'W'], \
                         ['C', 'G', 'L', 'R', 'X'], \
                         ['A', 'D', 'H', 'M', 'S', 'Y'], \
                         ['B', 'E', 'I', 'N', 'T']]
            leys = [['@', '@', '@', '@', '@', '@'], ['@', '@', '@', '@', \
                                                     '@', '@'], ['@', '@', \
                                                                 '@', '@', \
                                                                 '@', '@']]
            
            
        self.current_state = StonehengeState(p1_starts, (length, horiz, \
                                             diag_up, diag_down, leys))

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.

        @param self 'StonehengeGame': the current StonehengeGame object
        
        @rtype: str
        """
        instructions = "Players take turns claiming cells. When a player" + \
            " captures at least half of the cells in a ley-line, then the" + \
            " player captures that ley-line. The first player to capture" + \
            " at least half of the ley-lines wins."
        
        return instructions
    
    def is_over(self, state: 'StonehengeState') -> bool:
        """
        Return whether or not this game is over.
        
        @param self 'StoneheneGame': this current StonehengeGame object
        @param state 'StonehengeState': a StonehengeState object
        
        @rtype: bool
        """
        
        amount_of_leys = 0
        for outer_list in state.leys:
            for element in outer_list:
                amount_of_leys += 1
                
        p1_count = 0
        p2_count = 0
        for outer_list in state.leys:
            for element in outer_list:
                if element == 1:
                    p1_count += 1
                
                elif element == 2:
                    p2_count += 1
                    
        return p1_count >= amount_of_leys/2 or p2_count >= amount_of_leys/2
    
    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.
        
        @param self 'StonehengeGame': the current StonehengeGame object
        @param player str: the player to check
        
        @rtype: bool
        """
        
        amount_of_leys = 0
        for outer_list in self.current_state.leys:
            for element in outer_list:
                amount_of_leys += 1
        
        
        ley_lines_p1 = 0
        for outer_list in self.current_state.leys:
            for element in outer_list:
                if element == 1:
                    ley_lines_p1 += 1
                        
        if player == 'p1':    
            return self.is_over(self.current_state) and \
                   ley_lines_p1 >= amount_of_leys/2
                                 

        ley_lines_p2 = 0
        for outer_list in self.current_state.leys:
            for element in outer_list:
                if element == 2:
                    ley_lines_p2 += 1
        
        if player == 'p2':             
            return self.is_over(self.current_state) and \
                   ley_lines_p2 >= amount_of_leys/2
        
        return False
        
    def str_to_move(self, string: Any) -> str:
        """
        Return the move that string represents. If string is not a move,
        return an invalid move.

        @param self 'StonehengeGame': this currrent StonehengeGame object
        @param string Any: the move that is being checked
        
        @rtype: str
        """
        if string.strip().isdigit():
            return -1
        
        return string.strip().upper()
        
if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
    import doctest
    doctest.testmod(verbose=True)
        