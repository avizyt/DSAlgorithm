import heapq
from datetime import datetime


class Refrigerator:
    def __init__(self) -> None:
        self.items = []

    def addItem(self, item_name, expiration_date):
        """
        Add an item with its expiration data.
        """
        heapq.heappush(self.items, (expiration_date, item_name))
        print(f"Added {item_name} with expiration date {expiration_date}")

    def getNextItem(self):
        """Retrieve the item with the soonest expiration date."""
        if self.items:
            expiration_date, item_name = heapq.heappop(self.items)
            print(f"Use {item_name} by {expiration_date}")
            return item_name
        else:
            print("No items in the refrigerator!")
            return None

    def peekNextItem(self):
        """View the next item to expire without removing it."""
        if self.items:
            expiration_date, item_name = self.items[0]
            print(f"Next to use: {item_name}, expire on {expiration_date}")
            return item_name
        else:
            print("No items in the refrigerator!")
            return None


if __name__ == "__main__":
    fridge = Refrigerator()
    fridge.addItem("Milk", datetime(2024, 11, 15))
    fridge.addItem("Yogurt", datetime(2024, 11, 10))
    fridge.addItem("Cheese", datetime(2024, 11, 20))

    # Check the next item to use
    fridge.peekNextItem()

    # Get and use the next item to expire
    fridge.getNextItem()

    # Check the next item again
    fridge.peekNextItem()
