from src.services.genetic_algorithm_service import GeneticAlgorithmService
from src.services.n_queens_service import NQueensService
from src.view.view_data import ViewData


class GeneticAlgotithmController:

    def __init__(self):
        self.view = ViewData()
        self.n_queens_service = NQueensService()
        self.genetic_algorithm_service = GeneticAlgorithmService(self.n_queens_service, self.view)

    def run_genetic_algorithm(self):
        self.genetic_algorithm_service.execute()
