import os
import pathlib
import unittest

from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# driver = webdriver.Edge()
driver = webdriver.Chrome()

class Webpage(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri('counter.html'))
        self.assertEqual(driver.title, 'Counter')

    def test_increase(self):
        driver.get(file_uri('counter.html'))
        increase = driver.find_element(by='id', value='increase')
        increase.click()
        self.assertEqual(driver.find_element(by='tag name', value='h1').text, '1')

    def test_decrease(self):
        driver.get(file_uri('counter.html'))
        increase = driver.find_element(by='id', value='decrease')
        increase.click()
        self.assertEqual(driver.find_element(by='tag name', value='h1').text, '-1')

    def test_multiple_increase(self):
        driver.get(file_uri('counter.html'))
        increase = driver.find_element(by='id', value='increase')
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element(by='tag name', value='h1').text, '3')

if __name__ == "__main__":
    unittest.main()
