from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    pizza = Dish("Pizza de queijo", 15.00)
    pizza_two = Dish("Pizza de queijo", 15.00)
    chicken = Dish("Frango Assado", 20.00)

    assert pizza.name == "Pizza de queijo"
    assert pizza.price == 15.00

    assert repr(pizza) == "Dish('Pizza de queijo', R$15.00)"

    assert pizza.__eq__(pizza_two) is True
    assert pizza.__eq__(chicken) is False

    assert type(hash(pizza)) == int
    assert hash(pizza) == hash(pizza_two)
    assert hash(pizza) != hash(chicken)

    pizza.add_ingredient_dependency(Ingredient("queijo mussarela"), 1)
    pizza.add_ingredient_dependency(Ingredient("queijo provolone"), 1)
    pizza.add_ingredient_dependency(Ingredient("queijo provolone"), 1)

    assert pizza.get_ingredients() == {
        Ingredient("queijo mussarela"),
        Ingredient("queijo provolone"),
        Ingredient("queijo provolone"),
    }

    assert Restriction.ANIMAL_DERIVED in pizza.get_restrictions()

    with pytest.raises(TypeError):
        Dish("Frango", "Pizza")
    with pytest.raises(ValueError):
        Dish("Frango", -1)
