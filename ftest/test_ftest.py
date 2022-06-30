from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

class PageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    # def tearDown(self):
    #     self.browser.quit()

    def test_start_list_and_retrieve_it(self):
        self.browser.get(self.live_server_url)
        self.assertIn('The Author', self.browser.title)

        h4Author = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('Contact GotchaNovelist here!', h4Author)
        
        inputName = self.browser.find_element_by_id('userAuthor')
        inputName.send_keys('TestName1')
        self.assertEqual(inputName.get_attribute('placeholder'),'Up to 30 characters!')
        time.sleep(1)
        
        inputEmail = self.browser.find_element_by_id('emailAuthor')
        inputEmail.send_keys('sample1@mailingsite.com')
        self.assertEqual(inputEmail.get_attribute('placeholder'),'E-mail address here!')
        time.sleep(1)
        
        inputNumber = self.browser.find_element_by_id('numAuthor')
        inputNumber.send_keys('0913645127364')
        time.sleep(1)

        inputQuery = self.browser.find_element_by_id('queryAuthor')
        inputQuery.send_keys('Lorem ipsum dolor sit amet.')
        time.sleep(1)
        
        btnConfirm = self.browser.find_element_by_id('confirmAuthor')
        
        btnConfirm.click()
        time.sleep(2)
        
        self.browser.get(self.live_server_url)
        self.assertIn('The Author', self.browser.title)

        h4Author = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('Contact GotchaNovelist here!', h4Author)
        
        inputName = self.browser.find_element_by_id('userAuthor')
        inputName.send_keys('TestName2')
        self.assertEqual(inputName.get_attribute('placeholder'),'Up to 30 characters!')
        time.sleep(1)
        
        inputEmail = self.browser.find_element_by_id('emailAuthor')
        inputEmail.send_keys('sampleemail@mailingsite.com')
        self.assertEqual(inputEmail.get_attribute('placeholder'),'E-mail address here!')
        time.sleep(1)
        
        inputNumber = self.browser.find_element_by_id('numAuthor')
        inputNumber.send_keys('09128937918789886')
        time.sleep(1)

        inputQuery = self.browser.find_element_by_id('queryAuthor')
        inputQuery.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        time.sleep(1)
        
        btnConfirm = self.browser.find_element_by_id('confirmAuthor')
        
        btnConfirm.click()
        table = self.browser.find_element_by_id('testTable')
        row_data = table.find_elements_by_tag_name('tr')
        self.assertIn('1: TestName1, sample1@mailingsite.com, 913645127364, Lorem ipsum dolor sit amet.', [row.text for row in row_data])

# if __name__=='__main__':
#     unittest.main(warnings='ignore')
