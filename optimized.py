import csv
import time

start_time = time.time()
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

for action in actions:
    action["weight"] = action["profit"]/action["price"]
sorted_list = sorted(actions, key=lambda p: (p["weight"]), reverse=True)

def algo_optimized():
    budget = 500
    remaining_budget = 500
    spent_budget = 500-remaining_budget
    profit = 0
    best_combination = []
    for element in sorted_list:
        if element["price"] + spent_budget <= budget:
            spent_budget += element["price"]
            profit += element["profit"]
            best_combination.append(element["name"])
        else:
            None
    print("Meilleure combinaison d'actions:", best_combination)
    print(f"\nCoût total: {spent_budget} euros")
    print(f"Bénéfice total: {profit} euros")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nTemps d'exécution : {execution_time:.5f} secondes")

algo_optimized()