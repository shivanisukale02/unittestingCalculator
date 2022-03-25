import calc
import unittest

class Calculator(unittest.TestCase):
    def setUp(self):
        self.a=34
        self.b=50
        print("setUp called")
    def tearDown(self):
        self.a=0
        self.b=0
        print("teardown called")

    def test_add1(self):
        a=3
        b=6
        result=calc.add(a,b)

    def test_sub1(self):
        a = 3
        b = 6
        result = calc.sub(a, b)

    def test_mul1(self):
        a = 3
        b = 6
        result = calc.mul(a,b)

    def test_div1(self):
        a = 3
        b = 6
        result = calc.div(a,b)

if __name__=="__main__":
    unittest.main()

