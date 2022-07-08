import unittest
import filecmp
from challenge import Challenge

class ChallengeTest(unittest.TestCase):

    def test_case_normal(self):
        Challenge("./test_files/input-basic-normal.txt", None).run()
        outputFile = open("./output.txt","r")
        try:
            self.assertEqual(outputFile.read(), '-4,16\n0,12\n5,7\n')
        finally:
            outputFile.close()
    
    def test_case_100_items(self):
        Challenge("./test_files/input-100-items.txt","./output.txt").run()
        self.assertTrue(filecmp.cmp("./output.txt", "./test_files/input-100-items-expect.txt"))

    def test_case_1000_items(self):
        Challenge("./test_files/input-1000-items.txt","./output.txt").run()
        self.assertTrue(filecmp.cmp("./output.txt", "./test_files/input-1000-items-expect.txt"))

    def test_case_10000_items(self):
        Challenge("./test_files/input-10000-items.txt","./output.txt").run()
        self.assertTrue(filecmp.cmp("./output.txt", "./test_files/input-10000-items-expect.txt"))

unittest.main()