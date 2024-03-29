import unittest

from robot import Robot


class RobotTests(unittest.TestCase):

    def setUp(self):
        self.megazord = Robot('Megazord', battery=50)
        print('setUp beig executed')

    def test_charge(self):
        self.megazord.charge()
        self.assertEqual(self.megazord.battery, 100)

    def test_say_name(self):
        self.assertEqual(self.megazord.say_name(), "Beep Boop I'm Megazord")
        self.assertEqual(self.megazord.battery, 49)

    def tearDown(self):
        print('TearDown beig executed')


if __name__ == "__main__":
    unittest.main()
