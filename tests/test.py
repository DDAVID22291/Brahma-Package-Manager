import unittest

# None of these have worked to be able to import from src
# from .. import src.fetch
# from ..src import fetch
# sys.path.add trick


class UnitTests(unittest.TestCase):
    def test_nothing(self):
        self.assertEqual(0, 0)


if __name__ == "__main__":
    unittest.main()
