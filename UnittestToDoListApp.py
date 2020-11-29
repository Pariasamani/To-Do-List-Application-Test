#Import Libraries
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait

#class for unit test
class BrowserTest(unittest.TestCase):

    # setting up the driver (Chrome)
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:/Users/paria/Drivers/chromedriver.exe")

    #loading the App on the selected driver
    def testLoading(self):
        self.driver.get("http://localhost:3000/")
        titleOfWebPage = self.driver.title
        self.assertEqual("To Do List", titleOfWebPage, "Web Page Title is not the same")
        print("Loading test passed" + titleOfWebPage)

    #Testing that the App works on another browser (it can be anything else: IE, FireFox, Safari,...)
    def testDifferentBrowsers(self):
        self.driver=webdriver.Firefox(executable_path="C:/Users/paria/Drivers/geckodriver.exe")
        self.driver.get("http://localhost:3000/")

        titleOfWebPage = self.driver.title
        self.assertEqual("To Do List", titleOfWebPage, "Web Page Title is not the same")
        print("Loading test passed" + titleOfWebPage)

    #A function(method) to add an item to App to do list
    def additem(self,text_to_add):
        search_field = self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/input")
        search_field.send_keys(text_to_add)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/button").click()


    #Testing that adding single item App works
    def testSingleItemAdd(self):
        self.driver.get("http://localhost:3000/")
        self.additem("Task : Add single Item")
        # uncomment to see th result
        #time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/ul/li")))
        self.assertIsNotNone("//*[@id='root']/div/ul/li","Item Added succesfully")
        # uncomment to see th result
        #time.sleep(2)
        print("Single Item added succesfully!")


    #Testing that clearing single item works
    def testClearSingleItem(self):
        self.driver.get("http://localhost:3000/")
        self.additem("Task: Clearing single item")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/ul/li")))
        # uncomment to see th result
        #time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='root']/div/ul/li").click()
        # uncomment to see th result
        #time.sleep(2)
        count = len(self.driver.find_elements_by_xpath("//*[@id='root']/div/ul/li"))
        self.assertEqual(count,0,"Item Removed succesfully")

    #Testing Adding multiple items works
    def testAddMultipleItems(self,test_mode=True):
        self.driver.get("http://localhost:3000/")
        number_of_tasks=5
        for i in range (number_of_tasks):
            self.additem("Task "+str(i)+": Multiple items adding")
            #uncomment to see th result
            #time.sleep(1)
        # uncomment to see th result
        #time.sleep(1)


        if test_mode==True:
            count = len(self.driver.find_elements_by_xpath("//*[@id='root']/div/ul/li"))
            self.assertEqual(count, number_of_tasks, str(number_of_tasks)+" Item(s) added succesfully")

    #Testing the clear All butoom
    def testClearAllItems(self):
        self.testAddMultipleItems(test_mode=False)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[2]/button").click()
        # uncomment to see th result
        time.sleep(1)
        count = len(self.driver.find_elements_by_xpath("//*[@id='root']/div/ul/li"))
        self.assertEqual(count, 0, "All Item(s) Removed succesfully")


    def TearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
