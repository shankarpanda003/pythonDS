def process_events(events):
    prices = {}      # current price of each item
    profit = 0
    result = []

    for event in events:
        parts = event.split()

        if parts[0] == "BUY":
            item, price = parts[1], int(parts[2])
            prices[item] = price
            profit -= price

        elif parts[0] == "SELL":
            item, price = parts[1], int(parts[2])
            prices[item] = price
            profit += price

        elif parts[0] == "CHANGE":
            item, delta = parts[1], int(parts[2])
            prices[item] += delta

        elif parts[0] == "QUERY":
            result.append(profit)

    return result


events = [
    "BUY headphones 20",
    "BUY laptop 50",
    "CHANGE headphones 6",
    "QUERY",
    "SELL laptop 10",
    "CHANGE laptop -2",
    "QUERY"
]

print(process_events(events))
