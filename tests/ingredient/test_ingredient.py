from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    meat = Ingredient("carne")
    eggplant = Ingredient("berinjela")
    mozzarella_cheese = Ingredient("queijo mussarela")
    meat_two = Ingredient("carne")
    egg = Ingredient("ovo")

    assert meat.name == "carne"
    assert mozzarella_cheese.name == "queijo mussarela"

    assert repr(meat) == "Ingredient('carne')"
    assert repr(eggplant) == "Ingredient('berinjela')"
    assert repr(mozzarella_cheese) == "Ingredient('queijo mussarela')"
    assert repr(egg) == "Ingredient('ovo')"

    assert Restriction.ANIMAL_MEAT in meat.restrictions
    assert Restriction.ANIMAL_DERIVED in meat.restrictions
    assert Restriction.ANIMAL_DERIVED in mozzarella_cheese.restrictions
    assert Restriction.LACTOSE in mozzarella_cheese.restrictions
    assert eggplant.restrictions == set()

    assert meat.__eq__(egg) is False
    assert meat.__eq__(meat_two) is True

    assert type(hash(meat)) == int
    assert type(hash(egg)) == int

    assert hash(meat) != hash(egg)
    assert hash(meat) == hash(meat_two)
