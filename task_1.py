import networkx as nx


def create_supply_network():
    """Створюємо граф потоку для мережі постачання"""
    G = nx.DiGraph()

    # Визначаємо з'язки між вузлами та їх пропускну здатність

    connections = [
        ("Термінал 1", "Склад 1", 25),
        ("Термінал 1", "Склад 2", 20),
        ("Термінал 1", "Склад 3", 15),
        ("Термінал 2", "Склад 3", 15),
        ("Термінал 2", "Склад 4", 30),
        ("Термінал 2", "Склад 2", 10),
        ("Склад 1", "Магазин 1", 15),
        ("Склад 1", "Магазин 2", 10),
        ("Склад 1", "Магазин 3", 20),
        ("Склад 2", "Магазин 4", 15),
        ("Склад 2", "Магазин 5", 10),
        ("Склад 2", "Магазин 6", 25),
        ("Склад 3", "Магазин 7", 20),
        ("Склад 3", "Магазин 8", 15),
        ("Склад 3", "Магазин 9", 10),
        ("Склад 4", "Магазин 10", 20),
        ("Склад 4", "Магазин 11", 10),
        ("Склад 4", "Магазин 12", 15),
        ("Склад 4", "Магазин 13", 5),
        ("Склад 4", "Магазин 14", 10),
    ]

    # Додаємо ребра у граф

    for u, v, capacity in connections:
        G.add_edge(u, v, capacity=capacity)
    return G


def calculete_maximum_flow(G, sources, sinks):
    """Обчислює максимальний потік від терміналів до магазинів через склади"""
    # Додаємо штучне джерело та стік

    G.add_node("Джерело")
    G.add_node("Стік")

    # З'єднуємо джерело з терміналами

    for source in sources:
        G.add_edge("Джерело", source, capacity=float("inf"))
    # З'єднуємо магазини зі стоком
    for sink in sinks:
        G.add_edge(sink, "Стік", capacity=float("inf"))

    # Використовуємо алгоритм Едмонса-Карпа для пошуку максимального потоку

    max_flow, flow_distribution = nx.maximum_flow(
        G, "Джерело", "Стік", flow_func=nx.algorithms.flow.edmonds_karp
    )
    return max_flow, flow_distribution


def show_results(flow_distribution):
    """Виводить результати розподілу потоку"""
    print("Розподіл потоку")
    results = []
    for start, destinations in flow_distribution.items():
        for end, flow in destinations.items():
            if flow > 0:
                results.append([start, end, flow])
    header = (
        f"| {'Термінал':<10} | {'Магазин':<10} | {'Фактичний Потік (одиниць)':<26} |"
    )
    separator = f"+{'-' * 12}+{'-' * 12}+{'-' * 28}+"
    print(separator)
    print(header)
    print(separator)
    for result in results:
        print(f"| {result[0]:<10} | {result[1]:<10} | {result[2]:<26} |")
    print(separator)


def main():
    # Створюємо граф мережі постачання:
    G = create_supply_network()

    terminals = ["Термінал 1", "Термінал 2"]
    stores = [
        "Магазин 1",
        "Магазин 2",
        "Магазин 3",
        "Магазин 4",
        "Магазин 5",
        "Магазин 6",
        "Магазин 7",
        "Магазин 8",
        "Магазин 9",
        "Магазин 10",
        "Магазин 11",
        "Магазин 12",
        "Магазин 13",
        "Магазин 14",
    ]

    # Обчислюємо максимальний потік у системі
    max_flow, flow_distribution = calculete_maximum_flow(G, terminals, stores)
    print(f"Максимальний можливий потік: {max_flow}")
    show_results(flow_distribution)


if __name__ == "__main__":
    main()
