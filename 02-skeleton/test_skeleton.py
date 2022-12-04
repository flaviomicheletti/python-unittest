import unittest


def fun(x):
    return x + 1

class MyFun:
    def fun(self, n):
        return n + 1


class TestingFunctions(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)


class TestingClass(unittest.TestCase):
    def test_fun(self):
        obj = MyFun()
        self.assertEqual(obj.fun(3), 4)


if __name__ == "__main__":
    unittest.main()
