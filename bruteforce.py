import itertools
import csv
import time

start_time = time.time()
budget = 500
csv_data = "actions.csv"
actions = []

with open(csv_data, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        price = float(row["price"])
        if price > 0:
            actions.append({
                "name": row["name"],
                "price": float(row["price"]),
                "profit": float(row["profit"]),
            })

def calculate_profit(combination):
    total_cost = sum(action["price"] for action in combination)
    total_profit = sum(action["profit"] for action in combination)
    return total_cost, total_profit

def algo_bruteforce(actions, budget):
    best_profit = 0
    for r in range(1, len(actions) + 1):
        for combination in itertools.combinations(actions, r):
            actual_cost, actual_profit = calculate_profit(combination)

            if actual_cost <= budget and actual_profit > best_profit:
                best_combination = combination
                best_profit = actual_profit

    print("Meilleure combinaison d'actions:")
    for action in best_combination:
        print(f"{action['name']} - Coût: {action['price']} euros - Bénéfice: {action['profit']}")

    print(f"\nCoût total: {calculate_profit(best_combination)[0]} euros")
    print(f"Bénéfice total: {best_profit} euros")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nTemps d'exécution : {execution_time:.5f} secondes")

algo_bruteforce(actions, budget)


