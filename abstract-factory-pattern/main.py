from pizzas_store.type_store import Store
from pizzas_store.factory import PizzaStoreFactory
from pizza_factory.type_pizza import Pizza


def main():
    """ Main   """
    
    pizzaStore = PizzaStoreFactory()
    pizzaStore.store(Store.CALIFORNIA)\
        .orderPizza(Pizza.PEPPERONI)

    
if __name__ == "__main__":
    main()