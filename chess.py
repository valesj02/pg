from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @property
    @abstractmethod
    def symbol(self):
        pass

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def set_position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        if self.color == "white":
            return [(row + 1, col)] if 0 < row + 1 <= 8 else []
        else:  
            return [(row - 1, col)] if 0 < row - 1 <= 8 else []

    @property
    def symbol(self):
        return '♟' if self.color == "black" else '♙'

    def __str__(self):
        return f'Pawn({self.symbol}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        return [(r, c) for r, c in moves if 0 < r <= 8 and 0 < c <= 8]

    @property
    def symbol(self):
        return '♞' if self.color == "black" else '♘'

    def __str__(self):
        return f'Knight({self.symbol}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for i in range(1, 8):
            moves += [
                (row + i, col + i), (row + i, col - i),
                (row - i, col + i), (row - i, col - i)
            ]
        return [(r, c) for r, c in moves if 0 < r <= 8 and 0 < c <= 8]

    @property
    def symbol(self):
        return '♝' if self.color == "black" else '♗'

    def __str__(self):
        return f'Bishop({self.symbol}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for i in range(1, 8):
            moves += [
                (row + i, col), (row - i, col),
                (row, col + i), (row, col - i)
            ]
        return [(r, c) for r, c in moves if 0 < r <= 8 and 0 < c <= 8]

    @property
    def symbol(self):
        return '♜' if self.color == "black" else '♖'

    def __str__(self):
        return f'Rook({self.symbol}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for i in range(1, 8):
            moves += [
                (row + i, col + i), (row + i, col - i),
                (row - i, col + i), (row - i, col - i),
                (row + i, col), (row - i, col),
                (row, col + i), (row, col - i)
            ]
        return [(r, c) for r, c in moves if 0 < r <= 8 and 0 < c <= 8]

    @property
    def symbol(self):
        return '♛' if self.color == "black" else '♕'

    def __str__(self):
        return f'Queen({self.symbol}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 1, col), (row - 1, col),
            (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row - 1, col + 1), (row - 1, col - 1)
        ]
        return [(r, c) for r, c in moves if 0 < r <= 8 and 0 < c <= 8]

    @property
    def symbol(self):
        return '♚' if self.color == "black" else '♔'

    def __str__(self):
        return f'King({self.symbol}) at position {self.position}'


if __name__ == "__main__":
    pieces = [
        Pawn("white", (2, 2)),
        Pawn("black", (7, 2)),
        Knight("white", (1, 2)),
        Bishop("white", (4, 4)),
        Rook("black", (1, 1)),
        Queen("black", (4, 4)),
        King("white", (5, 5))
    ]
    for piece in pieces:
        print(piece)
        print("Possible moves:", piece.possible_moves())
