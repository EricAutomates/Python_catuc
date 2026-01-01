sandwich_orders = ["tuna", "ham", "chicken", "veggie"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)
