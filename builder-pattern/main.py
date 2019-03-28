from builder.chef import Chef
from builder.pizza_onions import PizzaOnions
from builder.pizza_pepperoni import PizzaPepperoni

def main():
    chef = Chef()
    pizzaPeppe = PizzaPepperoni()
    chef.pizzaBuilder = pizzaPeppe
    chef.preparePizza()
    print(chef.pizzaBuilder)


if __name__ == "__main__":
    main()
    