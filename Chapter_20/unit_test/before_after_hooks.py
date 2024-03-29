"""
Unittest - before after hooks

hooks are the tests - their execution

setuo() -> executer before eatch test method - create instances

tearDown() -> execute after test - close instances

"""

import unittest

class TestModule(unittest.TestCase):

    def setUp(self):
        # setUp() configuration
        pass

    def test_first(self):
        # setUp run before test
        # tearDown run after
        pass
    
    def tearDown(self):
        # tearDown() config
        pass