from django.test import TestCase

class MyTestClass(TestCase):
    def setUp(self):
        print("Hello SetUp!")

    def test_false_if_false(self):
        self.assertTrue(True)

    def test_false_if_true(self):
        self.assertFalse(False)

    def tearDown(self):
        print("hello TearDown")