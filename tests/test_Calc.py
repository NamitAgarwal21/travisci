from config.Calculator import Calculator


class TestCalci():

    def test_add(self):
        x, y = 1, 2
        instance = Calculator(x, y)
        assert instance.add() == x + y , "Some issue in Add Method"

    def test_minus(self):
        x, y = 2, 1
        instance = Calculator(x, y)
        assert instance.minus() == x - y, "Some issue in Minus Method"

    def test_multi(self):
        x, y = 2, 1
        instance = Calculator(x, y)
        assert instance.multi() == x * y, "Some issue in Multi Method"
