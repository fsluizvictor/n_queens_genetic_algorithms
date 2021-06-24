from src.dao.n_queens_dao import NQueensDao
from src.services.n_queens_service import NQueensService


def main():
    dao = NQueensDao(8)
    service = NQueensService()

    individual = dao.create()
    second_individual = dao.create()

    sons = service.recombine(individual,second_individual)

    mutate = service.mutate(sons[0])
    collisions = service.to_rate(sons[1])
    print(collisions)
    collisions_1 = service.to_rate(mutate)
    print(collisions_1)


if __name__ == "__main__":
    main()
