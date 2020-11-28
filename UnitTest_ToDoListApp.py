import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait


class BrowserTest(unittest.TestCase):
    def test_TodoList_Chrome(self):
        self.driver=webdriver.Chrome(executable_path="C:/Users/paria/Drivers/chromedriver.exe")
        self.driver.get("http://localhost:3000/")
        self.driver.quit()


    def test_TodoList_FireFox(self):
        self.driver=webdriver.Firefox(executable_path="C:/Users/paria/Drivers/geckodriver.exe")
        self.driver.get("http://localhost:3000/")
        self.driver.quit()


    def testTitle(self):
        self.driver=webdriver.Chrome(executable_path="C:/Users/paria/Drivers/chromedriver.exe")
        self.driver.get("http://localhost:3000/")
        titleOfWebPage = self.driver.title
        self.assertEqual("To Do List", titleOfWebPage, "Web Page Title is not the same")
        print("Title of the page is:" + titleOfWebPage)

# class AppTesting(unittest.TestCase):

    '''def testAddItem(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/paria/Drivers/chromedriver.exe")
        self.driver.get("http://localhost:3000/")
        add_buttom = self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/button")

        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, add_buttom)))'''




if __name__ == "__main__":
    unittest.main()
