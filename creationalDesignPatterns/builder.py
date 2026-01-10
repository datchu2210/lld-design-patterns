"""
Builder Pattern - Burger Example
--------------------------------

This module demonstrates the Builder Design Pattern using
a real-world Burger ordering system.

When to use Builder Pattern:
- Object has many optional parameters
- Construction should be step-by-step
- Want readable and maintainable object creation

Pattern Type: Creational
"""

from typing import List


class Burger:
    """
    Product class representing a Burger.

    The Burger object is immutable after creation.
    It receives its configuration from BurgerBuilder.
    """

    def __init__(self, builder: "BurgerBuilder"):
        self.size = builder.size
        self.ingredients = builder.ingredients.copy()

    def __str__(self) -> str:
        ingredients = ", ".join(self.ingredients) if self.ingredients else "Plain"
        return f"Burger(Size={self.size}, Ingredients=[{ingredients}])"


class BurgerBuilder:
    """
    Builder class responsible for constructing Burger objects
    step-by-step using a fluent interface.
    """

    def __init__(self, size: str):
        if not size:
            raise ValueError("Burger size must be provided")

        self.size = size
        self.ingredients: List[str] = []

    def add_cheese(self) -> "BurgerBuilder":
        self.ingredients.append("Cheese")
        return self

    def add_lettuce(self) -> "BurgerBuilder":
        self.ingredients.append("Lettuce")
        return self

    def add_tomato(self) -> "BurgerBuilder":
        self.ingredients.append("Tomato")
        return self

    def add_pepperoni(self) -> "BurgerBuilder":
        self.ingredients.append("Pepperoni")
        return self

    def add_extra_patty(self) -> "BurgerBuilder":
        self.ingredients.append("Extra Patty")
        return self

    def build(self) -> Burger:
        """
        Final build method that creates the Burger object.

        This is the only place where the Burger instance is created.
        """
        return Burger(self)


def main():
    """
    Client code demonstrating usage of Builder Pattern.
    """

    classic_burger = (
        BurgerBuilder("Medium")
        .add_cheese()
        .add_lettuce()
        .add_tomato()
        .build()
    )

    protein_burger = (
        BurgerBuilder("Large")
        .add_extra_patty()
        .add_pepperoni()
        .build()
    )

    print(classic_burger)
    print(protein_burger)


if __name__ == "__main__":
    main()

# 🧠 Interview Question – Builder Pattern (LLD Level)
# Scenario

# You are designing a Food Delivery Application.

# An Order has:

# Mandatory fields

# order_id

# restaurant_name

# Optional fields

# delivery_address

# coupon_code

# instructions

# is_contactless

# scheduled_time

# ❌ Constraints

# You must not use a large constructor with many parameters.

# The Order object should be immutable after creation.

# The client code should be readable and chainable.


class Order:
    def __init__(self,order:"OrderBuilder"):
        
        #required
        self.order_id = order.order_id
        self.restaurant_name = order.restaurant_name

        #optional
        self.delivery_address = order.is_delivery_address
        self.coupon_code = order.is_coupon
        self.instructions = order.is_instructions
        self.addon = order.additioal
        print(self.order_id,self.restaurant_name)
        


class OrderBuilder:

    def __init__(self,order_id,restaurant_name):
        self.order_id = order_id
        self.restaurant_name = restaurant_name
        self.additioal = []
        # print(self.additioal)

    def is_delivery_address(self,address):
        self.additioal.append(address)
        return self

    def is_coupon(self,coupon):
        self.additioal.append(coupon)
        return self

    def is_instructions(self,instructions):
        self.additioal.append(instructions)
        return self

    def build_order(self):
        return Order(self)

OrderBuilder('123','datchu').is_delivery_address('chennai').is_coupon("001").build_order()
