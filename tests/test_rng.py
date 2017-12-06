import unittest
from duriganbot import rng


class TestRng(unittest.TestCase):
    def test_handle_rand_args(self):
        cases = [[], ['100'], ['0', '100'], ['100', '0'], [0, 100, -1.5], ['0.0', '100', '0'],
                 ['0', '100', '1'], ['0', '100', '0.9']]
        for i in range(0, len(cases)):
            with self.subTest(i=i):
                args = rng.handle_rand_args(cases[i])
                self.assertEquals(args[0], 0.)
                self.assertEquals(args[1], 100.)
                self.assertEquals(args[2], 1)

    def test_handle_rand_args_negative(self):
        cases = [['-100'], ['0', '-100', '1'], ['-100', '0', '1']]
        for i in range(0, len(cases)):
            with self.subTest(i=i):
                args = rng.handle_rand_args(cases[i])
                self.assertEquals(args[0], -100.)
                self.assertEquals(args[1], 0.)
                self.assertEquals(args[2], 1)

    def test_handle_rand_args_cross(self):
        cases = [['100', '-10.5', '5'], ['-10.5', '100', '5']]
        for i in range(0, len(cases)):
            with self.subTest(i=i):
                args = rng.handle_rand_args(cases[i])
                self.assertEquals(args[0], -10.5)
                self.assertEquals(args[1], 100.)
                self.assertEquals(args[2], 5)

    def test_handle_rand_args_error(self):
        cases = [['a'], ['0', 'b'], ['0', '1', 'c']]
        for i in range(0, len(cases)):
            with self.subTest(i=i):
                with self.assertRaises(ValueError):
                    rng.handle_rand_args(cases[i])

    def test_rand(self):
        cases = [[-100., -100., 1], [-100., 0, 2], [-100., 100., 5], [0., 100, 10]]
        for i in range(0, len(cases)):
            with self.subTest(i=i):
                result = rng.rand(cases[i])
                self.assertEquals(len(result), cases[i][2])
                for j in range(0, cases[i][2]):
                    self.assertGreaterEqual(result[j], round(cases[i][0]))
                    self.assertLessEqual(result[j], round(cases[i][1]))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
