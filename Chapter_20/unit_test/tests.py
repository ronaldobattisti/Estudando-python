"""
test is done in different files
"""

import unittest

from activeties import eat, sleep


class TestsActivetis(unittest.TestCase):

    def test_eat_healthy(self):
        """testing return with healthy food"""
        self.assertEqual(
            eat('quiabo', True),
            "I'm eating quiabo and it's good"
        )

    def test_eat_unhealthy(self):
        """testing return with unhealthy food"""
        self.assertEqual(
            eat(food='pizza', is_healthy=False),
            "I'm eating pizza and it's bad"
        )

    def test_sleep_bit(self):
        """testing return sleeping bad"""
        self.assertEqual(
            sleep(4),
            'Still tired'
        )

    def test_sleep_lot(self):
        """testing return sleeping well"""
        self.assertEqual(
            sleep(10),
            'My back hurts'
        )


if __name__ == '__main__':
    unittest.main()
