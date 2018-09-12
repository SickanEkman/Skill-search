import unittest
from skill_search import match_skills


class TestRegex(unittest.TestCase):

    def test_regex(self):
        word = {"ord"}
        hits1 = "ord  ordn  orden  ordet  ordar  ordor  order ordr"
        hits2 = "/ord /ord/ /orden: /orden- orden. orden, orden'"
        hits3 = "-ord -orden/ /ord /orden"
        miss1 = "ordpar ordrar ^ord orrd \ord or:d :ord ord? 'ord'"
        self.assertEqual(match_skills(word, hits1),
                         {("ord", 0, 4), ("ord", 4, 10), ("ord", 10, 17), ("ord", 17, 24),
                          ("ord", 24, 31), ("ord", 31, 38), ("ord", 38, 45)},
                         "Regex matches Suffixes n, en, et")
        self.assertEqual(match_skills(word, hits2),
                         {("ord", 0, 5), ("ord", 5, 10), ("ord", 11, 18), ("ord", 19, 26),
                          ("ord", 26, 33), ("ord", 33, 40), ("ord", 40, 47)},
                         "Regex matches the right punctuation after word")
        self.assertEqual(match_skills(word, hits3),
                         {("ord", 0, 5), ("ord", 5, 12), ("ord", 13, 18), ("ord", 18, 24)},
                         "Regex matches hyphen and slash before word")
        self.assertFalse(len(match_skills(word, miss1)),
                         "Regex doesn't match wrong things")


if __name__ == '__main__':
    unittest.main()
