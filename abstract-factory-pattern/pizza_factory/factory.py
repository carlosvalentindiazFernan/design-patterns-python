from .pizza_california import PizzaCalifornia
from .pizza_chicago import PizzaChicago
from .pizza_greek import PizzaGreek
from .pizza_margherita import PizzaMargherita
from .pizza_onions import PizzaOnions
from .pizza_pepperoni import PizzaPepperoni
from .pizza_pepperoni import PizzaAdapter
from .type_pizza import Pizza


class PizzaFactory:
    """ Pizza Factory """

    def getPizza(self,pizza):
        """ Factory for getPizza """

        if pizza == Pizza.CALIFORNIA:
            return PizzaCalifornia()
        elif pizza == Pizza.CHICAGO:
            return PizzaChicago()
        elif pizza == Pizza.GREEK:
            return PizzaGreek()
        elif pizza == Pizza.MARGHERITA:
            return PizzaMargherita()
        elif pizza == Pizza.ONIONS:
            return PizzaOnions()
        elif pizza == Pizza.PEPPERONI:
            return PizzaPepperoni()
        else:
            raise Exception('Invalid Pizza')


    def __str__(self):
        return 'Pizza Factory'