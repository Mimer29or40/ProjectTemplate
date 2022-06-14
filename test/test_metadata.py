import unittest

import YOUR_PACKAGE


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertIsNotNone(YOUR_PACKAGE.__metadata_version__, "Metadata Version is None")
        self.assertIsNotNone(YOUR_PACKAGE.__title__, "Package Name is None")
        self.assertIsNotNone(YOUR_PACKAGE.__version__, "Package Version is None")
        self.assertIsNotNone(YOUR_PACKAGE.__summary__, "Package Summary is None")
        self.assertIsNotNone(YOUR_PACKAGE.__author__, "Package Author is None")
        self.assertIsNotNone(YOUR_PACKAGE.__maintainer__, "Package Maintainer is None")
        self.assertIsNotNone(YOUR_PACKAGE.__license__, "Package License is None")
        self.assertIsNotNone(YOUR_PACKAGE.__url__, "Package URL is None")
        self.assertIsNotNone(YOUR_PACKAGE.__download_url__, "Package Download URL is None")
        self.assertIsNotNone(YOUR_PACKAGE.__project_urls__, "Package Version is None")
        self.assertIsNotNone(YOUR_PACKAGE.__copyright__, "Package Version is None")
        self.assertIsNotNone(YOUR_PACKAGE.__data_dir__, "Package Version is None")


if __name__ == "__main__":
    unittest.main()
