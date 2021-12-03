from django.test import TestCase


class TestFirstTest(TestCase):
    def setUp(self):
        pass

    def test_first(self):
        print('klk')
        self.assertEqual(True, True)
