import itertools
import time

actions = [
    {"name": "Action-1", "price": 20, "profit": 5},
    {"name": "Action-2", "price": 30, "profit": 10},
    {"name": "Action-3", "price": 50, "profit": 15},
    {"name": "Action-4", "price": 70, "profit": 20},
    {"name": "Action-5", "price": 60, "profit": 17},
    {"name": "Action-6", "price": 80, "profit": 25},
    {"name": "Action-7", "price": 22, "profit": 7},
    {"name": "Action-8", "price": 26, "profit": 11},
    {"name": "Action-9", "price": 48, "profit": 13},
    {"name": "Action-10", "price": 34, "profit": 27},
    {"name": "Action-11", "price": 42, "profit": 17},
    {"name": "Action-12", "price": 110, "profit": 9},
    {"name": "Action-13", "price": 38, "profit": 23},
    {"name": "Action-14", "price": 14, "profit": 1},
    {"name": "Action-15", "price": 18, "profit": 3},
    {"name": "Action-16", "price": 8, "profit": 8},
    {"name": "Action-17", "price": 4, "profit": 12},
    {"name": "Action-18", "price": 10, "profit": 14},
    {"name": "Action-19", "price": 24, "profit": 21},
    {"name": "Action-20", "price": 114, "profit": 18},
]

budget = 500

class BruteForce:

    start_time = time.time()
    best_combination = None
    best_profit = 0

    def calculate_profit(self, combination):
        total_cost = sum(action["price"] for action in combination)
        total_profit = sum(action["price"] * action["profit"] / 100 for action in combination)
        return total_cost, total_profit

    def algo_bruteforce(self, actions, budget):
        for r in range(1, len(actions) + 1):
            for combination in itertools.combinations(actions, r):
                actual_cost, actual_profit = self.calculate_profit(combination)

                if actual_cost <= budget and actual_profit > self.best_profit:
                    self.best_combination = combination
                    self.best_profit = actual_profit

        print("Meilleure combinaison d'actions:")
        for action in self.best_combination:
            print(f"{action['name']} - Coût: {action['price']} euros - Bénéfice: {action['profit']}%")

        print(f"\nCoût total: {self.calculate_profit(self.best_combination)[0]} euros")
        print(f"Bénéfice total: {self.best_profit} euros")


    def print_time(self):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print(f"\nTemps d'exécution : {execution_time:.5f} secondes")

BruteForce().algo_bruteforce(actions, budget)
BruteForce().print_time()

