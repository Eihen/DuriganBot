import unittest
from duriganbot import rng


class TestRng(unittest.TestCase):

    def test_random_no_args(self):
        rand = rng.random([])
        self.assertEquals(len(rand), 1)
        self.assertGreaterEqual(rand[0], 0)
        self.assertLessEqual(rand[0], 100)

    def test_random_one_postive(self):
        cases = [[0], [1], [13]]
        for i in range(0, 3):
            with self.subTest(i=i):
                rand = rng.random(cases[i])
                self.assertEquals(len(rand), 1)
                self.assertGreaterEqual(rand[0], 0)
                self.assertLessEqual(rand[0], cases[i][0])

    def test_random_one_negative(self):
        cases = [[0], [-1], [-13]]
        for i in range(0, 3):
            with self.subTest(i=i):
                rand = rng.random(cases[i])
                self.assertEqual(len(rand), 1)
                self.assertGreaterEqual(rand[0], cases[i][0])
                self.assertLessEqual(rand[0], 0)

    def test_random_two_args(self):
        cases = [[0, 0], [0, 1], [0, 13], [10, 27], [-1, 0], [-13, 0], [-13, 13], [-27, -10]]
        for i in range(0, 8):
            with self.subTest(i=i):
                rand = rng.random(cases[i])
                self.assertEquals(len(rand), 1)
                self.assertGreaterEqual(rand[0], cases[i][0])
                self.assertLessEqual(rand[0], cases[i][1])

    def test_random_reversed_two_args(self):
        cases = [[1, 0], [13, 0], [27, 10], [0, -1], [0, -13], [13, -13], [-10, -27]]
        for i in range(0, 7):
            with self.subTest(i=i):
                rand = rng.random(cases[i])
                self.assertEquals(len(rand), 1)
                self.assertGreaterEqual(rand[0], cases[i][1])
                self.assertLessEqual(rand[0], cases[i][0])

    def test_random_three_args(self):
        cases = [[0, 13, 2], [-13, 13, 5], [13, 50, 13]]
        for i in range(0, 3):
            with self.subTest(i=i):
                rand = rng.random(cases[i])
                for j in range(0, cases[i][2]):
                    self.assertEquals(len(rand), cases[i][2])
                    self.assertGreaterEqual(rand[j], cases[i][0])
                    self.assertLessEqual(rand[j], cases[i][1])

    def test_random_error(self):
        cases = [['a'], [0, 'b'], [0, 13, 'c']]
        for i in range(0, 3):
            with self.subTest(i=i):
                with self.assertRaises(ValueError):
                    rng.random(cases[i])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
