
import org.anderes.edu.python.PythonicCardDesk
import unittest

class FrenchDeckTestCase(unittest.TestCase):
    def test_feature_one(self):
        deck = org.anderes.edu.python.PythonicCardDesk.FrenchDeck()
        assert len(deck) == 52
        assert deck[0].rank == "2"
        
if __name__ == '__main__':
    unittest.main()