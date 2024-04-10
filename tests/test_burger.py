from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
import pytest

class TestBurger:
    def test_get_receipt(self):
        bun_name = 'bip_bun'
        bun = Bun(name=bun_name, price=1.1)
        ingredient1 = Ingredient('INGREDIENT_TYPE_SAUCE', 'space_sauce', 1.0)
        ingredient2 = Ingredient('INGREDIENT_TYPE_FILLING', 'meteor beef', 200)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        receipt = burger.get_receipt()
        assert '(==== bip_bun ====)' in receipt and '= ingredient_type_sauce space_sauce =' in receipt and'= ingredient_type_filling meteor beef =' in receipt


    def test_burger_only_bun(self):
        bun = Bun(name='bip_bun', price=1.1)
        burger = Burger()
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        assert bun.get_name() in receipt

    def test_burger_bun_with_filling(self):
        bun_name = 'bip_bun'
        bun = Bun(name=bun_name, price=1.1)
        ingredient = Ingredient('INGREDIENT_TYPE_FILLING', 'meteor beef', 200)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        assert ingredient.get_name() in receipt and ingredient.get_type().lower() in receipt

    def test_burger_bun_with_sause(self):
        bun_name = 'bip_bun'
        bun = Bun(name=bun_name, price=1.1)
        ingredient = Ingredient('INGREDIENT_TYPE_SAUCE', 'space_sauce', 1.0)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        assert ingredient.get_name() in receipt and ingredient.get_type().lower() in receipt




    def test_burger_remove_ingredient(self):
        bun_name = 'bip_bun'
        bun = Bun(name=bun_name, price=1.1)
        ingredient1 = Ingredient('INGREDIENT_TYPE_SAUCE', 'space_sauce', 1.0)
        ingredient2 = Ingredient('INGREDIENT_TYPE_FILLING', 'meteor beef', 200)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        receipt = burger.get_receipt()
        assert ingredient1.get_name() not in receipt and ingredient2.get_name() in receipt


    def test_burger_move_ingredient(self):
        bun_name = 'bip_bun'
        bun = Bun(name=bun_name, price=1.1)
        ingredient1 = Ingredient('INGREDIENT_TYPE_SAUCE', 'space_sauce', 1.0)
        ingredient2 = Ingredient('INGREDIENT_TYPE_FILLING', 'meteor beef', 200)
        name1 = ingredient1.get_name()
        name2 = ingredient2.get_name()
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        receipt = burger.get_receipt()
        index1 = receipt.find(name1)
        index2 = receipt.find(name2)
        burger.move_ingredient(0, 1)
        receipt_new = burger.get_receipt()
        new_index1 = receipt_new.find(name1)
        new_index2 = receipt_new.find(name2)
        assert index1 < index2 and new_index1 > new_index2


    @pytest.mark.parametrize('name, price', [
        ['kator bun', 3],
        ['fluorescent bun', 10],
        ['volcanic bun', 7],
        ['Martian bun', 9]
    ])
    def test_burger_bun_total_price(self, name, price):
        bun = Bun(name, price)
        burger = Burger()
        burger.set_buns(bun)
        expected_price = bun.get_price() * 2
        actual_price = burger.get_price()
        assert expected_price == actual_price


    @pytest.mark.parametrize('name, price', [
        ['kator bun', 3],
        ['fluorescent bun', 10],
        ['volcanic bun', 7],
        ['Martian bun', 9]
    ])
    def test_burger_bun_ingredient_total_price(self, name, price):
        ingredients_list = [
            ['INGREDIENT_TYPE_SAUCE', 'space_sauce', 1],
            ['INGREDIENT_TYPE_SAUCE', 'hot ketchup', 5],
            ['INGREDIENT_TYPE_SAUCE', 'cheese sauce', 7],
            ['INGREDIENT_TYPE_SAUCE', 'teriyaki', 3],
            ['INGREDIENT_TYPE_FILLING', 'meteor beef', 200],
            ['INGREDIENT_TYPE_FILLING', 'bio cutlet', 250]]
        bun = Bun(name, price)
        burger = Burger()
        burger.set_buns(bun)
        order_price = bun.get_price() * 2
        for elem in ingredients_list:
            ingredient = Ingredient(ingredient_type=elem[0],
                                    name=elem[1], price=elem[2])
            burger.add_ingredient(ingredient)
            order_price += ingredient.get_price()

        actual_price = burger.get_price()
        assert order_price == actual_price