import unittest

from example import greeting


class BasicTest(unittest.TestCase):
    def test_basic(self) -> None:
        greeting("Bazel")

    def test_intentional_fail(self) -> None:
        assert False

if __name__ == "__main__":
    unittest.main()
