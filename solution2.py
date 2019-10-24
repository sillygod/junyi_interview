import unittest


def remove_three_and_five_multiple_without_common(num):
    if num < 1:
        raise ValueError("invalid input")
    return len(
        tuple(
            filter(lambda x: not ((x % 3 == 0 or x % 5 == 0) and x % 15 != 0),
                   range(1, num + 1))))


class TestCase(unittest.TestCase):
    def test_remove_three_and_five_multiple_without_common(self):
        num = 15
        expected = 9

        self.assertEqual(remove_three_and_five_multiple_without_common(num),
                         expected)

    def test_edge_case(self):
        num = 1
        expected = 1

        self.assertEqual(remove_three_and_five_multiple_without_common(num),
                         expected)

    def test_invalid_case(self):
        num = 0

        with self.assertRaises(ValueError):
            remove_three_and_five_multiple_without_common(num)


if __name__ == '__main__':
    unittest.main()
