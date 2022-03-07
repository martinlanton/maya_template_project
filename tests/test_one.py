import unittest
from one.module_one import my_first_var as v_1
from two.module_two import my_second_var as v_2


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_module_one(self):
        self.assertTrue(v_1)

    def test_module_two(self):
        self.assertTrue(v_2 == 2)


if __name__ == '__main__':
    unittest.main()
