from praktikum.database import Database

class TestDatabase:
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) != 0


    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) != 0