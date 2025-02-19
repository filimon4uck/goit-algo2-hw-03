import csv
import timeit
from BTrees.OOBTree import OOBTree


# Функція для завантаження даних з CSV файлу
def load_data(filename):
    data = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["ID"] = int(row["ID"])
            row["Price"] = float(row["Price"])
            data.append(row)
    return data


# Функція для додавання товарів до OOBTree
def add_item_to_tree(tree, item):
    tree[item["ID"]] = {
        "Name": item["Name"],
        "Category": item["Category"],
        "Price": item["Price"],
    }


# Функція для додавання товарів до словника (dict)
def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = {
        "Name": item["Name"],
        "Category": item["Category"],
        "Price": item["Price"],
    }


# Функція для виконання діапазонного запиту у OOBTree
def range_query_tree(tree, min_price, max_price):
    return list(tree.items(min=min_price, max=max_price))


# Функція для виконання діапазонного запиту у словнику (dict)
def range_query_dict(dictionary, min_price, max_price):
    return [
        value
        for value in dictionary.values()
        if min_price <= value["Price"] <= max_price
    ]


# Основна функція для виконання порівняльного аналізу
def main():
    filename = "data/generated_items_data.csv"
    data = load_data(filename)

    tree = OOBTree()
    dictionary = {}

    # Додавання товарів до OOBTree та словника
    for item in data:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    min_price = 10.0
    max_price = 100.0

    # Вимірювання часу виконання діапазонного запиту для OOBTree
    tree_time = timeit.timeit(
        lambda: range_query_tree(tree, min_price, max_price), number=100
    )

    # Вимірювання часу виконання діапазонного запиту для словника (dict)
    dict_time = timeit.timeit(
        lambda: range_query_dict(dictionary, min_price, max_price), number=100
    )

    # Виведення результатів
    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")


if __name__ == "__main__":
    main()
