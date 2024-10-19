# Class for Restaurant
class Restaurant:
    def __init__(self, restaurant_id, name, location_x, location_y):
        self.restaurant_id = restaurant_id
        self.name = name
        self.location_x = location_x  # X coordinate of the restaurant
        self.location_y = location_y  # Y coordinate of the restaurant
        self.menu = []

    def add_dish(self, dish):
        self.menu.append(dish)

    def remove_dish(self, dish_name):
        self.menu = [dish for dish in self.menu if dish.name != dish_name]

    def __str__(self):
        return f"Restaurant: {self.name}, Dishes: {[dish.name for dish in self.menu]}"

# Class for Dish
class Dish:
    def __init__(self, dish_id, name, price, is_available=True):
        self.dish_id = dish_id
        self.name = name
        self.price = price
        self.is_available = is_available

    def change_availability(self, availability):
        self.is_available = availability

# Class for Customer
class Customer:
    def __init__(self, customer_id, name, location_x, location_y):
        self.customer_id = customer_id
        self.name = name
        self.location_x = location_x  # X coordinate of the customer
        self.location_y = location_y  # Y coordinate of the customer
        self.order_history = []

    def place_order(self, order):
        self.order_history.append(order)

    def view_order_status(self, order):
        return order.status

    def cancel_order(self, order):
        if order.status == "Pending":
            self.order_history.remove(order)
            return "Order cancelled"
        return "Order cannot be cancelled"

# Class for Order
class Order:
    def __init__(self, order_id, customer, restaurant, dishes):
        self.order_id = order_id
        self.customer = customer
        self.restaurant = restaurant
        self.dishes = dishes  # List of Dish objects
        self.status = "Pending"  # Status: Pending, In Preparation, Delivered

    def update_status(self, new_status):
        self.status = new_status

    def add_dish(self, dish):
        self.dishes.append(dish)

    def remove_dish(self, dish_name):
        self.dishes = [dish for dish in self.dishes if dish.name != dish_name]
