"""
A module for strategies.
"""

from typing import Any
import random
from classes import Tree, Stack

def interactive_strategy(game: 'Game') -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)

def rough_outcome_strategy(game: 'Game') -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.
    
    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2 # Temporarily -- just so we can replace this easily later
    
    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)
        
        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move
    
    # Return the move that resulted in the best rough_outcome
    return best_move

def iterative_minimax(game: 'Game') -> Any:
    """
    Returns the best score available for a certain game using an iterative 
    approach.
    
    @param game 'Game': the Game object that represents the game being played
    
    @rtype: Any
    """
    tree_list = []
    tree_list.append(Tree((game.current_state, [], None, None)))
    
    s = Stack()
    s.add(tree_list[0])
    
    a_lst = []
   
    while not s.is_empty():
        p = s.remove()
        if (p.children == []) and p.value.get_possible_moves() != []:
            moves = [p]
            
            for value in p.value.get_possible_moves():
                q = Tree((p.value.make_move(value), [], None, value))
                p.children.append(q)
                tree_list.append(q)
                moves.append(q)
            
            a_lst.append(moves)
            
            for node in tree_list:
                s.add(node)
   
        elif (p.children == []) and p.value.get_possible_moves() == []:
            old_state = game.current_state
            game.current_state = p.value
            
            if not game.is_winner('p1') and not game.is_winner('p2'):
                p.score = 0
                game.current_state = old_state
                
            else:
                p.score = -1
                game.current_state = old_state
            
        else:
            lst_scores = []
            for node in p.children:
                lst_scores.append(node.score * -1)
                
            p.score = max(lst_scores)
    
    for outer_list in a_lst:
        if game.current_state.__repr__() == outer_list[0].value.__repr__() \
           and outer_list[0].children != []:
            
            lst = []
            for node in outer_list[0].children:
                if node.value.get_possible_moves() == []:
                    lst.append(node.move_made)
                    
            if len(lst) == 1:
                return lst[0]
            
            elif len(lst) >= 1:
                return random.choice(lst)
            
            m = [(node.move_made, node.score) for node in outer_list[1:]]
            lst = []
            
            for item in m:
                if item[1] == outer_list[0].score * -1:
                    lst.append(item[0])
                        
            return random.choice(lst)
            
    return -1
    
def recursive_helper(t: 'Tree', game: 'Game') -> Any:
    """
    A recursive minimax helper function that returns the best available move
    that can be played by a player for a certain game.
    
    @param t 'Tree': a Tree onject that is a representation of a specific state 
                     within the game
    @param game 'Game': a Game object that represents the current game being
                        played
                        
    @rtype: Any
    """
    if t.value.get_possible_moves() == []:
        old_state = game.current_state
        game.current_state = t.value
        
        if not game.is_winner('p1') and not game.is_winner('p2'):
            t.score = 0
            game.current_state = old_state
            
        else:
            t.score = -1
            game.current_state = old_state
            
        return t.score
    
    elif t.value.get_possible_moves() != [] and \
         t.value.__repr__() != game.current_state.__repr__():
        for move in t.value.get_possible_moves():
            q = Tree((t.value.make_move(move), [], None, move))
            
            if q.value.get_possible_moves() == []:
                q.score = recursive_helper(q, game)
                
            else:
                q.score = max([-1 * \
                               recursive_helper(Tree((q.value.make_move(x), \
                                                        [], None, x,)), game)\
                               for x in q.value.get_possible_moves()])
            
            t.children.append(q)
            
        t.score = max([x.score * -1 for x in t.children])
        return t.score
            
    else:
        for value in game.current_state.get_possible_moves():
            node = Tree((t.value.make_move(value), [], None, value))
            t.children.append(node)
            
        for node in t.children:
            if node.value.get_possible_moves() == []:
                return node.move_made
        
        lst = []
        t.score = max([-1 * recursive_helper(x, game) for x in t.children])
        for node in t.children:
            if node.score == t.score * -1:
                lst.append(node.move_made)
                
        return random.choice(lst)
    
def recursive_minimax(game: 'Game') -> Any:
    """
    A recursive minimax implementation that returns the best score that the 
    a player can make for a certain game.
    
    @param game 'Game': a Game object that represents the current game being
                        played
                        
    @rtype: Any
    """
    t = Tree((game.current_state, [], None, None))
    return recursive_helper(t, game)
    
if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
