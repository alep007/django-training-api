from django.test import TestCase

from app.calc import add


class CalcTest(TestCase):

    def test_add_numbers(self):
        # testing 2 numbers being added together
        self.assertEqual(add(3, 8), 11)
