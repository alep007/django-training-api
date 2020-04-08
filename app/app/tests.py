from django.test import TestCase

from app.calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        # testing 2 numbers being added together
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        # test 2 numbers are subtracted
        self.assertEqual(subtract(5, 11), 6)
