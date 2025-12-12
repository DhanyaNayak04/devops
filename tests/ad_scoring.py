import unittest
from ad_scoring import score_ad

class TestAdScoring(unittest.TestCase):
    def test_score_positive(self):
        self.assertGreater(score_ad({'clicks': 10, 'views': 100}), 0)

    def test_score_zero(self):
        self.assertEqual(score_ad({'clicks': 0, 'views': 0}), 0)

if __name__ == '__main__':
    unittest.main()