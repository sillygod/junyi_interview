import unittest


def reverse_str(value):
    return value[::-1]


def reverse_words(words):
    return ' '.join([word[::-1] for word in words.split(' ')])


class TestCase(unittest.TestCase):
    def test_reverse_str(self):
        value = 'abc'
        expected = 'cba'

        self.assertEqual(reverse_str(value), expected)

    def test_reverse_words(self):
        words = "flipped class room is important"
        expected = "deppilf ssalc moor si tnatropmi"

        self.assertEqual(reverse_words(words), expected)


if __name__ == '__main__':
    unittest.main()
