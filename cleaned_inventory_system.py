import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global variable
stock_data = {}


def add_item(item: str = "default", qty: int = 0, logs=None):
    """Add an item and its quantity to the stock."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types for add_item: item=%s, qty=%s", item, qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    log_entry = f"{datetime.now()}: Added {qty} of {item}"
    logs.append(log_entry)
    logging.info(log_entry)


def remove_item(item: str, qty: int):
    """Remove a specific quantity of an item from the stock."""
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types for remove_item: item=%s, qty=%s", item, qty)
        return

    try:
        if item not in stock_data:
            logging.warning("Attempted to remove non-existent item: %s", item)
            return

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Removed item entirely: %s", item)
        else:
            logging.info("Removed %d of %s", qty, item)
    except KeyError as e:
        logging.error("Error removing item: %s", e)


def get_qty(item: str) -> int:
    """Return the quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json"):
    """Load stock data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        logging.info("Loaded data from %s", file)
    except FileNotFoundError:
        logging.warning("File not found: %s. Starting with empty stock.", file)
        stock_data = {}
    except json.JSONDecodeError as e:
        logging.error("Error decoding JSON from %s: %s", file, e)
        stock_data = {}


def save_data(file: str = "inventory.json"):
    """Save current stock data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Saved data to %s", file)
    except OSError as e:
        logging.error("Error saving data: %s", e)


def print_data():
    """Print a simple report of all items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5):
    """Return a list of items below the given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main execution block for demonstration."""
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("orange", 1)

    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
