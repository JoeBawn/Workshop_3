"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    # to get the player: self.player
    # self.player == Player.WHITE
    # self.player == Player.BLACK


    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        available_moves = []

        if self.player == Player.WHITE: 
            if current_square.row == 1:
                #if Square.at(current_square.row) == 2:
                two_squares_in_front = Square.at(current_square.row +2, current_square.col)
                available_moves.append(two_squares_in_front)
            else:
                square_in_front = Square.at(current_square.row +1, current_square.col)
                available_moves.append(square_in_front)
  
        if self.player == Player.BLACK: 
            if current_square.row == 6:
                #if Square.at(current_square.row) == 7:
                two_squares_in_front = Square.at(current_square.row -2, current_square.col)
                available_moves.append(two_squares_in_front)
            else:
                square_in_front = Square.at(current_square.row -1, current_square.col)# current_square.row
                available_moves.append(square_in_front)


        # current_square.col
        # Square.at(4, 6)
        # Square.at(current_square.row + 1, 6)

        return available_moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []