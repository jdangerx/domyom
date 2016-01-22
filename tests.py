from collections import namedtuple
import unittest

from domyom import Domyom

PlayerInfo = namedtuple("PlayerInfo", ["treasure", "bank", "hand", "discard", "deck"])


class DomyomTest(unittest.TestCase):
    def setUp(self):
        self.domyom = Domyom()

    def test_two_five(self):
        choice = self.domyom.buy_choice(PlayerInfo(**{
            "treasure": 2,
            "bank": {"Smithy": 10, "Village": 10},
            "hand": [],
            "discard": [],
            "deck": ["Copper"] * 7 + ["Estate"] * 3
        }))
        self.assertEqual(choice, "Copper")

        choice = self.domyom.buy_choice(PlayerInfo(**{
            "treasure": 5,
            "bank": {"Smithy": 10, "Village": 10},
            "hand": [],
            "discard": [],
            "deck": ["Copper"] * 8 + ["Estate"] * 3
        }))
        self.assertEqual(choice, "Smithy")

    def test_five_two(self):
        choice = self.domyom.buy_choice(PlayerInfo(**{
            "treasure": 5,
            "bank": {"Smithy": 10, "Village": 10},
            "hand": [],
            "discard": [],
            "deck": ["Copper"] * 7 + ["Estate"] * 3
        }))
        self.assertEqual(choice, "Smithy")

        choice = self.domyom.buy_choice(PlayerInfo(**{
            "treasure": 2,
            "bank": {"Smithy": 10, "Village": 10},
            "hand": [],
            "discard": [],
            "deck": ["Copper"] * 7 + ["Estate"] * 3
        }))
        self.assertEqual(choice, "Copper")

    def test_four_three(self):
        choice = self.domyom.buy_choice(PlayerInfo(**{
            "treasure": 4,
            "bank": {"Smithy": 10, "Village": 10},
            "hand": [],
            "discard": [],
            "deck": ["Copper"] * 7 + ["Estate"] * 3
        }))
        self.assertEqual(choice, "Smithy")

        choice = self.domyom.buy_choice(PlayerInfo(**{
            "treasure": 3,
            "bank": {"Smithy": 10, "Village": 10},
            "hand": [],
            "discard": [],
            "deck": ["Copper"] * 7 + ["Estate"] * 3
        }))
        self.assertEqual(choice, "Silver")

    def test_three_four(self):
        choice = self.domyom.buy_choice(PlayerInfo(**{
            "treasure": 3,
            "bank": {"Smithy": 10, "Village": 10},
            "hand": [],
            "discard": [],
            "deck": ["Copper"] * 7 + ["Estate"] * 3
        }))
        self.assertEqual(choice, "Silver")

        choice = self.domyom.buy_choice(PlayerInfo(**{
            "treasure": 4,
            "bank": {"Smithy": 10, "Village": 10},
            "hand": [],
            "discard": [],
            "deck": ["Copper"] * 7 + ["Estate"] * 3 + ["Silver"]
        }))
        self.assertEqual(choice, "Smithy")

if __name__ == "__main__":
    unittest.main()
