from pizza_factory.type_pizza import Pizza
from pizza_factory.factory import PizzaFactory

def main():
    factory = PizzaFactory()
    factory.getPizza(Pizza.PEPPERONI).doPizza()


if __name__ == "__main__":
    main()