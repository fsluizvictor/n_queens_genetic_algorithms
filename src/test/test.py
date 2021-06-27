from src.dao.n_queens_dao import NQueensDao
from src.models.n_queens import NQueens
from src.services.n_queens_service import NQueensService


def main():
    teste = NQueens()
    print(teste.is_rated)
    print(teste.rate)
    print(teste.genes)
    teste.is_rated = True
    print(teste.is_rated)


if __name__ == "__main__":
    main()
