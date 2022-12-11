import aoc202201 as aoc
import unittest


class TestAoc202201(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(24000, aoc.part1('example.txt'))

    def test_part2(self):
        self.assertEqual(45000, aoc.part2('example.txt'))
