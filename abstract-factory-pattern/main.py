from pizza_factory.type_pizza import Pizza

from pizzas_store.factory import PizzaStoreFactory
from pizzas_store.texas_store import TexasStore
from pizzas_store.calif_store import CaliforniaStore
from pizzas_store.ny_store import NYStore


def main():
    store = PizzaStoreFactory(CaliforniaStore())
    store.order(Pizza.PEPPERONI)


if __name__ == "__main__":
    main()