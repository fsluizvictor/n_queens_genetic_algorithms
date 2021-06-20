from src.models.n_queens import NQueens


class NQueenDao(object):
    _amount_queens: int

    def __init__(self, amount_queens):
        self._amount_queens = amount_queens

    @property
    def amount_queens(self):
        return self._amount_queens

    def create(self) -> NQueens:
        return NQueens(self.amount_queens)
