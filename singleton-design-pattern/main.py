from singleton import Singleton

class PizzasStore(metaclass=Singleton):
    """ Pizza Store Using Singleton """
    

    def takePizza(self):
        print("Woeo Pizza")

    def __str__(self):
        return 'Pizzas Store'

    


def main():
    store = PizzasStore()
    store2 = PizzasStore()

    print(f'store {store}')
    print(f'store2 {store2}')

if __name__ == "__main__":
    main()