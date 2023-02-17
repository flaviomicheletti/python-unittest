import unittest

def fun(x):
    return x + 1

class MyFun:
    def fun(self, n):
        return n + 1


class TestingFunctionFun(unittest.TestCase):
    def test_fun(self):
        self.assertEqual(fun(3), 4)


class TestingClassMyFun(unittest.TestCase):
    def test_my_fun(self):
        obj = MyFun()
        self.assertEqual(obj.fun(3), 4)


