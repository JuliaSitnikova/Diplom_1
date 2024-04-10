import random

from praktikum.database import Database

class TestBun:
    def test_get_bun_return_name(self):
        db = Database()
        bun = random.choice(db.available_buns())
        bun_name_from_db = bun.name
        bun_name = bun.get_name()
        assert bun_name == bun_name_from_db

    def test_get_bun_return_price(self):
        db = Database()
        bun = random.choice(db.available_buns())
        bun_price_from_db = bun.price
        bun_price = bun.get_price()
        assert bun_price == bun_price_from_db