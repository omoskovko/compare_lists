import unittest
import os
import inspect
import json

from app.list_app import compare_lists

class TestLists(unittest.TestCase):
    @staticmethod
    def get_out_path(*dirList):
        main_file_name = inspect.stack()[0][1]
        incom_folder = 'json'
        return os.path.abspath(os.path.join(os.path.dirname(main_file_name), incom_folder, *dirList))

    def setUp(self):
        with open(self.get_out_path("list1.json"), "r") as f:
            self.list1 = json.load(f)

        with open(self.get_out_path("list2.json"), "r") as f:
            self.list2 = json.load(f)

    def test_lists(self):
        res = compare_lists(self.list1, self.list2)
        self.assertEqual(0, res["list1"]["len_diff"])
        self.assertEqual([], res["list1"]["dif_elems"])

        self.assertEqual(0, res["list2"]["len_diff"])
        self.assertEqual([], res["list2"]["dif_elems"])

if __name__ == '__main__':
    unittest.main()
